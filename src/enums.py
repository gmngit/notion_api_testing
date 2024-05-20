from enum import Enum


class UserType(str, Enum):
    PERSON = "person"
    BOT = "bot"


class ObjectType(Enum):
    BOOKMARK = "bookmark"
    BREADCRUMB = "breadcrumb"
    CHILD_PAGE = "child_page"
    HEADING_1 = "heading_1"
    HEADING_2 = "heading_2"
    HEADING_3 = "heading_3"
    PARAGRAPH = "paragraph"
    QUOTE = "quote"
    LIST_ITEM = "bulleted_list_item"


class RichTextType(Enum):
    text = "text"
    mention = "mention"
    equation = "equation"
