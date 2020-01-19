
from tkinter import*

data_list_1 = [10,20,200,200,400]
data_list_2 = [0,10,50,200,500]
time_list = ["2020/1/9","2020/1/10","2020/1/11","2020/1/12","2020/1/13"]

def update_data_1(new_data_list_1):#replace old data to new data
    data_list_1 = new_data_list_1
    return

def update_data_2(new_data_list_2):#replace old data to new data
    data_list_2 = new_data_list_2
    return

def make_form(numbers_1,numbers_2,times):
    start_x =0
    start_y = 50
    unit_y = 50
    
    canvas_tk = Tk()
    canvas_tk = Canvas(canvas_tk,width = 300,height = len(time_list*50)+50)
    canvas_tk.pack()
    
    canvas_tk.create_rectangle(0,0,200,50)#title block
    canvas_tk.create_text(30,25,text="time")
    canvas_tk.create_text(150,25,text="ALberta")
    canvas_tk.create_text(250,25,text="Nova Scotia")
    
    for position in range(int((len(numbers_1)*50)/50)):
        next_y = start_y+unit_y
        canvas_tk.create_rectangle(0,start_y,300,next_y)#draw rectangles
        canvas_tk.create_text(30,25+start_y,text=times[position])# adding text
        canvas_tk.create_text(150,25+start_y,text=numbers_1[position])# adding text
        canvas_tk.create_text(250,25+start_y,text=numbers_2[position])# adding text
        start_y = start_y+unit_y
        
    canvas_tk.create_line(100,0,100,int(len(time_list)*50+50))#draw vertical line
    canvas_tk.create_line(200,0,200,int(len(time_list)*50+50))#draw vertical line
    
    return

def make_graph(numbers_1,numbers_2):
    start_x =0
    start_y = 250
    unit_x = 500/len(numbers_1)
    if(numbers_1[-1]>>numbers_2[-1]):
        unit_y = 250/numbers_1[-1]
    else:
        unit_y = 250/numbers_2[-1]
    
    canvas_tk = Tk()
    canvas_tk = Canvas(canvas_tk,width = 500,height = 500)
    canvas_tk.pack()
    
    for position in range(len(numbers_1)):  #draw line 1 part
        next_x = start_x+unit_x*position  #x keep increasing
        next_y = start_y-unit_y*numbers_1[position] # y keep decreasing
        canvas_tk.create_line(start_x,start_y,next_x,next_y)
        start_x = start_x+unit_x*position
        start_y = start_y-unit_y*numbers_1[position]
        
    start_x =0
    start_y = 250
    unit_x = 500/len(numbers_1)
    if(numbers_1[-1]>numbers_2[-1]):
        unit_y = 250/numbers_1[-1]
    else:
        unit_y = 250/numbers_2[-1]
    
    for position in range(len(numbers_2)):  #draw line 2 part
        next_x = start_x+unit_x*position  #x keep increasing
        next_y = start_y-unit_y*numbers_2[position] # y keep decreasing
        canvas_tk.create_line(start_x,start_y,next_x,next_y,fill = "blue")
        start_x = start_x+unit_x*position
        start_y = start_y-unit_y*numbers_2[position]
    return

def graph_event():#protect from bug
    make_graph(data_list_1,data_list_2)
 
    return

def form_event():#protect from bug
    make_form(data_list_1,data_list_2,time_list)
    return

#main operating part
control_tk = Tk()
btn1 = Button(control_tk,text = "graph",command = graph_event)
btn2 = Button(control_tk,text = "form",command = form_event)
btn1.pack()
btn2.pack()


