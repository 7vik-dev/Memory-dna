import os
import warnings
import re

# Optionally add telemetry
from memory_dna.red_team import red_team

# Import guardrails for production LLM safety
from memory_dna.guardrails import (
    Guardrails,
)
from memory_dna._version import __version__

__all__ = [
    "red_team",
    "Guardrails",
    "__version__",
]


def compare_versions(version1, version2):
    def normalize(v):
        return [int(x) for x in re.sub(r"(\.0+)*$", "", v).split(".")]

    return normalize(version1) > normalize(version2)


def check_for_update():
    return
    try:
        import requests

        try:
            response = requests.get(
                "https://pypi.org/pypi/memory_dna/json", timeout=5
            )
            latest_version = response.json()["info"]["version"]

            if compare_versions(latest_version, __version__):
                warnings.warn(
                    f'You are using memory_dna version {__version__}, however version {latest_version} is available. You should consider upgrading via the "pip install --upgrade memory_dna" command.'
                )
        except (
            requests.exceptions.RequestException,
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
            requests.exceptions.SSLError,
            requests.exceptions.Timeout,
        ):
            # when pypi servers go down
            pass
    except ModuleNotFoundError:
        # they're just getting the versione
        pass


def update_warning_opt_out():
    return os.getenv("DEEPEVAL_UPDATE_WARNING_OPT_OUT") == "YES"


if not update_warning_opt_out():
    check_for_update()
