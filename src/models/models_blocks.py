from pydantic import BaseModel
from typing import Literal, Union
from src.enums import ObjectType
from src.models.models_page import ChildrenParagraph


class BaseBlock:
    object: Literal["block"]
    type: ObjectType


class HeadingBlock(BaseModel, BaseBlock):
    heading_2: ChildrenParagraph


class ItemListBlock(BaseModel, BaseBlock):
    bulleted_list_item: ChildrenParagraph


class RequestBodyBlock(BaseModel):
    children: list[Union[HeadingBlock, ItemListBlock]]
