from tkinter import *
window = Tk()

button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")

# 정렬. 왼쪽을 기준으로 나열하겠다
button1.pack(side=LEFT)
button3.pack(side=LEFT)
button2.pack(side=LEFT)

window.mainloop()
