from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

def get_hack_data():

# Initialize the driver
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options = options)
       
# HackerEarth --------------------------------------------------
    website = "https://www.hackerearth.com/challenges/hackathon/"
    driver.get(website)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

# Get contest data and parse the string
    entries = soup.find_all('div', class_ = "challenge-content align-center")

    data = []
    for entry in entries:
        name = entry.find('span', class_ = "challenge-list-title challenge-card-wrapper").text.strip()
        if entry.find('div', class_ = 'date date-countdown'):
            date_time = entry.find('div', class_ = 'date date-countdown').text.strip().replace('\n', '')
        else:
            date_time = entry.find('div', class_ = 'date less-margin dark').text.strip()
        data.append({
            "Name": name,
            "Date & Time": date_time
        })

# Convert to pandas dataframe
    df = pd.DataFrame(data)
    print(df)
    '''

    website = "https://devfolio.co/hackathons/open"
    driver.get(website)

    try:
        WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "sc-crXcEl dsyQUs CompactHackathonCard__StyledCard-sc-9ff45231-0 fudhHJ"))
        )
    except Exception as e:
        print("Error: Table did not load in time.")
        print(e)
        driver.quit()
        exit()

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    entries = soup.find_all('div', class_ = "sc-crXcEl dsyQUs CompactHackathonCard__StyledCard-sc-9ff45231-0 fudhHJ")

    print(entries)
    '''
    driver.quit()

    return df
