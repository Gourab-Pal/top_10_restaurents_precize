import time
import random
import json
from selenium.common.exceptions import NoSuchElementException

def format_review_count(text):
    """
    Convert shorthand like (2K), (3.5M), (4B), (1.2T) into actual numbers.
    Removes any parentheses.
    """
    try:
        text = text.replace("(", "").replace(")", "")
        text = text.upper().replace(",", "").strip()
        if text.endswith("K"):
            return int(float(text[:-1]) * 1_000)
        elif text.endswith("M"):
            return int(float(text[:-1]) * 1_000_000)
        elif text.endswith("B"):
            return int(float(text[:-1]) * 1_000_000_000)
        elif text.endswith("T"):
            return int(float(text[:-1]) * 1_000_000_000_000)
        else:
            return int(text)
    except:
        return None

def send_texts_to_webelement(query, webelement):
    """
    Simulate human typing behavior in a text field.
    """
    try:
        webelement.clear()
        for char in query:
            webelement.send_keys(char)
            time.sleep(random.uniform(0.05, 0.2)) 
    except NoSuchElementException:
        print("Element not found")

def save_dictionary_as_json(json_filename, dictionary):
    """
    Save dictionary to a JSON file.
    """
    try:
        with open(json_filename, "w", encoding="utf-8") as f:
            json.dump(dictionary, f, ensure_ascii=False, indent=4)
        return True
    except IOError as e:
        print("I/O error occured!")
        return False
    except Exception as e:
        print("Unexpected exception while saving json file!")
        return False
