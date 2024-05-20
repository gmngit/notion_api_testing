from pydantic import BaseModel, UUID4, HttpUrl
from typing import Literal, Optional
from src.enums import ObjectType, RichTextType


class Parent(BaseModel):
    type: Literal["page_id"]
    page_id: UUID4


class CoverExternal(BaseModel):
    url: HttpUrl


class Cover(BaseModel):
    type: str
    external: CoverExternal


class PropertiesTitleAnnotations(BaseModel):
    bold: bool
    italic: bool
    strikethrough: bool
    underline: bool
    code: bool
    color: str


class PropertiesTitleText(BaseModel):
    content: str
    link: Optional[str] = None


class PropertiesTitle(BaseModel):
    type: Literal["text"]
    text: PropertiesTitleText
    annotations: dict
    plain_text: str
    href: Optional[str] = None


class Title(BaseModel):
    id: str
    type: str
    title: list[PropertiesTitle]


class Properties(BaseModel):
    title: Title


class ChildrenParagraphRichText(BaseModel):
    type: RichTextType
    text: PropertiesTitleText


class ChildrenParagraph(BaseModel):
    rich_text: list[ChildrenParagraphRichText]


class Children(BaseModel):
    object: Literal["block"]
    type: ObjectType
    paragraph: ChildrenParagraph


class RequestBodyPage(BaseModel):
    parent: Parent
    cover: Cover
    properties: Properties
    children: list[Children]


class Icon(BaseModel):
    type: Literal["external"]
    external: CoverExternal


class CreatedOrEditedBy(BaseModel):
    object: Literal["user"]
    id: UUID4
