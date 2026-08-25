import pyautogui

pyautogui.PAUSE = 2


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.PAUSE = 0.50




pyautogui.press("tab")


pyautogui.PAUSE = 2

pyautogui.press("enter")

pyautogui.hotkey("ctrl", "t")

pyautogui.write("https://www.bible.com/pt/bible/212/PSA.48.1-14.ARC")

pyautogui.press("enter")

pyautogui.hotkey("ctrl", "t")

pyautogui.write("https://www.youtube.com/watch?v=4_rv9Jmgc78")

pyautogui.press("enter")
