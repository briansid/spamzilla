from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv
from time import sleep
import sys

with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    driver.implicitly_wait(10)
    driver.get('https://www.spamzilla.io/account/login/')
    input('Откройте таблицу и нажмите Enter (ctrl+c для выхода) ')

    try:
        driver.find_element(By.TAG_NAME, 'table')
    except:
        print('Таблица не найдена')
        sys.exit(0)

    print('Export... Можете свернуть все окна')

    with open('export.csv', 'w') as file, open('log.txt', 'w') as log:
        writer = csv.DictWriter(file, fieldnames=[
                                'Domain', 'Source', 'TF', 'Ahrefs DR', 'Ahrefs RD', 'Age', 'SZ Score', 'Date Added', 'Expires'])
        writer.writeheader()

        while 1:
            table = driver.find_element(By.TAG_NAME, 'table')
            rows = table.find_elements(
                By.CSS_SELECTOR, 'tbody tr.expired-domains')

            for n, row in enumerate(rows):
                try:
                    row = {
                        'Domain': row.find_element(By.CSS_SELECTOR, '[data-col-seq="1"]').text,
                        'Source': row.find_element(By.CSS_SELECTOR, '[data-col-seq="data_source"] img').get_attribute('alt'),
                        'TF': row.find_element(By.CSS_SELECTOR, '[data-col-seq="majestic_tf"] a').text,
                        'Ahrefs DR': row.find_element(By.CSS_SELECTOR, '[data-col-seq="ahrefs_dr"] a').text,
                        'Ahrefs RD': row.find_element(By.CSS_SELECTOR, '[data-col-seq="ahrefs_rd"]').text,
                        'Age': row.find_element(By.CSS_SELECTOR, '[data-col-seq="age"]').text,
                        'SZ Score': row.find_element(By.CSS_SELECTOR, '[data-col-seq="sz_score"] a').text,
                        'Date Added': row.find_element(By.CSS_SELECTOR, '[data-col-seq="date_added"]').text,
                        'Expires': row.find_element(By.CSS_SELECTOR, '[data-col-seq="expiry_date"]').text,
                    }
                    writer.writerow(row)
                except:
                    log.write(table.get_attribute('outerHTML'))
                    log.write('\n')
                    continue
            try:
                next_button = driver.find_element(By.CSS_SELECTOR, '.next a')
            except:
                break
            next_button.click()
            sleep(5)

        print('Таблица сохранена в export.csv')
