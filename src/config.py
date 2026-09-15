import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass
class DialogflowCXConfig:
    project_id: str
    credentials_path: str
    location: str
    agent_id: str
    language_code: str
    session_id: str


def load_dialogflow_cx_config() -> DialogflowCXConfig:
    """Load Dialogflow CX configuration from environment variables."""

    load_dotenv()

    required_variables = [
        "GOOGLE_CLOUD_PROJECT_ID",
        "GOOGLE_APPLICATION_CREDENTIALS",
        "DIALOGFLOW_CX_LOCATION",
        "DIALOGFLOW_CX_AGENT_ID",
        "DIALOGFLOW_CX_LANGUAGE_CODE",
        "DIALOGFLOW_CX_SESSION_ID",
    ]

    missing = [var for var in required_variables if not os.getenv(var)]

    if missing:
        raise EnvironmentError(
            "Missing required environment variables: "
            + ", ".join(missing)
            + ". Copy .env.example to .env and fill in local values."
        )

    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "")

    if not Path(credentials_path).exists():
        raise FileNotFoundError(
            f"Credentials file not found: {credentials_path}. "
            "Make sure the path points to a local service account key file."
        )

    return DialogflowCXConfig(
        project_id=os.environ["GOOGLE_CLOUD_PROJECT_ID"],
        credentials_path=credentials_path,
        location=os.environ["DIALOGFLOW_CX_LOCATION"],
        agent_id=os.environ["DIALOGFLOW_CX_AGENT_ID"],
        language_code=os.environ["DIALOGFLOW_CX_LANGUAGE_CODE"],
        session_id=os.environ["DIALOGFLOW_CX_SESSION_ID"],
    )