"""Application settings."""

import os

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """Application settings class."""

    base_host: str = 'https://www.linkedin.com/'
    search_url: str = 'https://www.linkedin.com/search/results/people/?geoUrn=%5B%22104508036%22%2C%22106156085%22%2C%2290010322%22%5D&keywords=recruiter&origin=FACETED_SEARCH&profileLanguage=%5B%22en%22%2C%22ru%22%5D&titleFreeText=recruiter'  # noqa: WPS323, E501

    limit_invites: int = 30  # 30 per week for fresh accounts
    limit_failures: int = 3
    limit_pages: int = 20

    start_page: int = 1
    timeout_default: int = 10
    throttling_seconds: int = 5

    session_path: str = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            '.inviter_session',
        ),
    )


app_settings = AppSettings(
    _env_file=os.path.join(os.path.dirname(__file__), '..', '.env'),  # type: ignore
)
