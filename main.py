import random
import os, sys
import time
import string
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

index = 0
fstring = ""
cwd = os.path.dirname(sys.executable) if hasattr(sys, 'frozen') else os.path.dirname(os.path.realpath(sys.argv[0]))
f = open("NitroCodes.txt", "a")
chrome_options = webdriver.ChromeOptions()

def gen():
    global index
    code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    index += 1
    return code

def check(string):
    driver.get("https://discordapp.com/gifts/{}".format(string))
    while True:
        try:
            driver.find_element_by_tag_name("button")
            break
        except NoSuchElementException:
            time.sleep(0.5)
    if not "This gift code may be expired or you might have the wrong code." in driver.find_element_by_tag_name("body").text:
        return True
    return False

print("Nitroxx - Discord Nitro Brute Forcer")
print("                       Coded By M47Z\n")

amount = int(input("How many codes should be generated?: "))

print("\nOpening Chrome...")

chrome_options.add_argument("--disable-notification")
chrome_options.add_argument("--force-dark-mode")
chrome_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=chrome_options, executable_path="{}/chromedriver.exe".format(cwd))

driver.maximize_window()

print("\nGenerating...\n")

while amount > 0:
    code = gen()
    print("Testing Code: {} Attempt Number {}".format(code, index), end="\r")
    if check(code):
        fstring += "https://discordapp.com/gifts/{}\n".format(code)
        amount -= 1
        
f.write(fstring)
