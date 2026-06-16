from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

try:
    driver.get("https://owasp.org/Top10/2025/")
    sleep(3)

    results = []

    links = driver.find_elements(By.CSS_SELECTOR, 'ol li a')
    
    for link in links:
        title = link.text.strip()
        href = link.get_attribute('href')
        if title:
            results.append({'title': title, 'href': href})

    print(results)

    with open('owasp_top_10.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'href'])
        writer.writeheader()
        writer.writerows(results)

    print("Saved to owasp_top_10.csv")

except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()