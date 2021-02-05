from works import working
from exercise import exercising

def main():
    # works일때, exercise일때 조건문
    # 작업 중 일시
    while True:
        num = int(input("works이면 1, exercise이면 2, 전체 종료 3:"))

        # working일때
        if num ==1:
            working()

        # exercising일때
        elif num ==2:
            exercising()

        elif num ==3:
            print("안녕히계세요 여러분~ 전 이 세상의 모든 굴레와 속박을 벗어던지고 제 행복을 찾아 떠납니다~!~!")
            break

        else:
            print("제대로 입력해!!!!!!!!!!!!!!!!!!!")




if __name__ == "__main__":
    main()