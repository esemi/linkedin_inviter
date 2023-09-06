"""Inviter cron task."""

import logging

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from app.selenium_actions import click, create_browser, highlight, press_escape, save_screenshot
from app.settings import app_settings
from app.status import InviteStatus

logger = logging.getLogger(__file__)


def main() -> bool:
    """Open linkedin, make people search and press "connect" button few times."""
    browser_with_auth = _open_ll()
    logger.info('browser open result {0}'.format(browser_with_auth))
    if not browser_with_auth:
        logger.warning('auth check failure')
        return False

    invites_sent = _process_invites(browser_with_auth)
    logger.info('end and processed {0} invites'.format(invites_sent))

    return invites_sent >= app_settings.limit_invites


def _process_invites(browser: WebDriver) -> int:
    page: int = app_settings.start_page
    failures: int = 0
    invites_sent: int = 0
    go_next: bool = True

    while go_next:
        potential_relations = _get_connections(browser, page=page)
        logger.info('found {0} connect buttons on page {1}'.format(len(potential_relations), page))

        for connection in potential_relations[:app_settings.limit_invites - invites_sent]:
            logger.info('process connect {0}'.format(connection.accessible_name))
            response = _process_connect(browser, connection)
            if response is InviteStatus.success:
                invites_sent += 1

            if response is InviteStatus.failure:
                failures += 1
                break

        go_next = all([
            page < app_settings.limit_pages,
            failures < app_settings.limit_failures,
            invites_sent < app_settings.limit_invites,
        ])

        logger.info('go to next page')
        page += 1

    return invites_sent


def _open_ll() -> WebDriver | None:
    browser = create_browser()

    browser.get(app_settings.base_host)
    try:
        browser.find_element(By.XPATH, '//a[contains(@class,"ember-view")]')
        return browser
    except NoSuchElementException:
        save_screenshot(browser)
        logger.debug('auth failure')

    browser.quit()
    return None


def _get_connections(browser: WebDriver, page: int) -> list[WebElement]:
    url = '&'.join([app_settings.search_url, f'page={page}'])
    browser.get(url)

    return browser.find_elements(
        By.XPATH,
        '//div[@class="entity-result"]//li-icon[@type="connect"]/parent::button',
    )


def _process_connect(browser: WebDriver, button_element: WebElement) -> InviteStatus:
    highlight(browser, button_element)
    click(browser, button_element)

    try:
        send_button = browser.find_element(
            By.XPATH,
            '//button[@aria-label="Send now"]',
        )
    except NoSuchElementException:
        logger.warning('send button not found')
        save_screenshot(browser)
        return InviteStatus.failure

    click(browser, send_button)

    try:
        browser.find_element(
            By.XPATH,
            '//h2[@id="ip-fuse-limit-alert__header"]',
        )
    except NoSuchElementException:
        return InviteStatus.success

    logger.warning('limit popup fired!')
    save_screenshot(browser)
    press_escape(browser)
    return InviteStatus.failure


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )
    main()
