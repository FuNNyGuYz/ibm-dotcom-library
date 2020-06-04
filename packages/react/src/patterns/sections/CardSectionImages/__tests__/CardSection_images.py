from selenium import webdriver
import time
import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class cardSection_images(unittest.TestCase):
    def test_CardSectionImg(self):
        driver = webdriver.Chrome('C:\Sel_chrome\chromedriver.exe')
        driver.maximize_window()
        driver.refresh()
        driver.get("https://ibmdotcom-react-staging.mybluemix.net/")
        time.sleep(15)
        element = driver.find_element_by_id("explorerpatterns-sections-cardsectionimages")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        print("Card section images Selected")
        time.sleep(4)
        Selg10 = Select(driver.find_element_by_name('theme'))
        Selg10.select_by_visible_text("g10")
        print("g10 selected")
        time.sleep(4)
        driver.switch_to_frame("storybook-preview-iframe")
        print("frame switched")
        CardSection_image1 = driver.find_element_by_css_selector(".bx--card-group.bx--card-group--g10").value_of_css_property("background")
        print ("Theme is :" + CardSection_image1)
        time.sleep(2)
        driver.refresh()
        time.sleep(4)
        Selg90 = Select(driver.find_element_by_xpath("//select[@name='theme']"))
        Selg90.select_by_visible_text("g90")
        print("g90 selected")
        time.sleep(2)
        driver.switch_to_frame("storybook-preview-iframe")
        CardSection_image2 = driver.find_element_by_css_selector(".bx--card-group.bx--card-group--g90").value_of_css_property("background")
        print ("Theme is :" + CardSection_image2)
        time.sleep(2)
        driver.refresh()
        time.sleep(4)
        Selg100 = Select(driver.find_element_by_xpath("//select[@name='theme']"))
        Selg100.select_by_visible_text("g100")
        print("g100 selected")
        time.sleep(2)
        driver.switch_to_frame("storybook-preview-iframe")
        CardSection_image3 = driver.find_element_by_css_selector(".bx--card-group.bx--card-group--g100").value_of_css_property("background")
        print ("Theme is :" + CardSection_image3)
        time.sleep(2)
        driver.refresh()
        time.sleep(4)
        heading = driver.find_element_by_xpath("//textarea[@id='Heading (required):']")
        heading.clear()
        heading.send_keys("Serving society ethically in the age of Artificial Intelligence.")
        time.sleep(2)
        print("heading changed")
        driver.switch_to_default_content()
        time.sleep(2)
        driver.find_element_by_xpath("//*[contains(@title, 'Go full screen')]").click()
        print("full screen")
        time.sleep(2)
        driver.switch_to_frame("storybook-preview-iframe")
        time.sleep(2)
        Heading1 = driver.find_element_by_xpath("//h2[@class='bx--content-section__heading']")
        print("Updated heading is " + Heading1.text)
        time.sleep(2)
        driver.find_element_by_xpath("(//div[@class='bx--card__wrapper'])[1]").click()
        print ("Card clicked")
        time.sleep(2)
        driver.close()
