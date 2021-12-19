import os
import json
from dvr.web.dvr_base_web import DvrBaseWeb


class DvrAisinWeb(DvrBaseWeb):
    def __init__(self, config: dict):
        super().__init__(config)
        self.go_home()

    def go_home(self):
        webpage = self.config['aisin_webpage']
        return super().go_home(webpage)

    def login(self):
        dirpath = self.config['aisin_usrinfo_dirpath']
        dirpath = os.path.expanduser(dirpath)
        filename = self.config['aisin_usrinfo_filename']
        filepath = dirpath + filename
        with open(filepath) as f:
            usrinfo = json.load(f)
        id = usrinfo['id']
        password = usrinfo['password']
        element = self.driver.find_element_by_id('HID_USER_ID')
        element.send_keys(id)
        element = self.driver.find_element_by_id('PASSWORD')
        element.send_keys(password)
        element = self.driver.find_element_by_class_name('ui-btn-hidden')
        element.submit()
