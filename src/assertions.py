import logging

from pydantic import TypeAdapter
from src.custom_errors import CodeLogMsg

logger = logging.getLogger("logger_assertions")


class ResponseAssertion:
    @staticmethod
    def assert_status_code(response, expected_code):
        assert response.status_code == expected_code, CodeLogMsg(response) \
            .add_compare_result(response.status_code, expected_code) \
            .add_request_info() \
            .add_response_info() \
            .get_message()

    @staticmethod
    def assert_response_body(response, schema):
        if isinstance(response, list):
            TypeAdapter(list[schema]).validate_python(response)
        else:
            schema.model_validate(response.json())
