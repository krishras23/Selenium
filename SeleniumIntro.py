from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/Users/Soccerboy_Krish/Documents/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://maps.google.com")
p = driver.find_element_by_name("q")
p.send_keys("Restaurants in San Jose")
p.submit()


driver.get("https://sfhs.com/students")
username = driver.find_element_by_name("username")
username.send_keys("krishrastogi")
username.submit()
password = driver.find_element_by_name("password")
password.send_keys("not seeing my password :)")
password.submit()

for i in range(30):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "Day"))
    )
        print(element)
    except:
        driver.quit()


