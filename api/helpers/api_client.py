import requests
from utils.config_reader import ConfigReader


class APIClient:
    def __init__(self):
        self.base_url_1 = ConfigReader.get("api", "base_url_1")
        self.session = requests.Session()
        self.token = None

    # -------------------------
    # Authentication Handling
    # -------------------------

    def set_token(self, token: str):
        """
        Set Bearer token for future requests.
        """
        self.token = token

    def clear_token(self):
        """
        Remove token from session.
        """
        self.token = None

    def _build_headers(self, extra_headers=None):
        """
        Construct request headers including Authorization if token exists.
        """
        headers = {
            "Content-Type": "application/json"
        }

        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        if extra_headers:
            headers.update(extra_headers)

        return headers

    # -------------------------
    # HTTP Methods
    # -------------------------

    def get(self, endpoint, params=None, headers=None):
        return self.session.get(
            f"{self.base_url_1}{endpoint}",
            params=params,
            headers=self._build_headers(headers)
        )

    def post(self, endpoint, payload=None, headers=None):
        return self.session.post(
            f"{self.base_url_1}{endpoint}",
            json=payload,
            headers=self._build_headers(headers)
        )

    def put(self, endpoint, payload=None, headers=None):
        return self.session.put(
            f"{self.base_url_1}{endpoint}",
            json=payload,
            headers=self._build_headers(headers)
        )

    def delete(self, endpoint, headers=None):
        return self.session.delete(
            f"{self.base_url_1}{endpoint}",
            headers=self._build_headers(headers)
        )
