import pyautogui
import time

print("A automação começará em 3 segundos...")
time.sleep(3)

pyautogui.press('win')

pyautogui.write("edge", interval=0.5)

pyautogui.press('enter')

time.sleep(1)
pyautogui.hotkey('win', 'up')

time.sleep(3)
pyautogui.moveTo(1466, 114, duration=0.5)

pyautogui.click()

print("⏳ Aguardando carregamento do site...")
time.sleep(10)

pyautogui.moveTo(1543, 447, duration=0.5)

pyautogui.click()
pyautogui.doubleClick()
pyautogui.doubleClick()

pyautogui.moveTo(1251, 426, duration=0.5)

pyautogui.click()

time.sleep(1)
pyautogui.moveTo(570, 518, duration=0.5)

# Define a região da tela: (x, y, largura, altura)
screenshot_area = pyautogui.screenshot(region=(570, 518, 990, 415))
screenshot_area.save(r"C:\Users\S492704\Autobots\Forjaria\screenshot_PPacote.png")


pyautogui.scroll(-500)  # Para baixo

pyautogui.moveTo(570, 598, duration=0.5)

# Define a região da tela: (x, y, largura, altura)
screenshot_area = pyautogui.screenshot(region=(570, 598, 990, 361))
screenshot_area.save(r"C:\Users\S492704\Autobots\Forjaria\screenshot_PGerencia.png")

print("Fim.")
pyautogui.alert("Automação concluída com sucesso, agora revise o resultado.")