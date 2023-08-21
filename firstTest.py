# print("hello python")

# a=1
# print(type(a))
# print("출력형식 %d"%(a))

# print("이메일을 입력해주세요")
# email=input()
# print(f"이메일 : {email}")

import turtle as t

t.shape('turtle')
t.bgcolor("black")
t.color("black")

n = 50
t.color("white")
t.speed(0)

for i in range(1):

   for i in range(n):
      t.circle(80)
      t.right(10)
      t.forward(10)
    
   t.up()

   for i in range(n):
      t.circle(0)
      t.left(10)
      t.forward(20)

   t.down()

   for i in range(n):
      t.circle(80)
      t.right(10)
      t.forward(10)


t.done()
