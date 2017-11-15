# echo.py만 import시키게 하겠다.

# __all__은 외부에서 '*'로 import를 할 때, __all__안의 모든 애들을 다 가져가게 한다.(단, 리스트 안의 파일이 하나라도 없으면 import 시 에러)
__all__ = ['echo', 'effect']
from . import echo
