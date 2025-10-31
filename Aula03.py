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
