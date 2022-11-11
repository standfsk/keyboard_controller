import pyautogui
from pynput.keyboard import Listener, Key, KeyCode, Controller
keyboard = Controller()
x = 1450
y = 268
addy = 38
addy2 = 52

def handlePress( key ):
    if hasattr(key, 'vk') and 96 <= key.vk <= 105:
        print( 'Press: {}'.format( key ) )
def handleRelease( key ):
    if hasattr(key, 'vk') and 96 == key.vk:
        # Numpad0: 코멘트 입력창 내용 삭제
        pyautogui.moveTo(x, y+addy*6+addy2)
        pyautogui.click()
        keyboard.press(Key.ctrl.value)
        keyboard.press('a')
        keyboard.release(Key.ctrl.value)
        keyboard.release('a')
        pyautogui.hotkey('del')
        pyautogui.moveTo(x, y+addy*6+addy2*2)
        pyautogui.click()
    elif hasattr(key, 'vk') and 97 == key.vk:
        # Numpad1: 통과
        pyautogui.moveTo(x, y)
        pyautogui.click()
    elif hasattr(key, 'vk') and 98 == key.vk:
        # Numpad2: 레이블 명칭 오류
        pyautogui.moveTo(x, y+addy*1)
        pyautogui.click()
    elif hasattr(key, 'vk') and 99 == key.vk:
        # Numpad3: 영역 설정 오류
        pyautogui.moveTo(x, y+addy*2)
        pyautogui.click()
    elif hasattr(key, 'vk') and 100 == key.vk:
        # Numpad4: 영역/레이블 설정 오류
        pyautogui.moveTo(x, y+addy*3)
        pyautogui.click()
    elif hasattr(key, 'vk') and 101 == key.vk:
        # Numpad5: 과설정
        pyautogui.moveTo(x, y+addy*4)
        pyautogui.click()
    elif hasattr(key, 'vk') and 102 == key.vk:
        # Numpad6: 테스트 오류
        pyautogui.moveTo(x, y+addy*5)
        pyautogui.click()
    elif hasattr(key, 'vk') and 103 == key.vk:
        # Numpad7: 기타
        pyautogui.moveTo(x, y+addy*6)
        pyautogui.click()
    elif hasattr(key, 'vk') and 104 == key.vk:
        # Numpad8: 코멘트 입력창 선택
        pyautogui.moveTo(x, y+addy*6+addy2)
        pyautogui.click()
    
    # 종료
    if key == Key.esc:
        return False
 
with Listener(on_press=handlePress, on_release=handleRelease) as listener:
    listener.join()


# numpad1: 통과
# numpad2: 레이블 명칭 오류
# numpad3: 영역 설정 오류
# numpad4: 영역/레이블 설정 오류
# numpad5: 과설정
# numpad6: 테스트 오류
# numpad7: 기타
# numpad8: 코멘트 입력창 선택
# numpad0: 코멘트 입력창 내용 삭제

# VK_NUMPAD0	96	Numeric keypad 0 key
# VK_NUMPAD1	97	Numeric keypad 1 key
# VK_NUMPAD2	98	Numeric keypad 2 key
# VK_NUMPAD3	99	Numeric keypad 3 key
# VK_NUMPAD4	100	Numeric keypad 4 key
# VK_NUMPAD5	101	Numeric keypad 5 key
# VK_NUMPAD6	102	Numeric keypad 6 key
# VK_NUMPAD7	103	Numeric keypad 7 key
# VK_NUMPAD8	104	Numeric keypad 8 key
# VK_NUMPAD9	105	Numeric keypad 9 key
