from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#your email and password here
email =""
pass_word = ""

#main py
try:
    driver.get("https://www.linkedin.com/home")

    try:
       
        user_name = driver.find_element(By.ID, "session_key")
        user_name.send_keys(email)

        password = driver.find_element(By.ID, "session_password")
        password.send_keys(pass_word)

        sign_in = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button")
        sign_in.click()
        time.sleep(5)

    except AttributeError:
        print("Already signed in")

    try:  

        driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3451156668&f_AL=true&geoId=105490917&keywords=electronic%20engineer&location=New%20Zealand&refresh=true")
        time.sleep(5)
        submit = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        submit.click()
    
    except AttributeError:
        print("Already applied for this job")

except AttributeError:
    print("No more jobs to apply for")

time.sleep(5)
driver.close()
