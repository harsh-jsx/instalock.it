import pyautogui
import time
import keyboard

def instalock():
    cords = {
        "jettX": 1024,
        "jettY": 1024,
        "ReynaX": 102,
        "ReynaY": 102,
        "CloveX": 10,
        "CloveY": 10,
    }
    whichOne = int(input("Please select an agent to instalock\n 1 for jett, 2 for reyna, 3 for clove: "))

    while True:
        if keyboard.is_pressed('ctrl'):
            print("Pressed ctrl, breaking!!!")
            break
        else:

            if whichOne == 1:
                event = keyboard.read_event()
                if event.event_type == keyboard.KEY_DOWN and event.name == 'f':
                    print("instalocking jett, Please press ctrl after your agent has been locked.")
                    for i in range(100):
                        pyautogui.click(cords["jettX"],cords["jettY"])
                        print("Clicked 100 times")
                        break
                else:
                    print("Waiting for user to press F")

            elif whichOne == 2:
                event = keyboard.read_event()
                if event.event_type == keyboard.KEY_DOWN and event.name == 'f':
                    print("instalocking Reyna, Please press ctrl after your agent has been locked.")
                    for i in range(100):
                        pyautogui.click(cords["ReynaX"],cords["ReynaY"])
                        print("Clicked 100 times")
                        break
                else:
                    print("Waiting for user to press F")
                    
            elif whichOne == 3:
                event = keyboard.read_event()
                if event.event_type == keyboard.KEY_DOWN and event.name == 'f':
                    print("instalocking Clove, Please press ctrl after your agent has been locked.")
                    for i in range(100):
                        pyautogui.click(cords["CloveX"],cords["CloveY"])
                        print("Clicked 100 times")
                        break
                else:
                    print("Waiting for user to press F")
            else:
                print("Wrong input")
instalock()