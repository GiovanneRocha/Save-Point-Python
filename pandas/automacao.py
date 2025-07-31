# 📦 Instalar: pip install pyautogui
import pyautogui
import time

# 🔧 Início da automação
print("🔧 Automação começará em 5 segundos...")
print("⏳ Preparando ambiente...")
time.sleep(5)

# 1️⃣ Mover o mouse e clicar 🖱️
pyautogui.moveTo(100, 100, duration=1)
pyautogui.click()

# 2️⃣ Digitar mensagem ⌨️
pyautogui.write("Automação iniciada com sucesso!", interval=0.1)

# 3️⃣ Pressionar Enter ↩️
pyautogui.press('enter')

# 4️⃣ Salvar com Ctrl + S 💾
pyautogui.hotkey('ctrl', 's')

# 5️⃣ Capturar posição atual do mouse 📍
x, y = pyautogui.position()
print(f"📍 Posição atual do mouse: ({x}, {y})")

# 6️⃣ Abrir menu iniciar 🪟
pyautogui.press('win')
print("⏳ Aguardando menu iniciar abrir...")
time.sleep(2)

# 7️⃣ Copiar e colar texto 📋
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')

# 8️⃣ Selecionar e copiar área com o mouse ✂️
pyautogui.moveTo(300, 300)
pyautogui.mouseDown()
pyautogui.moveTo(500, 300)
pyautogui.mouseUp()
pyautogui.hotkey('ctrl', 'c')

# 9️⃣ Tirar print da tela inteira 🖼️
screenshot_full = pyautogui.screenshot()
screenshot_full.save("screenshot_completa.png")

# 🔟 Tirar print de uma área específica 📸
# Define a região da tela: (x, y, largura, altura)
screenshot_area = pyautogui.screenshot(region=(100, 100, 400, 300))
screenshot_area.save("prints/screenshot_area.png")
screenshot_area.save(r"C:\Users\S492704\Pictures\tday\screenshot_PPacote.png")


# 1️⃣1️⃣ Rolar a tela 🔽🔼
pyautogui.scroll(-500)  # Para baixo
pyautogui.scroll(500)   # Para cima

# 1️⃣2️⃣ Rolar horizontalmente ↔️
pyautogui.keyDown('shift')
pyautogui.scroll(500)   # Direita ➡️
pyautogui.scroll(-500)  # Esquerda ⬅️
pyautogui.keyUp('shift')

# 1️⃣3️⃣ Duplo clique 🖱️🖱️
pyautogui.doubleClick()

# 1️⃣4️⃣ Clique com botão direito 🖱️➡️
pyautogui.rightClick()

# 1️⃣5️⃣ Arrastar e soltar 🧲
pyautogui.moveTo(400, 400)
pyautogui.dragTo(600, 400, duration=1)

# 1️⃣6️⃣ Esperar carregamento de site ou sistema 🌐
print("⏳ Aguardando carregamento do site...")
time.sleep(5)

# 🎯 Nomes das teclas de seta:
# Tecla	Nome usado no pyautogui
# ⬆️ Seta para cima	"up"
# ⬇️ Seta para baixo	"down"
# ⬅️ Seta para esquerda	"left"
# ➡️ Seta para direita	"right"


# 1️⃣7️⃣ Alerta final ⚠️
pyautogui.alert("Automação concluída com sucesso, agora revise o resultado.")

print("✅ Script de automação finalizado.")
