from selenium import webdriver
from time import sleep


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(10)

        fb_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/div[1]/button')
        fb_btn.click()

        # switch to login popup
        # base_window = self.driver.window_handles[0]
        # self.driver.switch_to_window(self.driver.window_handles[1])
        sleep(5)
        email_in = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input')
        email_in.send_keys('enter your mobile number here before running the script')

        login_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button')
        login_btn.click()

        password = input("type opt here\n")

        for index, value in enumerate(password):
            pw_in = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div[2]/div[3]/input[{}]'.format(index+1))
            pw_in.send_keys(value)

        continue_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button')
        continue_btn.click()

        # self.driver.switch_to_window(base_window)
        sleep(3)
        popup_1 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        sleep(3)
        popup_2 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


bot = TinderBot()
bot.login()
bot.auto_swipe()
