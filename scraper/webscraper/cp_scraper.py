from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

def get_cp_data():

    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)

# Leetcode -----------------------------------------------------
    website = "https://leetcode.com/contest/"
    driver.get(website)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    raw_data = soup.find('div', class_ = 'swiper-wrapper').text

    entries = [entry.strip() for entry in raw_data.split("Starts in") if entry.strip()]

    data = []

    for  entry in entries:
        entry = entry[entry.find("s") + 1:].strip()

        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            if day in entry:
                name = entry[:entry.index(day)].strip()
                date_time = entry[entry.index(day):].strip()
                break
        else:
            name = entry
            date_time = ""

        data.append({
            "Name": name,
            "Date & Time": date_time
        })

# CodeForces ---------------------------------------------------
    website = "https://codeforces.com/contests"
    driver.get(website)

    try:
        WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//Table"))
        )
    except Exception as e:
        print("Error: Table did not load in time.")
        driver.quit()
        exit()

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    table = soup.find('table')

    date_times = [element.text.strip() for element in table.find_all('a', target = '_blank') if element.text.strip()]

    names = table.find_all('tr')

    names = [element.find('td').text.strip() for element in names if element.find('td') and element.find('td').text.strip()]

    for i in range(len(names)):
        data.append({
            "Name": names[i],
            "Date & Time": date_times[i]
            })

# CodeChef -----------------------------------------------------
    website = "https://www.codechef.com/contests"
    driver.get(website)

    try:
        WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//Table"))
        )
    except Exception as e:
        print("Error: Table did not load in time.")
        driver.quit()
        exit()

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')

    for row in rows:
        row = row.find_all('td')
        row = [element.text.strip() for element in row if element.text.strip()]
        if not row:
            continue
        data.append({
            "Name": row[1].replace('Name', ''),
            "Date & Time": row[2].replace('Start', '')
        })

    df = pd.DataFrame(data)
    print(df)

    driver.quit()

 
    return df
