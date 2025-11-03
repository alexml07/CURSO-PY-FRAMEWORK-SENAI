import pyautogui as py

py.press("win")
py.write("chrome")
py.press("enter")
py.sleep(2)
py.write("senai americana")
py.press("enter")
# py.sleep(5)
# print(py.position())  # Posição do link do site
py.sleep(2)
py.click(x=246, y=462, button="left")  # Clique no link do site
# py.sleep(3)
# print(py.position())
py.sleep(2)
py.click(x=1405, y=770, button="left")  # Clique no link do site
# py.sleep(3)
# print(py.position())
py.sleep(2)
py.click(x=241, y=501, button="left")
py.sleep(1)
py.write("python")
py.sleep(1)
py.press("enter")
py.sleep(1)  # Rola a página para baixo
py.vscroll(-500)  # Rola a página para baixo