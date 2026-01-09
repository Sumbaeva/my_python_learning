from selenium.webdriver.common.by import By
from .base_page import BasePage


class InventoryPage(BasePage):
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BOLT_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self):
        self.click(self.ADD_BACKPACK)

    def add_bolt_tshirt(self):
        self.click(self.ADD_BOLT_TSHIRT)

    def add_onesie(self):
        self.click(self.ADD_ONESIE)

    def go_to_cart(self):
        self.click(self.CART_LINK)
