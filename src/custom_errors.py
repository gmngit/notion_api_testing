class BaseMsg:
    """
    Basic class for AssertionError logs.
    """

    def __init__(self, response):
        self._msg = ""
        self._response = response

    def add_request_info(self):
        self._msg += f"\tURL: {self._response.request.url}\n"
        self._msg += f"\tmethod: {self._response.request.method}\n"
        if hasattr(self._response.request, 'content') and self._response.request.read():
            self._msg += f"\trequest body: {self._response.request.read()}\n"
        else:
            self._msg += f"\trequest body: None\n"
        return self

    def add_response_info(self):
        self._msg += f"Response body :\n\t{self._response.json()}\n"
        return self

    def get_message(self):
        return self._msg


class CodeLogMsg(BaseMsg):
    def add_compare_result(self, act, exp):
        self._msg += f"\n\tactual status code: {act}\n\texpected status code: {exp}\n"
        return self
