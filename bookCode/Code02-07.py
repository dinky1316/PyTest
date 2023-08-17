import turtle
import random

## 함수 선언 부분 ##
# 들여쓰기, 파이썬, 의무
def  screenLeftClick(x, y):
    global r, g, b
    turtle.pencolor((r, g, b))
    # pendown 선을 그리겠다 의미
    turtle.pendown()
    turtle.goto(x, y)
    
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)

    # 거북이 도장 찍기
    turtle.stamp()

    # 회전
    turtle.right(50)


# 우클릭시 기능
def  screenRightClick(x, y):
    # penup 선을 안그리고
    turtle.penup()
    # 해당 좌표로 이동
    turtle.goto(x, y)
    

# 휠 클릭시
def  screenMidClick(x, y):
    # 전역으로 설정된 rgb 색깔 설정부분
    global r, g, b
    tSize = random.randrange(1, 10)
    # shape size , 거북이 모양 크기
    turtle.shapesize(tSize)
    # 색상 랜덤을 이용해서 할당
    r = random.random()
    g = random.random()
    b = random.random()

## 변수 선언 부분 ##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

# 이벤트 핸들러 역할 onscreenclick
turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
