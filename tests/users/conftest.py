import pytest
import allure

from src.objects import User


@pytest.fixture(scope='class')
@allure.title("Prepare a name for user")
def user_name():
    name = "Mairo"
    return name


@pytest.fixture(scope='class')
@allure.title("Prepare an UID")
def user_id(client, user_name):
    response = client.get_all_users()
    list_users = response.json()['results']
    return User.get_id(list_users=list_users, name=user_name)
