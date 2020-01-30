from selenium.webdriver.common.by import By


class ProductPageLocator():
    GET_LINK_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    GET_PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner article div div h1")
    GET_BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")
    GET_ALERT_ABOUT_PROTUCT_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages strong")
    GET_PRICE_OF_PRODUCT_LINK = (By.CSS_SELECTOR, "#content_inner .price_color")