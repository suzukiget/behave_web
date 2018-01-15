
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By


driver=webdriver.Chrome("C:\\webdrive\\chromedriver.exe")
login_url = "https://bortnik.hipchat.com/login_password?email=genasmetchik%40gmail.com"



user_logs = []

def logining():
#login
    try:
        pswd = "Ry990sQ1"

        driver.get(login_url)
        driver.find_element_by_id("password").send_keys(pswd)
        driver.find_element_by_id("signin").click()
    except:
        while driver.current_url == login_url:
            logining()
def chat():
    wait = ui.WebDriverWait(driver, 10)

    driver.get("https://bortnik.hipchat.com/chat")
   # wait.until(lambda driver: driver.find_element_by_id('status_dropdown'))
    #driver.find_element_by_xpath("//span[text()='Alias room']").click()
   # try:
   #     wait.until(lambda driver: driver.find_element_by_id('input_actions_dropdown-trigger'))
   # except:
    wait.until(lambda driver: driver.find_element_by_id('status_dropdown'))
    driver.find_element_by_xpath("//span[text()='Alias room']").click()
    wait.until(lambda driver: driver.find_element_by_id('input_actions_dropdown-trigger'))
    driver.find_element_by_id("input_actions_dropdown-trigger").click()

    wait.until(
        lambda driver: driver.find_element_by_css_selector("#input_actions_dropdown > div > ul > li:nth-child(1) > a"))
    driver.find_element_by_css_selector("#input_actions_dropdown > div > ul > li:nth-child(1) > a").click()

   # wait.until(
    #    lambda driver: driver.switch_to.frame(driver.find_element_by_class_name('aliases')))

    wait.until(lambda driver: driver.find_element_by_class_name('hc-addon-iframe'))
    iframe = driver.find_element_by_class_name('hc-addon-iframe')
    driver.switch_to.frame(iframe)
    wait.until(lambda driver: driver.find_element(By.XPATH, '//*[@id="react-app"]/div/div/a'))
    confbut = driver.find_element(By.XPATH, '//*[@id="react-app"]/div/div/a')

    confbut.click()
    form = driver.find_element_by_name('alias')
    form.send_keys("@test")
    inputname = driver.find_element(By.XPATH, '//*[@id="react-app"]/div/form/div/div[2]/div/div/div/input')
    inputname.send_keys('@HenaYamkoviy')
    inputname.send_keys(u'\ue007')
    button = driver.find_element_by_css_selector('#react-app > div > form > div > div.aui-item.actions > input')
    button.click()


    table = driver.find_elements_by_css_selector('.aui>.aliases>.alias>.mentions')
    for element in table:
        if element == "@test":
            return True
        else:
            return False





logining()

chat()





