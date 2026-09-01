from typing import List, Optional
from dataclasses import dataclass

from deepeval.confident.api import HttpMethods

from memory_dna.vulnerabilities import (
    BaseVulnerability,
)
from memory_dna.attacks import BaseAttack
from memory_dna.confident.api import Api, Endpoints
from memory_dna.frameworks.api import RedTeamingFrameworkHttpResponse
from memory_dna.frameworks.risk_category import RiskCategory
from memory_dna.frameworks.utils import build_risk_categories
from memory_dna.utils import add_pbar, create_progress, update_pbar


@dataclass
class RedTeamingFramework:
    name: str = ""
    description: str = ""
    vulnerabilities: Optional[List[BaseVulnerability]] = None
    attacks: Optional[List[BaseAttack]] = None
    risk_categories: Optional[List[RiskCategory]] = None
    _has_dataset: bool = False
    _id: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True

    def get_name(self) -> str:
        return self.name

    def pull(self, id: str, confident_api_key: Optional[str] = None) -> None:
        """
        Pull a red teaming framework from Confident AI to run it locally.
        """
        api = Api(api_key=confident_api_key)
        progress = create_progress()
        with progress:
            task_id = add_pbar(
                progress,
                description=f"⬇️  Pulling framework '{id}' from Confident AI",
                total=1,
            )
            data, _ = api.send_request(
                method=HttpMethods.GET,
                endpoint=Endpoints.RT_FRAMEWORK_ENDPOINT,
                url_params={"frameworkId": id},
            )
            update_pbar(progress, task_id, advance_to_end=True)

        response = RedTeamingFrameworkHttpResponse(**data["framework"])
        risk_categories = build_risk_categories(
            response.risk_categories, response.name
        )

        if not risk_categories:
            raise ValueError(
                f"Framework '{response.name}' has no runnable risk categories. Add "
                "vulnerability types to at least one of its risk categories on Confident AI."
            )

        vulnerabilities = []
        attacks = []
        for risk_category in risk_categories:
            vulnerabilities.extend(risk_category.vulnerabilities)
            attacks.extend(risk_category.attacks or [])

        self.name = response.name
        self.description = response.description or ""
        self.vulnerabilities = vulnerabilities
        self.attacks = attacks
        self.risk_categories = risk_categories
        self._id = response.id
