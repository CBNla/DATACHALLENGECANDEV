from tkinter import*


def graph():
    print("1")
    return

def form():
    print("2")
    return


def canvas():
    canvas_tk = Tk()
    canvas = Canvas(canvas_tk,width = 500,height = 500)
    canvas.pack()
    return


control_tk = Tk()
btn1 = Button(control_tk,text = "graph",command = canvas)
btn2 = Button(control_tk,text = "form",command = form)
btn1.pack()
btn2.pack()
