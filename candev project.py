
from tkinter import*

data_list = [0,10,50,200,400]
time_list = ["2020/1/9","2020/1/10","2020/1/11","2020/1/12","2020/1/13"]

def update_data(new_data_list):#replace old data to new data
    data_list = new_data_list
    return

def make_form(numbers,times):
    start_x =0
    start_y = 50
    unit_y = 50
    
    canvas_tk = Tk()
    canvas_tk = Canvas(canvas_tk,width = 200,height = len(numbers*50)+50)
    canvas_tk.pack()
    
    canvas_tk.create_rectangle(0,0,200,50)#title block
    canvas_tk.create_text(30,25,text="time")
    canvas_tk.create_text(150,25,text="value")
    
    for position in range(int((len(numbers)*50)/50)):
        next_y = start_y+unit_y
        canvas_tk.create_rectangle(0,start_y,200,next_y)#draw rectangles
        canvas_tk.create_text(30,25+start_y,text=times[position])# adding text
        canvas_tk.create_text(150,25+start_y,text=numbers[position])# adding text
        start_y = start_y+unit_y
        
    canvas_tk.create_line(100,0,100,int(len(numbers)*50+50))#draw middle line

    
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

def graph_event():#protect from bug
    make_graph(data_list)
    return

def form_event():#protect from bug
    make_form(data_list,time_list)
    return

control_tk = Tk()
btn1 = Button(control_tk,text = "graph",command = graph_event)
btn2 = Button(control_tk,text = "form",command = form_event)
btn1.pack()
btn2.pack()


