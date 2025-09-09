import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

#function for intializing the driver
def initialize_driver():
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

#funtion for URL
def open_url(driver,url):
    driver.get(url)
    driver.maximize_window()

#function to click a CTA button after waiting for it to be clickable
def click_cta_button(driver,cta_button_xpath):
    wait=WebDriverWait(driver,10)
    cta_button=wait.until(EC.element_to_be_clickable((By.XPATH,cta_button_xpath)))
    #driver.execute_script("arguments[0].click();",cta_button) #javaScrip function
    cta_button.click()

#function to switch to a new window and return to the original window
def switch_between_windows(driver):
    driver.switch_to.window(driver.window_handles[1])
    print("Switched to the new window: ",driver.title)
    driver.switch_to.window(driver.window_handles[0])
    print("Switched to the main window: ", driver.title)

def main():
    cta_button_xpath = "(//a[@class='cta_button'])[1]"
    url = "https://www.salesforce.com/your-account/"

    driver=initialize_driver()

    open_url(driver,url)

    click_cta_button(driver,cta_button_xpath)

    time.sleep(2)

    switch_between_windows(driver)

    driver.quit()

if __name__=="__main__":
    main()
