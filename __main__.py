# __main__.py의 실행 경로가 이미 top level에 있기 때문에 run.py안에서 '..graphic'을 실행할 때, ..이 __main__.py의 level을 가리키기 때문에 에러남
# top level에서는 '.' 또한 실행 안됨
# from play import run
# run.test_start()

from graphic import screen
from sound import echo

if __name__ == '__main__':
    screen.test_screen()
    echo.test_echo()