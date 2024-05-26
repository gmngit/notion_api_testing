import allure

from http import HTTPStatus
from src.assertions import ResponseAssertion
from src.models import models_response


class TestUser:
    def test_get_user(self, client, user_id, user_name):
        with allure.step("Get response"):
            response = client.get_user_by_id(user_id)
        with allure.step("Check status code"):
            ResponseAssertion.assert_status_code(response, HTTPStatus.OK)
        with allure.step("Check response body"):
            ResponseAssertion.assert_response_body(response, models_response.UserModel)
        with allure.step("Check the user was found"):
            assert response.json()['id'] == user_id

    def test_get_user_not_exist(self, client):
        user_id = "1a8da1e5-bd1c-450a-b335-a963354f9a3d"
        with allure.step("Get response"):
            response = client.get_user_by_id(user_id)
        with allure.step("Check status code"):
            ResponseAssertion.assert_status_code(response, HTTPStatus.NOT_FOUND)
        with allure.step("Check response body"):
            ResponseAssertion.assert_response_body(response, models_response.NotFound)
