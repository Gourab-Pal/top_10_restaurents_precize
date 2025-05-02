from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random
import json

# import necessary functions from utility.py and setup.py
from utility import format_review_count, send_texts_to_webelement, save_dictionary_as_json
from setup import configure, tear_down

# setup browser
driver = configure()
driver.get("https://www.google.com/")
time.sleep(random.uniform(1, 3))

# take input city name from user
print("Type city name and hit enter button.....")
city_name = input("Enter city name: ")
print("Processing top 10 restaurents of " + city_name + "....")

# search with simulated typing in the search fields
try:
    search_box = driver.find_element(By.XPATH, "//textarea[@class='gLFyf']")
except NoSuchElementException:
    print("Search box element not found")
query = "top 10 restaurants in " + city_name
send_texts_to_webelement(query, search_box)
search_box.send_keys(Keys.ENTER)

# click on more result to get more than 10 visible results
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='More places']"))).click()
except NoSuchElementException:
    print("More result button not found")

# extracts and saves top 10 results in dictionary
restaurent_cards = driver.find_elements(By.XPATH, "//div[contains(@id, 'tsuid')]")
assert len(restaurent_cards)>0, "No result found for the given city..."
restaurant_data = {}
for i in range(min(10, len(restaurent_cards))):  # Avoid IndexError if <10 results
    restaurent_name = restaurent_cards[i].find_element(By.XPATH, ".//span[@class='OSrXXb']").text
    restaurent_rating = restaurent_cards[i].find_element(By.XPATH, ".//span[@class='yi40Hd YrbPuc']").text
    restaurent_review = restaurent_cards[i].find_element(By.XPATH, ".//span[@class='RDApEe YrbPuc']").text
    restaurent_review = format_review_count(restaurent_review)
    restaurant_address = restaurent_cards[i].find_element(By.XPATH, ".//div[@class='rllt__details']//div[3]").text
    restaurant_data[restaurent_name] = {
        "rating": restaurent_rating,
        "reviews": restaurent_review,
        "address": restaurant_address
    }
assert len(restaurant_data)>0, "Scrapping data is unsuccessfull!"

# Save to JSON file
json_filename = "top_10_restaurent_" + city_name + ".json"
assert save_dictionary_as_json(json_filename, restaurant_data)==True

# close driver and browser instance
tear_down(driver)
