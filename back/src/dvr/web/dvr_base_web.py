from selenium import webdriver


class DvrBaseWeb:
    def __init__(self, config: dict):
        self.config = config
        dvrpath = self.config['chromedriver_filepath']
        self.driver = webdriver.Chrome(executable_path=dvrpath)

    def go_home(self, homepage: str):
        self.driver.get(homepage)
