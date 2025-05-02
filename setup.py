from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def configure():
    """
    Sets up browser configurtions using Options from Chrome.
    Initilise driver object using options.
    Sets 10 second implicit waits for every find_element() and find_elements() methods.
    return driver object.
    """
    # Set Chrome options
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

    # Initialize the driver
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver

def tear_down(driver):
    """
    Closes current driver instance and quits the browser. 
    """
    driver.quit()