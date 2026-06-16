from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
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
    driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
    sleep(3)  # wait 3 seconds for page to fully load

    books = driver.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')
    print(f"Found {len(books)} books")

    results = []

    for book in books:
        try:
            title = book.find_element(By.CSS_SELECTOR, 'span.title-content').text.strip()
            
            author_els = book.find_elements(By.CSS_SELECTOR, 'a.author-link')
            authors = '; '.join([a.text.strip() for a in author_els])
            
            format_year = book.find_element(By.CSS_SELECTOR, 'span.display-info-primary').text.strip()

            results.append({
                'Title': title,
                'Author': authors,
                'Format-Year': format_year
            })

        except Exception as e:
            print(f"Skipping a result: {e}")
            continue

    df = pd.DataFrame(results)
    print(df)

    df.to_csv('get_books.csv', index=False)
    print("Saved to get_books.csv")

    with open('get_books.json', 'w') as f:
        json.dump(results, f, indent=4)
    print("Saved to get_books.json")

except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()