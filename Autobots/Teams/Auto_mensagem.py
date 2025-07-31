import pyautogui
import time

print("A automação começará em 3 segundos...")
time.sleep(3)

pyautogui.press('win')

pyautogui.write("teams", interval=0.1)

pyautogui.press('enter')

time.sleep(1)

pyautogui.moveTo(360, 388, duration=1)

pyautogui.click()
time.sleep(1)

pyautogui.write("teste", interval=0.1)

pyautogui.press('enter')