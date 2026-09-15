from src.config import load_dialogflow_cx_config


def build_session_path(config) -> str:
    """Build a Dialogflow CX session path from local configuration."""

    return (
        f"projects/{config.project_id}/locations/{config.location}/"
        f"agents/{config.agent_id}/sessions/{config.session_id}"
    )


def main() -> None:
    config = load_dialogflow_cx_config()
    session_path = build_session_path(config)

    print("Dialogflow CX configuration loaded successfully.")
    print(f"Project ID: {config.project_id}")
    print(f"Location: {config.location}")
    print(f"Agent ID: {config.agent_id}")
    print(f"Language code: {config.language_code}")
    print(f"Session path: {session_path}")
    print("Credentials path loaded from environment variable.")


if __name__ == "__main__":
    main()