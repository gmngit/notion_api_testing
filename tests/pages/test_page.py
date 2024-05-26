import logging
import allure

from http import HTTPStatus
from src.assertions import ResponseAssertion
from src.models import models_response
from src.objects import Block

logger = logging.getLogger("logger_tests")


class TestPage:
    def test_create_page(self, client, create_page):
        with allure.step("Check status code"):
            ResponseAssertion.assert_status_code(create_page, HTTPStatus.OK)
        with allure.step("Check response body"):
            ResponseAssertion.assert_response_body(create_page, models_response.CreatedPage)

    def test_get_page(self, client, page_id):
        with allure.step("Get response"):
            response = client.get_page(page_id)
        with allure.step("Check status code"):
            ResponseAssertion.assert_status_code(response, HTTPStatus.OK)
        with allure.step("Check response body"):
            ResponseAssertion.assert_response_body(response, models_response.CreatedPage)
        with allure.step("Check the page was found"):
            assert response.json()['id'] == page_id

    def test_append_block(self, client, page_id, create_block, blocks_id):
        with allure.step("Check status code"):
            ResponseAssertion.assert_status_code(create_block, HTTPStatus.OK)
        with allure.step("Check response body"):
            ResponseAssertion.assert_response_body(create_block, models_response.ListOfBlocks)

        with allure.step("Check the block was appended"):
            response = client.get_list_blocks(page_id)
            actual_blocks = blocks_id
            expected_blocks = Block.get_id(list_blocks=response.json()['results'])

            for key in actual_blocks.keys():
                if key not in expected_blocks.keys():
                    logger.error("No expected blocks in the list")
                    assert False
                else:
                    assert True

    def test_get_block(self, client, blocks_id):
        with allure.step("Get a block ID"):
            block_id = blocks_id['heading_2']
        with allure.step("Get response"):
            response = client.get_block(block_id)
        with allure.step("Check status code"):
            ResponseAssertion.assert_status_code(response, HTTPStatus.OK)
        with allure.step("Check response body"):
            ResponseAssertion.assert_response_body(response, models_response.CreatedBlock)
        with allure.step("Check the block was found"):
            assert response.json()['id'] == block_id

    def test_delete_block(self, client, blocks_id):
        with allure.step("Get a block ID"):
            block_id = blocks_id['heading_2']
        with allure.step("Get response"):
            response = client.delete_block(block_id)
        with allure.step("Check status code"):
            ResponseAssertion.assert_status_code(response, HTTPStatus.OK)
        with allure.step("Check response body"):
            ResponseAssertion.assert_response_body(response, models_response.CreatedBlock)
        with allure.step("Check the block was deleted"):
            assert response.json()['archived'] is True
            assert response.json()['in_trash'] is True

    def test_update_page(self, client, page_id):
        request_body = {
            'in_trash': True
        }
        with allure.step("Get response"):
            response = client.update_page(page_id, request_body)
        with allure.step("Check status code"):
            ResponseAssertion.assert_status_code(response, HTTPStatus.OK)
        with allure.step("Check response body"):
            ResponseAssertion.assert_response_body(response, models_response.CreatedPage)
        with allure.step("Check the page was updated"):
            response = client.get_page(page_id)
            assert response.json()['in_trash'] == request_body['in_trash']

    def test_get_page_invalid_id(self, client):
        page_id = "abd75eea8a94e2e8cfff644a261ab2d"
        with allure.step("Get response"):
            response = client.get_page(page_id)
        with allure.step("Check status code"):
            ResponseAssertion.assert_status_code(response, HTTPStatus.BAD_REQUEST)
        with allure.step("Check response body"):
            ResponseAssertion.assert_response_body(response, models_response.BadRequest)

    def test_delete_block_not_exist(self, client):
        block_id = "ec13a87b-7f0d-428b-9bf0-b80004d5b93c"
        with allure.step("Get response"):
            response = client.delete_block(block_id)
        with allure.step("Check status code"):
            ResponseAssertion.assert_status_code(response, HTTPStatus.BAD_REQUEST)
        with allure.step("Check response body"):
            ResponseAssertion.assert_response_body(response, models_response.BadRequest)
