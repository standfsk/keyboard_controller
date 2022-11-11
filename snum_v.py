import pyautogui
from pynput.keyboard import Listener, Key, KeyCode, Controller
# 기능 x,y 세팅
x = 1450
y = 268
addy = 38
addy2 = 52
# 메뉴 x,y 세팅
menu_y = 175
i_x = 1458
c_x = 1536
r_x = 1660

keyboard = Controller()
def handlePress( key ):
    print( 'Press: {}'.format( key ) )
def handleRelease( key ):
    if key == KeyCode(char='1'):
        # 1: 통과
        pyautogui.moveTo(x, y)
        pyautogui.click()
    elif key == KeyCode(char='2'):
        # 2: 레이블 명칭 오류
        pyautogui.moveTo(x, y+addy*1)
        pyautogui.click()
    elif key == KeyCode(char='3'):
        # 3: 영역 설정 오류
        pyautogui.moveTo(x, y+addy*2)
        pyautogui.click()
    elif key == KeyCode(char='4'):
        # 4: 코멘트 입력창 선택
        pyautogui.moveTo(x, y+addy*6+addy2)
        pyautogui.click()
    elif key == KeyCode(char='5'):
        # 5: 코멘트 입력창 내용 삭제
        pyautogui.moveTo(x, y+addy*6+addy2)
        pyautogui.click()
        keyboard.press(Key.ctrl.value)
        keyboard.press('a')
        keyboard.release(Key.ctrl.value)
        keyboard.release('a')
        pyautogui.hotkey('del')
        pyautogui.moveTo(x, y+addy*6+addy2*2)
        pyautogui.click()
    elif key == KeyCode(char='6'):
        # 6: 검수 메뉴로 이동
        pyautogui.moveTo(i_x, menu_y)
        pyautogui.click()
    elif key == KeyCode(char='7'):
        # 7: 착장정보 메뉴로 이동
        pyautogui.moveTo(c_x, menu_y)
        pyautogui.click()
    elif key == KeyCode(char='8'):
        # 8: 반려 메뉴로 이동
        pyautogui.moveTo(r_x, menu_y)
        pyautogui.click()
    elif key == Key.esc:
        # esc: 프로그램 종료
        return False
    
with Listener(on_press=handlePress, on_release=handleRelease) as listener:
    listener.join()


# 1: 통과
# 2: 레이블 명칭 오류
# 3: 영역 설정 오류
# 4: 코멘트 입력창 선택
# 5: 코멘트 입력창 내용 삭제
# 6: 검수 메뉴로 이동
# 7: 착장정보 메뉴로 이동
# 8: 반려 메뉴로 이동
# esc: 프로그램 종료
