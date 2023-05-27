from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get('https://www.n11.com/bilgisayar')

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "productName")))

product_items = driver.find_elements(By.CLASS_NAME, "productName")
price_items = driver.find_elements(By.CLASS_NAME, "newPrice.cPoint.priceEventClick")

for product, price in zip(product_items, price_items):
    print(f"{product.text} : {price.text}")

driver.quit()
