import logging
import pytest
import allure

from src.objects import Page, Block
from src.models.models_page import RequestBodyPage
from src.models.models_blocks import RequestBodyBlock

logger = logging.getLogger("logger_pages_fixtures")


@pytest.fixture(scope='class')
@allure.title("Prepare a request body for page")
def request_body_page():
    page_id = "01714444-3760-495f-af0a-fb1bcfc0f640"
    cover_url = "https://images.unsplash.com/photo-1648437595587-e6a8b0cdf1f9?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb"
    parent = {
        'type': "page_id",
        'page_id': page_id
    }
    cover = {
        'type': "external",
        'external': {'url': cover_url}
    }
    properties = {
        'title': {
            'id': "",
            'type': "title",
            'title': [
                {
                    'type': "text",
                    'text': {
                        'content': "Carnitas"
                    },
                    'annotations': {},
                    'plain_text': "",
                    'href': ""
                }
            ]
        }
    }
    children = [
        {
            'object': "block",
            'type': "paragraph",
            'paragraph': {
                'rich_text': [
                    {
                        'type': "text",
                        'text': {'content': "Carnitas are originally from Michoacán, Mexico. Pork shoulder or butt is "
                                            "cut into smaller bite-sized pieces, hence the charming name: “little "
                                            "meats.” It’s then cooked submerged in hot lard, a confit-like cooking "
                                            "process that yields pork that is deliciously tender on the inside and "
                                            "beautifully crisp on the outside. Carnitas are usually served with warm "
                                            "corn tortillas to make one of the most iconic and classic tacos in "
                                            "Mexico. You get the succulent taste of pure pork—salty, crispy, "
                                            "and perfect in every way."}
                    }
                ]
            }
        }
    ]

    model = RequestBodyPage(
        parent=parent,
        cover=cover,
        properties=properties,
        children=children
    )

    return Page.convert_model_to_json(model)


@pytest.fixture(scope='class')
@allure.title("Creating a page...")
def create_page(client, request_body_page):
    response = client.create_page(request_body_page)
    return response


@pytest.fixture(scope='class')
@allure.title("Prepare a page ID")
def page_id(create_page):
    return create_page.json()['id']


@pytest.fixture(scope='class')
@allure.title("Prepare a request body for blocks")
def request_body_block():
    children = [
        {
            'object': "block",
            'type': "heading_2",
            'heading_2': {
                'rich_text': [
                    {
                        'type': "text",
                        'text': {'content': "How to make Pork Carnitas"}
                    }
                ]
            }
        },
        {
            'object': "block",
            'type': "bulleted_list_item",
            'bulleted_list_item': {
                'rich_text': [
                    {
                        'type': "text",
                        'text': {'content': "Flavour for cooking – top pork in slow cooker with onion, garlic and "
                                            "jalapeño, then pour over orange juice (the secret ingredient!). It "
                                            "sounds so simple, but with hours of slow cooking, mingling with the pork "
                                            "juices, it transforms into the most incredible braising broth that more "
                                            "than makes up for the absence of gallons of lard."}
                    }
                ]
            }
        }
    ]

    model = RequestBodyBlock(children=children)

    return Page.convert_model_to_json(model)


@pytest.fixture(scope='class')
@allure.title("Creating a block...")
def create_block(client, page_id, request_body_block):
    response = client.append_block(page_id, request_body_block)
    return response


@pytest.fixture(scope='class')
@allure.title("Prepare a block ID")
def blocks_id(create_block):
    response = create_block
    list_blocks = response.json()['results']
    return Block.get_id(list_blocks=list_blocks)
