import pyautogui
import base64


def ShotAndSave():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.jpeg')
    with open('screenshot.jpeg', "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

