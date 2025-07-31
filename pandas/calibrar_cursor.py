
import pyautogui
import time

print("Mova o mouse para a posição desejada em 5 segundos...")
time.sleep(5)

# Captura e exibe a posição atual do mouse
x, y = pyautogui.position()
print(f"Posição capturada: ({x}, {y})")

pyautogui.alert("Local do cursor gravado.")