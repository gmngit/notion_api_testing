from api.api_client import APIClient


class NotionRequests(APIClient):
    USERS = f"/v1/users"
    PAGES = f"/v1/pages"
    BLOCKS = f"/v1/blocks"
    SEARCH = f"/v1/search"

    def get_all_users(self, params=None):
        return self.get_obj(
            endpoint=self.USERS,
            headers=self.session.headers,
            params=params
        )

    def get_user_by_id(self, user_id, params=None):
        return self.get_obj(
            endpoint=f"{self.USERS}/{user_id}",
            headers=self.session.headers,
            params=params
        )

    def create_page(self, request_body):
        return self.post_obj(
            endpoint=self.PAGES,
            headers=self.session.headers,
            json=request_body
        )

    def search_pages(self, request_body=None):
        return self.post_obj(
            endpoint=self.SEARCH,
            headers=self.session.headers,
            json=request_body
        )

    def get_page(self, page_id, params=None):
        return self.get_obj(
            endpoint=f"{self.PAGES}/{page_id}",
            headers=self.session.headers,
            params=params
        )

    def update_page(self, page_id, request_body):
        return self.patch_obj(
            endpoint=f"{self.PAGES}/{page_id}",
            headers=self.session.headers,
            json=request_body
        )

    def append_block(self, block_id, request_body):
        return self.patch_obj(
            endpoint=f"{self.BLOCKS}/{block_id}/children",
            headers=self.session.headers,
            json=request_body
        )

    def get_list_blocks(self, page_id, params=None):
        return self.get_obj(
            endpoint=f"{self.BLOCKS}/{page_id}/children",
            headers=self.session.headers,
            params=params
        )

    def get_block(self, block_id, params=None):
        return self.get_obj(
            endpoint=f"{self.BLOCKS}/{block_id}",
            headers=self.session.headers,
            params=params
        )

    def delete_block(self, block_id):
        return self.delete_obj(
            endpoint=f"{self.BLOCKS}/{block_id}",
            headers=self.session.headers
        )
