import os
import logging
import pytest
import allure

from api.api_requests import NotionRequests

logger = logging.getLogger("logger_fixtures")


def pytest_configure():
    logging.basicConfig(level=logging.DEBUG)


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://api.notion.com",
        help="Base url for requests"
    )


@pytest.fixture(scope='class')
@allure.title("Prepare a bearer token")
def bearer_token():
    return os.getenv('TOKEN')


@pytest.fixture(scope='class')
@allure.title("Prepare HTTP client for requests")
def client(bearer_token, request):
    base_url = request.config.getoption("--url")

    client = NotionRequests(
        base_url=f"{base_url}",
        token=bearer_token
    )
    client.set_session_authentication()
    client.add_header("Notion-Version", "2022-06-28")
    yield client
    with allure.step("Close session"):
        logger.info(f"\nSession was closed")
        client.session.close()
