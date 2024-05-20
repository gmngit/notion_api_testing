import logging

from pydantic import BaseModel

logger = logging.getLogger("logger_objects")


class User:
    @staticmethod
    def get_id(list_users, name):
        if list_users:
            for item in list_users:
                if item.get("name") == name:
                    uid = item.get('id')
                    logger.debug(f"\nThe user {name} has id: {uid}")
                    return uid
            logger.debug(f"\nThe user with name '{name}' doesn't exist")
        else:
            logger.error("\nNo users found")


class Page:
    @staticmethod
    def convert_model_to_json(model: BaseModel):
        if not isinstance(model, BaseModel):
            raise ValueError("Model must be an instance of pydantic.BaseModel")

        json_body = model.model_dump(mode='json')
        return json_body

    @staticmethod
    def find_content(data):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == 'content':
                    return value
                else:
                    result = Page.find_content(value)
                    if result is not None:
                        return result
        elif isinstance(data, list):
            for item in data:
                result = Page.find_content(item)
                if result is not None:
                    return result


class Block:
    @staticmethod
    def get_id(list_blocks):
        if list_blocks:
            res = {}
            for block in list_blocks:
                res[block['type']] = block['id']

            logger.debug(f"\nThe ids of blocks: {res}")
            return res
        else:
            logger.error("\nNo blocks found")
