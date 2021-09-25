from selenium import webdriver

PATH = "/Users/Soccerboy_Krish/Documents/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://krishrastogi.com")
print(driver.title)

driver.quit()

