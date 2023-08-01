# import time
#
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from threading import Thread
# # This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
#
# username="rakeshslambdatest"
# access_key="MIBbYCQdJybdc0R0STUXKaZYt8XimqqH7lYBGi5hO2Rw0Oxjjw"
#
# caps = [{
#     "build": "Python parallel testing",
#     "name": "Win11/Chrome101",
#     "platform": "Windows 11",
#     "browserName": "Chrome",
#     "version": "101.0"
# },
#     {
#         "build": "Python parallel testing",
#         "name": "Win10/Chrome97",
#         "platform": "Windows 10",
#         "browserName": "Chrome",
#         "version": "97.0"
#     },
#     {
#         "build": "Python parallel testing",
#         "name": "Win8/Edge101",
#         "platform": "Windows 8",
#         "browserName": "MicrosoftEdge",
#         "version": "101.0"
#     }
# ]
#
# grid_Url = "hub.lambdatest.com/wd/hub"
# url = "https://"+username+":"+access_key+"@"+grid_Url
#
# # run_session function adds a product in cart bstackdemo.com
#
# def run_session(desired_cap):
#     driver = webdriver.Remote(
#         grid_Url,caps)
#     driver.get("https://lambdatest.com/")
#     time.sleep(5)
#
#
# # Stop the driver
# # driver.quit()
# # The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session in parallel
# for cap in caps:
#     Thread(target=run_session, args=(cap,)).start()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
username = "rakeshslambdatest"
access_key = "MHu1nfiZVVPSteHsFVqybmvsxePoFJq0j8htKDk7uHcRwPgLGg"
grid_Url = "hub.lambdatest.com/wd/hub"
options = webdriver.ChromeOptions()
options.browser_version = ""
options.platform_name = "Windows 11"
lt_options = {}
lt_options["username"] ="ritamg"
lt_options["accessKey"] ="lHWNSA0QECwjeN8DoDb9U6KyXMBgAFXqlIIArkxeOTDSeEdLyG"





"
lt_options["project"] = "Parallel1"
lt_options["selenium_version"] = "4.0.0"
lt_options["w3c"] = True
options.set_capability('LT:Options', lt_options)
options2 = webdriver.EdgeOptions()
options2.browser_version = ""
options2.platform_name = "Windows 11"
# lt_options = {}
# lt_options["username"] = "utkarshs"
# lt_options["accessKey"] = "URepF67q3TohDB8lP8SrqlWGOPVyXbV2NBcx2nESEJj2S6hKC1"
lt_options["project"] = "Parallel1"
lt_options["selenium_version"] = "4.0.0"
lt_options["w3c"] = True
options2.set_capability('LT:Options', lt_options)
url = "https://"+username+":"+access_key+"@"+grid_Url
driver = webdriver.Remote(
    command_executor=url,
    options=options
    )
driver1 = webdriver.Remote(
    command_executor=url,
    options=options2
    )
driver.get("https://accounts.lambdatest.com/")
# driver.get("https://accounts.lambdatest.com/")
u_name = driver.find_element("id", "email")
u_name.send_keys("rakeshs@lambdatest.com")
# uname.send_keys("gauravp@lambdatest.com")
# for  password
p_word = driver.find_element("id", "password")
p_word.send_keys("Rakesh@9015")
# for login
login = driver.find_element("id", "login-button")
login.send_keys(Keys.ENTER)
time.sleep(10)
# for dropdown
print("Test completed")
time.sleep(10)
driver.quit()




