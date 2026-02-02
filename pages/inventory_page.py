from selenium.webdriver.common.by import By 
from pages.base_page import BasePage 
 
class InventoryPage(BasePage): 
    TITLE = (By.CLASS_NAME, "title") 
 
    def is_loaded(self): 
        return self.is_visible(self.TITLE)