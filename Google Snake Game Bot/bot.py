import selenium
from selenium import webdriver as wd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
from pynput.keyboard import Key, Controller

# Link to Snake Game
url = "https://www.google.com/search?q=google+snake+game&rlz=1C1RXQR_enCA974CA974&oq=google+snake+game&aqs=chrome..69i57j69i64.2084j0j7&sourceid=chrome&ie=UTF-8"
driver = wd.Chrome(executable_path="chromedriver.exe")
driver.get(url)

# Buttons

# Clicks on Snake Game
start_button = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[2]/div/div')
start_button.click()
# Clicks on Settings Button
settings_button = driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div/div/g-lightbox/div[2]/div[2]/span/div/div[3]/div/div[4]/div[2]')
settings_button.click()

# Selects Specific setting options
pyautogui.press('down')
pyautogui.press('right')
pyautogui.press('right')
pyautogui.press('right')
pyautogui.press('right')
pyautogui.press('down')
pyautogui.press('right')
pyautogui.press('right')
pyautogui.press('down')
pyautogui.press('right')
pyautogui.press('enter')

# Executes Snake Moves using Pyautogui, however this is not as efficient as pynput, and will thus not be the primary method used
def snake_moves():
    while True:
        # 165 Current Record
        # Normal Speed : 2.13 or 2.268
        # Fast 1.43 or 1.42
        #pyautogui.press('down')
        #pyautogui.press('right')
        pyautogui.press('down')
        pyautogui.press('right')
        time.sleep(1.25)


button = Controller()
while True:
    # List of timings and corresponding scores
    # Note that 250 is the max score, so the closer to 250, the better
    # 1.485 = 233
    # 1.487 = 234
    # 1.48 = 36
    # 1.48 = 77
    # 1.488 = 56
    # 1.49 = 70
    # 1.492 = 72
    # 1.4875 = 239
    # 1.4877 = 250

    time.sleep(1.4877)
    button.press(Key.down)
    button.release(Key.down)
    button.press(Key.right)
    button.release(Key.right)
