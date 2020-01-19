
from tkinter import*

data_list = [0,10,50,200,400]

def update_data(new_data_list):#replace old data to new data
    data_list = new_data_list
    return

def make_form(numbers):
    canvas_tk = Tk()
    canvas_tk = Canvas(canvas_tk,width = 500,height = 500)
    canvas_tk.pack()
    return

def make_graph(numbers):
    start_x =0
    start_y = 250
    unit_x = 500/len(numbers)
    unit_y = 250/numbers[-1]
    
    canvas_tk = Tk()
    canvas_tk = Canvas(canvas_tk,width = 500,height = 500)
    canvas_tk.pack()
    
    for position in range(len(numbers)):  #draw line part
        next_x = start_x+unit_x*position  #x keep increasing
        next_y = start_y-unit_y*numbers[position] # y keep decreasing
        canvas_tk.create_line(start_x,start_y,next_x,next_y)
        start_x = start_x+unit_x*position
        start_y = start_y-unit_y*numbers[position]
    return

def graph_event():
    make_graph(data_list)
    return

def form_event():
    make_form(data_list)
    return

control_tk = Tk()
btn1 = Button(control_tk,text = "graph",command = graph_event)
btn2 = Button(control_tk,text = "form",command = form_event)
btn1.pack()
btn2.pack()


