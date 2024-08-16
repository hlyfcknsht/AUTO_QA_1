import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import codecs

def main():
    fake = Faker()
    fields = {
            0 : f"{fake.first_name()}",
            1 : f"{fake.last_name()}",
            2 : f"{fake.first_name()}",
            3 : f"{2024 - int(fake.year())}",
            4 : f"{fake.city()}",
            5 : f"{fake.email()}"
    }


    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/1/1.html')
        count = 0
        for i in browser.find_elements(By.CLASS_NAME, "form"):
            i.send_keys(fields.get(count))
            count += 1
        browser.find_element(By.ID, "btn").click()
        result = browser.find_element(By.ID, "result").text
        print(result)
        time.sleep(30)

main()