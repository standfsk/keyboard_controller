

import pyautogui
from pynput.keyboard import Listener, Key, KeyCode, Controller
keyboard = Controller()
def handlePress( key ):
    print( 'Press: {}'.format( key ) )
def handleRelease( key ):
    if key == KeyCode(char='1'):
        # 1: 통과
        pyautogui.moveTo(1450, 268)
        pyautogui.click()
    elif key == KeyCode(char='2'):
        # 2: 레이블 명칭 오류
        pyautogui.moveTo(1450, 310)
        pyautogui.click()
    elif key == KeyCode(char='3'):
        # 3: 영역 설정 오류
        pyautogui.moveTo(1450, 348)
        pyautogui.click()
    elif key == KeyCode(char='4'):
        # 4: 영역/레이블 설정 오류
        pyautogui.moveTo(1450, 386)
        pyautogui.click()
    elif key == KeyCode(char='5'):
        # 5: 과설정
        pyautogui.moveTo(1450, 421)
        pyautogui.click()
    elif key == KeyCode(char='6'):
        # 6: 테스트 오류
        pyautogui.moveTo(1450, 461)
        pyautogui.click()
    elif key == KeyCode(char='7'):
        # 7: 기타
        pyautogui.moveTo(1450, 500)
        pyautogui.click()
    elif key == KeyCode(char='8'):
        # 8: 코멘트 입력창 선택
        pyautogui.moveTo(1488, 552)
        pyautogui.click()
    if key == KeyCode(char='9'):
        # 9: 코멘트 입력창 내용 삭제
        pyautogui.moveTo(1488, 552)
        pyautogui.click()
        keyboard.press(Key.ctrl.value)
        keyboard.press('a')
        keyboard.release(Key.ctrl.value)
        keyboard.release('a')
        pyautogui.hotkey('del')
        pyautogui.moveTo(1488, 652)
        pyautogui.click()
    
    # 종료
    if key == Key.esc:
        return False
 
with Listener(on_press=handlePress, on_release=handleRelease) as listener:
    listener.join()


# 1: 통과
# 2: 레이블 명칭 오류
# 3: 영역 설정 오류
# 4: 영역/레이블 설정 오류
# 5: 과설정
# 6: 테스트 오류
# 7: 기타
# 8: 코멘트 입력창 선택
# 9: 코멘트 입력창 내용 삭제

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