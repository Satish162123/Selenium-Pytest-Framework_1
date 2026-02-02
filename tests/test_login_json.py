import pytest 
import json 
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
 
def read_json(): 
    with open("test_data/login_data.json") as file: 
        return json.load(file) 
 
@pytest.mark.regression 
@pytest.mark.parametrize("data", read_json()) 
def test_login_json(driver, data): 
    login = LoginPage(driver) 
    inventory = InventoryPage(driver) 
 
    login.load() 
    login.login(data["username"], data["password"]) 
 
    if data["expected"] == "success": 
        assert inventory.is_loaded() 
    else: 
        assert "username and password do not match" in login.get_error().lower()