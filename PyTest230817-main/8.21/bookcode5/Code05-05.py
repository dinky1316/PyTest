from tkinter import *
window = Tk()

# 버튼, 버튼 텍스트 : 텍스트 , fg : 글자 색깔 , command : 이벤트 핸들러
button1 = Button(window, text="파이썬 종료", fg="red", command=quit)

button1.pack()

window.mainloop()
