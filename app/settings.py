"""Application settings."""

import os

from pydantic_settings import BaseSettings

APP_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
    ),
)


class AppSettings(BaseSettings):
    """Application settings class."""

    base_host: str = 'https://www.linkedin.com/'
    search_url: str = 'https://www.linkedin.com/search/results/people/?geoUrn=%5B%2290010322%22%2C%22103973174%22%2C%22106156085%22%2C%22104508036%22%5D&keywords=recruiter&origin=FACETED_SEARCH&profileLanguage=%5B%22en%22%2C%22ru%22%5D&sid=a6%40&titleFreeText=recruiter'  # noqa: WPS323, E501

    limit_invites: int = 10  # 30 per week for fresh accounts
    limit_failures: int = 2
    limit_pages: int = 20

    start_page: int = 1
    timeout_default: int = 10
    throttling_seconds: int = 5

    headless: bool = True
    session_path: str = os.path.join(APP_PATH, '.inviter_session')
    screenshots_path: str = os.path.join(APP_PATH, 'screenshots')

    chrome_path: str = os.path.join(APP_PATH, 'bin', 'chrome-linux64', 'chrome')
    chrome_driver_path: str = os.path.join(APP_PATH, 'bin', 'chromedriver-linux64', 'chromedriver')


app_settings = AppSettings(
    _env_file=os.path.join(APP_PATH, '.env'),  # type: ignore
)
