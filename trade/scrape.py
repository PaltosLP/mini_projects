from selenium import webdriver
from time import sleep
import yaml
from selenium.webdriver.chrome.options import Options


#options = webdriver.ChromeOptions()
#options.add_argument(r"--user-data-dir=C:\Users\motat\AppData\Local\Chromium\User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
#options.add_argument(r'--profile-directory=YourProfileDir') #e.g. Profile 3
#driver = webdriver.Chrome(executable_path=r'C:\Users\motat\Desktop\Code\Python Code\Scrape\chromedriver.exe', chrome_options=options)

# conf = yaml.load(open('config.yml'))
# email = conf['user']['email']
# password = conf['user']['password']

#needs chromedriver.exe


driver = webdriver.Chrome()

def login(url,usernameId, username, password_name, password, submit_buttonId_1, submit_buttonId_2):
   driver.get(url)
   sleep(1)
   driver.find_element("id",usernameId).send_keys(username)
   sleep(1)
   driver.find_element("id",submit_buttonId_1).click()
   sleep(3)
   driver.find_element("name", password_name).send_keys(password)
   sleep(1)
   driver.find_element("id", submit_buttonId_2).click()
   sleep(10)
   
   #driver.find_element("id",":2v").click()
   #sleep(10)
   
   print(driver.page_source)
   #https://www.geeksforgeeks.org/web-driver-methods-in-selenium-python/
   #https://www.lambdatest.com/blog/selenium-webdriver-with-python/
   
   driver.quit()

# login("https://mail.google.com", "identifierId", email, "Passwd", password, "identifierNext", "passwordNext" )
