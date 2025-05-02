# 🍽️ Top 10 Restaurants Scraper using Selenium

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-Automation-brightgreen)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-Testing-orange)](https://docs.pytest.org/)

This project is a web automation tool built using **Selenium** that fetches the top 10 restaurants in a given city using Google Search and stores the details in a JSON file.

---

## 📁 Project Structure

```
top_10_restaurents_precize/
├── main.py                     # Main execution script
├── setup.py                    # Browser setup and teardown logic
├── utility.py                  # Reusable helper functions
└── README.md                   # Project documentation
```

---

## 🧠 What It Does

- Launches Google Chrome in Incognito mode using Selenium.
- Simulates human-like typing of search query: `top 10 restaurants in <city>`.
- Extracts restaurant details:
  - Name
  - Rating
  - Number of reviews (e.g., 3.5K → 3500)
  - Address
- Saves results in a JSON file.

---

## 🛠️ File Overview

### `main.py`
- Accepts user input for a city.
- Performs search and scraping using Selenium.
- Stores top 10 results in JSON.

### `setup.py`
- `configure()`: sets up Chrome WebDriver with options.
- `tear_down()`: closes the WebDriver session.

### `utility.py`
- `format_review_count(text)`: converts "3.5K" or "2M" into integers.
- `send_texts_to_webelement(query, webelement)`: types text with delays.
- `save_dictionary_as_json(json_filename, dictionary)`: safely writes dictionary to JSON with I/O error handling.


---

## ✅ Features

- Human-like search typing
- Converts abbreviated review counts (e.g., "2.5K" → 2500)
- Exception handling for missing elements and file errors
- Modular and reusable codebase
- Pytest-enabled for maintainability

---

## 📦 Installation

```bash
git clone https://github.com/Gourab-Pal/top_10_restaurents_precize.git
cd top_10_restaurents_precize
```

---

## 🚀 How to Run

```bash
python main.py
```

You’ll be prompted to input a city name. The script:
1. Opens Chrome browser.
2. Searches “Top 10 restaurants in <city>”.
3. Extracts results and saves to `top_10_restaurent_<city>.json`.

---



## 📋 Example Output

```json
{
  "Spice Garden": {
    "rating": "4.6",
    "reviews": 3200,
    "address": "1234 Main Street, Delhi"
  },
  "Flame & Grill": {
    "rating": "4.3",
    "reviews": 2500,
    "address": "Salt Lake Sector V, Kolkata"
  }
}
```

---

## 🔒 Requirements

```text
selenium
pytest
```

Install via:

```bash
pip install selenium
pip install pytest
```

---



## 📬 Contact

**Gourab Pal**  
📧 gourab.pal.gpal@gmail.com  
🔗 [LinkedIn](http://www.linkedin.com/in/gourab-pal-0327801a4)

---

## 📄 License

This project is free to use. Feel free to collaborate!
