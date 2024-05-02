#! /usr/bin/python3.10

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
import pandas as pd
from datetime import datetime
from time import sleep

import re
import time
import gevent
import pandas as pd
from bs4 import BeautifulSoup


from gevent import monkey
from urllib.request import Request, urlopen
from collections import defaultdict
from pprint import pprint as pp

import csv


monkey.patch_all()


now = datetime.now()
date_time_format = now.strftime("%Y%m%d_%H%M%S")
output_filename = f"job_description_data_{date_time_format}.csv"
save_directory = f"./linkedin/{output_filename}"

results = pd.DataFrame(columns=["job_link", "job_description"])


def scrape_url(url):
    start_time = time.time()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    sleep(20)

    expand_description(driver)
    job_description = extract_job_description(driver)
    # extracted_skills = extract_skills(job_description)


    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.4f} seconds\n")

    results = results._append(
        {"job_link": url, "job_description": job_description},
        ignore_index=True,
    )

    driver.quit()

    return job_description


def extract_job_description(driver):
    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".description"))
        )

        job_description = driver.execute_script(
            "return document.querySelector('.description').textContent"
        )

        job_description = job_description.strip()
        job_description = job_description.replace("\n", "  ")
        job_description = job_description.replace("\r", "  ")
        job_description = job_description.replace("\t", "  ")
        job_description = " ".join(job_description.split())

        return job_description
    except TimeoutException:
        return ""


def expand_description(driver):
    try:
        show_more_button = WebDriverWait(card, 15).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".show-more-less-html__button")
            )
        )

        show_more_button.click()
        time.sleep(60)
    except Exception as e:
        pass


def extract_job_description(driver):
    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".description"))
        )

        job_description = driver.execute_script(
            "return document.querySelector('.description').textContent"
        )

        job_description = job_description.strip()
        job_description = job_description.replace("\n", "  ")
        job_description = job_description.replace("\r", "  ")
        job_description = job_description.replace("\t", "  ")
        job_description = " ".join(job_description.split())

        return job_description
    except TimeoutException:
        return ""


def main():
    data = pd.read_csv("./linkedin/li_data_20240502_100019.csv")
    urls = data["job_link"].tolist()

    global_start_time = time.time()
    greenlets = [gevent.spawn(scrape_url, url) for url in urls]
    gevent.joinall(greenlets)
    global_end_time = time.time()
    global_elapsed_time = global_end_time - global_start_time
    print(f"Total time taken: {global_elapsed_time:.4f} seconds")


if __name__ == "__main__":
    main()
