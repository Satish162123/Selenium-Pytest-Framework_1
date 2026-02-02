from selenium.webdriver.common.by import By 
from pages.base_page import BasePage 
from utils.config_reader import ConfigReader 
 
class LoginPage(BasePage): 
    USERNAME = (By.ID, "user-name") 
    PASSWORD = (By.ID, "password") 
    LOGIN_BTN = (By.ID, "login-button") 
    ERROR = (By.CSS_SELECTOR, "h3[data-test='error']") 
 
    def load(self): 
        self.open(ConfigReader.get("app", "base_url")) 
 
    def login(self, username, password): 
        self.type(self.USERNAME, username) 
        self.type(self.PASSWORD, password) 
        self.click(self.LOGIN_BTN) 
 
    def get_error(self): 
        return self.get_text(self.ERROR)