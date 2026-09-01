from typing import Union

from memory_dna.metrics.intellectual_property.template import (
    IntellectualPropertyTemplate,
)
from memory_dna.vulnerabilities.bias.template import BiasTemplate
from memory_dna.vulnerabilities.competition.template import CompetitionTemplate
from memory_dna.vulnerabilities.graphic_content.template import (
    GraphicContentTemplate,
)
from memory_dna.vulnerabilities.illegal_activity.template import (
    IllegalActivityTemplate,
)
from memory_dna.vulnerabilities.intellectual_property import (
    IntellectualPropertyType,
)
from memory_dna.vulnerabilities.misinformation.template import (
    MisinformationTemplate,
)
from memory_dna.vulnerabilities.personal_safety.template import (
    PersonalSafetyTemplate,
)
from memory_dna.vulnerabilities.pii_leakage.template import PIILeakageTemplate
from memory_dna.vulnerabilities.prompt_leakage.template import (
    PromptLeakageTemplate,
)
from memory_dna.vulnerabilities.toxicity.template import ToxicityTemplate
from memory_dna.vulnerabilities.illegal_activity import IllegalActivityType
from memory_dna.vulnerabilities.personal_safety import PersonalSafetyType
from memory_dna.vulnerabilities.graphic_content import GraphicContentType
from memory_dna.vulnerabilities.misinformation import MisinformationType
from memory_dna.vulnerabilities.prompt_leakage import PromptLeakageType
from memory_dna.vulnerabilities.competition import CompetitionType
from memory_dna.vulnerabilities.pii_leakage import PIILeakageType
from memory_dna.vulnerabilities.toxicity import ToxicityType
from memory_dna.vulnerabilities.bias import BiasType
from memory_dna.vulnerabilities.rbac import RBACType
from memory_dna.vulnerabilities.bola.types import BOLAType
from memory_dna.vulnerabilities.bfla.types import BFLAType
from memory_dna.vulnerabilities.ssrf.types import SSRFType
from memory_dna.vulnerabilities.debug_access.types import DebugAccessType
from memory_dna.vulnerabilities.shell_injection.types import ShellInjectionType
from memory_dna.vulnerabilities.sql_injection.types import SQLInjectionType
from memory_dna.vulnerabilities.rbac.template import RBACTemplate
from memory_dna.vulnerabilities.bola.template import BOLATemplate
from memory_dna.vulnerabilities.bfla.template import BFLATemplate
from memory_dna.vulnerabilities.ssrf.template import SSRFTemplate
from memory_dna.vulnerabilities.debug_access.template import DebugAccessTemplate
from memory_dna.vulnerabilities.shell_injection.template import (
    ShellInjectionTemplate,
)
from memory_dna.vulnerabilities.sql_injection.template import SQLInjectionTemplate
from memory_dna.vulnerabilities.robustness import RobustnessType
from memory_dna.vulnerabilities.robustness.template import (
    RobustnessTemplate,
)
from memory_dna.vulnerabilities.excessive_agency import (
    ExcessiveAgencyType,
)
from memory_dna.vulnerabilities.excessive_agency.template import (
    ExcessiveAgencyTemplate,
)
from memory_dna.vulnerabilities.exploit_tool_agent.types import (
    ExploitToolAgentType,
)
from memory_dna.vulnerabilities.exploit_tool_agent.template import (
    ExploitToolAgentTemplate,
)
from memory_dna.vulnerabilities.external_system_abuse.types import (
    ExternalSystemAbuseType,
)
from memory_dna.vulnerabilities.external_system_abuse.template import (
    ExternalSystemAbuseTemplate,
)
from memory_dna.vulnerabilities.cross_context_retrieval.types import (
    CrossContextRetrievalType,
)
from memory_dna.vulnerabilities.cross_context_retrieval.template import (
    CrossContextRetrievalTemplate,
)
from memory_dna.vulnerabilities.system_reconnaissance.types import (
    SystemReconnaissanceType,
)
from memory_dna.vulnerabilities.system_reconnaissance.template import (
    SystemReconnaissanceTemplate,
)

# Import agentic vulnerability types
from memory_dna.vulnerabilities.goal_theft.types import GoalTheftType
from memory_dna.vulnerabilities.recursive_hijacking.types import (
    RecursiveHijackingType,
)
from memory_dna.vulnerabilities.goal_theft.template import (
    GoalTheftTemplate,
)
from memory_dna.vulnerabilities.recursive_hijacking.template import (
    RecursiveHijackingTemplate,
)

VulnerabilityType = Union[
    IllegalActivityType,
    PersonalSafetyType,
    GraphicContentType,
    MisinformationType,
    PromptLeakageType,
    PromptLeakageType,
    CompetitionType,
    PIILeakageType,
    ToxicityType,
    BiasType,
    IntellectualPropertyType,
    IntellectualPropertyType,
    IntellectualPropertyType,
    RBACType,
    BOLAType,
    BFLAType,
    SSRFType,
    DebugAccessType,
    ShellInjectionType,
    SQLInjectionType,
    ExploitToolAgentType,
    ExternalSystemAbuseType,
    CrossContextRetrievalType,
    SystemReconnaissanceType,
    # Restored vulnerability types
    RobustnessType,
    ExcessiveAgencyType,
    # Agentic vulnerability types
    GoalTheftType,
    RecursiveHijackingType,
]

TemplateType = Union[
    BiasTemplate,
    CompetitionTemplate,
    GraphicContentTemplate,
    IllegalActivityTemplate,
    IntellectualPropertyTemplate,
    MisinformationTemplate,
    PersonalSafetyTemplate,
    PIILeakageTemplate,
    PromptLeakageTemplate,
    ToxicityTemplate,
    RBACTemplate,
    BOLATemplate,
    BFLATemplate,
    SSRFTemplate,
    DebugAccessTemplate,
    ShellInjectionTemplate,
    SQLInjectionTemplate,
    RobustnessTemplate,
    ExcessiveAgencyTemplate,
    GoalTheftTemplate,
    RecursiveHijackingTemplate,
    ExploitToolAgentTemplate,
    ExternalSystemAbuseTemplate,
    CrossContextRetrievalTemplate,
    SystemReconnaissanceTemplate,
]
