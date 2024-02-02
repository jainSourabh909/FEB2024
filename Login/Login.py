from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Replace with the path to your chromedriver executable
# chromedriver_path = '/path/to/chromedriver'

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to Google Images
driver.get("https://www.google.com/imghp")

# Find the search box element
search_box = driver.find_element("name", "q")

# Enter your search query (e.g., "cats")
search_box.send_keys("BUS" + Keys.RETURN)

# Wait for some time to load the results (you might need to adjust this)
time.sleep(2)

# Extract image URLs from the search results
image_elements = driver.find_elements(By.CSS_SELECTOR,".rg_i.Q4LuWd")
image_urls = [element.get_attribute("src") for element in image_elements]



# Close the browser
driver.quit()