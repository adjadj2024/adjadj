import json
import time

from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from database import Database
from css_selectors import Selectors
from constants import Constants


class Authorization:
    def __init__(self):
        self.username = None
        self.password = None
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def get_page(self, url):
        self.driver.get(url)

    def fill_field(self, text, locator):
        element = self.driver.find_element(By.CSS_SELECTOR, locator)
        element.send_keys(text)

    def click_on_element(self, locator):
        element = self.driver.find_element(By.CSS_SELECTOR, locator)
        element.click()

    def authorization(self, username, password):
        self.username = username
        self.password = password
        self.get_page(url=Constants.AUTHORIZATION_PAGE_URL)
        time.sleep(10)
        self.fill_field(username, Selectors.USERNAME)
        self.fill_field(password, Selectors.PASSWORD)
        self.click_on_element(Selectors.LOGIN_BUTTON)
        time.sleep(10)

    def get_user_id_from_response(self):
        for request in self.driver.requests:
            if request.method == 'POST':
                if 'https://coreapi.adjarabet.am/WebsiteService?' in request.url:
                    try:
                        response_body = json.loads(request.response.body.decode('utf-8'))
                    except json.JSONDecodeError:
                        continue
                    if response_body:
                        if "UserID" in response_body:
                            user_id = response_body["UserID"]
                            return user_id

    # def get_user_hash(self):
    #     for request in self.driver.requests:
    #         if request.method == 'GET':
    #             if 'https://salesiq.zohopublic.com/visitor/v2/channels/website?widgetcode' in request.url:
    #                 print(request.params)
    #                 return request.params.get('widgetcode')

    def get_user_hash(self):
        self.driver.get(Constants.AKCIA_PAGE_URL)
        time.sleep(20)
        for request in self.driver.requests:
            if request.method == 'POST':
                if ".php" in request.url:
                    decoded_str = request.body.decode()
                    params_dict = dict(pair.split('=') for pair in decoded_str.split('&'))
                    user_hash = params_dict.get('userHash', None)
                    return user_hash

    def write_user_in_db(self):
        db = Database()
        user_id = self.get_user_id_from_response()
        user_hash = self.get_user_hash()
        if user_hash:
            if user_id:
                db.create_table()
                db.insert_user(user_id=user_id, user_hash=user_hash)
                return 'Done', user_id, user_hash
            return "Something is wrong", '', ''
        return "Something is wrong", '', ''


if __name__ == '__main__':
    auth = Authorization()
    auth.authorization(username='davit.noreyan', password='QnarDavo1985&')
    print(auth.get_user_id_from_response())

    print(auth.get_user_hash())
