import pytest 
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage 
from utils.config_reader import ConfigReader 
 
@pytest.mark.smoke 
@pytest.mark.regression 
def test_valid_login(driver): 
    login = LoginPage(driver) 
    inventory = InventoryPage(driver) 
 
    login.load() 
    login.login( 
        ConfigReader.get("credentials", "valid_username"), 
        ConfigReader.get("credentials", "valid_password") 
    ) 
 
    assert inventory.is_loaded() 
 
@pytest.mark.regression 
def test_invalid_login(driver): 
    login = LoginPage(driver) 
 
    login.load() 
    login.login( 
        ConfigReader.get("credentials", "invalid_username"), 
        ConfigReader.get("credentials", "invalid_password") 
    ) 
 
    assert "username and password do not match" in login.get_error().lower()