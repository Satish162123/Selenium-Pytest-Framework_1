import pytest 
import csv 
from pages.login_page import LoginPage 
from pages.inventory_page import InventoryPage 
 
def read_csv(): 
    with open("test_data/login_data.csv") as file: 
        reader = csv.DictReader(file) 
        return [(r["username"], r["password"], r["expected"]) for r in reader] 
 
@pytest.mark.regression 
@pytest.mark.parametrize("username,password,expected", read_csv()) 
def test_login_csv(driver, username, password, expected): 
    login = LoginPage(driver) 
    inventory = InventoryPage(driver) 
 
    login.load() 
    login.login(username, password) 
 
    if expected == "success": 
        assert inventory.is_loaded() 
    else: 
        assert "username and password do not match" in login.get_error().lower()