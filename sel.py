from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv
from time import sleep
import sys
import pandas as pd

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

    all_df = pd.DataFrame()

    # with open('export.csv', 'w') as file, open('log.txt', 'w') as log:
    # writer = csv.DictWriter(file, fieldnames=[
    #                         'Domain', 'Source', 'TF', 'Ahrefs DR', 'Ahrefs RD', 'Age', 'SZ Score', 'Date Added', 'Expires'])
    # writer.writeheader()

    while 1:
        table = driver.find_element(By.TAG_NAME, 'table')
        df = pd.read_html(table.get_attribute('outerHTML'))[0]
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df = df[df['Domain'].notna()]

        if all_df.empty:
            all_df = df
        else:
            all_df = pd.concat([all_df, df], ignore_index=True, sort=False)

        all_df.to_csv('export.csv')

        # rows = table.find_elements(
        #     By.CSS_SELECTOR, 'tbody tr.expired-domains')

        # print('rows', len(rows))
        # import pdb
        # pdb.set_trace()

        # for n, row in enumerate(rows):
        #     try:
        #         ahrefs_dr = row.find_element(
        #             By.CSS_SELECTOR, '[data-col-seq="ahrefs_dr"] a').text
        #     except:
        #         ahrefs_dr = row.find_element(
        #             By.CSS_SELECTOR, '[data-col-seq="ahrefs_dr"]').text

        #     try:
        #         row = {
        #             'Domain': row.find_element(By.CSS_SELECTOR, '[data-col-seq="1"]').text,
        #             'Source': row.find_element(By.CSS_SELECTOR, '[data-col-seq="data_source"] img').get_attribute('alt'),
        #             'TF': row.find_element(By.CSS_SELECTOR, '[data-col-seq="majestic_tf"] a').text,
        #             'Ahrefs DR': ahrefs_dr,
        #             'Ahrefs RD': row.find_element(By.CSS_SELECTOR, '[data-col-seq="ahrefs_rd"]').text,
        #             'Age': row.find_element(By.CSS_SELECTOR, '[data-col-seq="age"]').text,
        #             'SZ Score': row.find_element(By.CSS_SELECTOR, '[data-col-seq="sz_score"] a').text,
        #             'Date Added': row.find_element(By.CSS_SELECTOR, '[data-col-seq="date_added"]').text,
        #             'Expires': row.find_element(By.CSS_SELECTOR, '[data-col-seq="expiry_date"]').text,
        #         }
        #     except Exception as err:
        #         print(err)
        #         import pdb
        #         pdb.set_trace()

        #     print(row)
        #     writer.writerow(row)

        try:
            next_button = driver.find_element(By.CSS_SELECTOR, '.next a')
        except:
            break
        next_button.click()
        sleep(5)

    print('Таблица сохранена в export.csv')
