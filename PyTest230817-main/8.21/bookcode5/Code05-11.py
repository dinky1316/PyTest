from tkinter import *

# 윈도우 창 부분 인스턴스
window = Tk()

# 메뉴 부분 구성, mainMenu : 상위 메뉴
mainMenu = Menu(window)
# 메인 메뉴의 부모 창 -> window
window.config(menu=mainMenu)
# 파일 메뉴의 부모 창 -> 메인메뉴
fileMenu = Menu(mainMenu)
fileMenu2 = Menu(mainMenu)

mainMenu.add_cascade(label="파일", menu=fileMenu)
mainMenu.add_cascade(label="파일2", menu=fileMenu2)

# 부모 메뉴 : 파일 1
fileMenu.add_command(label="열기")
fileMenu.add_separator()
fileMenu.add_command(label="종료")

# 부모 메뉴 : 파일 2
fileMenu2.add_command(label="열기")
fileMenu2.add_separator()
fileMenu2.add_command(label="종료")

window.mainloop()
