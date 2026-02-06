import requests 
from utils.config_reader import ConfigReader 
 
class ApiClient:
    def __init__(self): 
        self.base_url_1 = ConfigReader.get("api", "base_url_1") 
 
    def get(self, endpoint): 
        return requests.get(f"{self.base_url_1}{endpoint}") 
 
    def post(self, endpoint, payload): 
        return requests.post( 
            f"{self.base_url_1}{endpoint}", 
            json=payload 
        ) 
 
    def put(self, endpoint, payload): 
        return requests.put( 
            f"{self.base_url_1}{endpoint}", 
            json=payload 
        ) 