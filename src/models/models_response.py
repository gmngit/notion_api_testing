import uuid

from typing import Optional, Literal
from pydantic import BaseModel, UUID4, field_validator
from datetime import datetime
from src.enums import UserType, ObjectType
from src.models.models_page import CreatedOrEditedBy, Cover, Icon, Parent, Properties


class UserModel(BaseModel):
    object: Literal["user"]
    id: str
    name: str
    avatar_url: Optional[str] = None
    type: UserType
    person: dict[str, str]
    developer_survey: Optional[str] = None
    request_id: Optional[str] = None

    @field_validator('id')
    @classmethod
    def is_valid_uuid(cls, v: str):
        try:
            uuid.UUID(v)
            return True
        except ValueError:
            raise ValueError(f"The id: {v} is not a valid UUID")


class BaseErrors:
    object: Literal["error"]
    code: str
    message: str
    developer_survey: Optional[str] = None
    request_id: Optional[str] = None


class NotFound(BaseModel, BaseErrors):
    status: Literal[404]


class BadRequest(BaseModel, BaseErrors):
    status: Literal[400]


class BaseObject:
    id: UUID4
    created_time: datetime
    last_edited_time: datetime
    created_by: CreatedOrEditedBy
    last_edited_by: CreatedOrEditedBy
    archived: bool
    in_trash: bool
    developer_survey: Optional[str] = None
    request_id: Optional[str] = None


class CreatedPage(BaseModel, BaseObject):
    object: Literal["page"]
    cover: Cover
    icon: Optional[Icon] = None
    parent: Parent
    properties: Properties
    url: Optional[str] = None
    public_url: Optional[str] = None


class CreatedBlock(BaseModel, BaseObject):
    object: Literal["block"]
    parent: Parent
    has_children: bool
    type: ObjectType
    ObjectType: Optional[dict] = None


class ListOfBlocks(BaseModel):
    object: Literal["list"]
    results: list
    next_cursor: Optional[str] = None
    has_more: bool
    type: str
    block: Optional[dict]
    developer_survey: Optional[str] = None
    request_id: Optional[str] = None
