import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ChromePath = r"chromedriver.exe"

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(
    executable_path=ChromePath, options=options)
driver.get('https://redbubble.dabu.ro/redbubble-popular-tags')
result_list = []
popularity_list = []
tag_list = []


def searchtrends(results_lower=100, results_upper=200, popularity_lower=1, popularity_upper=700):
    popularitycheck = driver.find_elements_by_xpath(
        "//*[@id='DataTables_Table_0']/thead/tr/th[2]")[0]
    popularitycheck.click()
    popularitycheck.click()
    pageno = 1
    while pageno < 50:
        for i in range(1, 25):
            stri = str(i)
            result = driver.find_elements_by_xpath(
                "//*[@id='DataTables_Table_0']/tbody/tr["+stri+"]/td[3]")
            for value in result:
                # if int(value.text) < 500 and int(value.text) > 200:
                if int(value.text) < 300:
                    result_list.append(value.text)
                    popularity = driver.find_elements_by_xpath(
                        '//*[@id="DataTables_Table_0"]/tbody/tr['+stri+']/td[2]')
                    for value in popularity:
                        popularity_list.append(int(value.text))

                    tag = driver.find_elements_by_xpath(
                        "//*[@id='DataTables_Table_0']/tbody/tr["+stri+"]/td[5]")
                    for value in tag:
                        tag_list.append(value.text)
        pageno += 1
        nextpage = driver.find_elements_by_xpath(
            "//*[@id='DataTables_Table_0_next']")[0]
        nextpage.click()

    final = zip(result_list, popularity_list, tag_list)
    for i, j, k in final:
        print(i, j, k)


if __name__ == "__main__":
    searchtrends()
