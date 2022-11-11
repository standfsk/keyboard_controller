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
        # 4: 코멘트 입력창 선택
        pyautogui.moveTo(1488, 552)
        pyautogui.click()
    elif key == KeyCode(char='5'):
        # 5: 코멘트 입력창 내용 삭제
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
# 4: 코멘트 입력창 선택
# 5: 코멘트 입력창 내용 삭제