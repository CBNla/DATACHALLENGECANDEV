
from tkinter import*

data_list_AS = [10,20,200,200,400]#Alberta power supply
data_list_AD = [0,10,50,200,500]#Alberta power demand
data_list_NS = [100,100,100,100,100]#Nova Scotia power supply
data_list_ND = [200,200,200,200,200]#Nova Scotia power demand
time_list = ["2020/1/9","2020/1/10","2020/1/11","2020/1/12","2020/1/13"]#time

def update_data_AS(new_data_list):#replace old data to new data
    data_list_AS = new_data_list
    return

def update_data_AD(new_data_list):#replace old data to new data
    data_list_AD = new_data_list
    return

def update_data_NS(new_data_list):#replace old data to new data
    data_list_NS = new_data_list
    return

def update_data_ND(new_data_list):#replace old data to new data
    data_list_ND = new_data_list
    return

def update_time(new_data_list):#replace old data to new data
    time_list = new_data_list
    return

def make_form(numbers_1,numbers_2,numbers_3,numbers_4,times):
    start_x =0
    start_y = 50
    unit_y = 50
    
    canvas_tk = Tk()
    canvas_tk = Canvas(canvas_tk,width = 500,height = len(time_list*50)+100)
    canvas_tk.pack()
    
    canvas_tk.create_rectangle(0,0,500,50)#title block
    canvas_tk.create_text(30,25,text="time")
    canvas_tk.create_text(175,25,text="Alberta")
    canvas_tk.create_text(375,25,text="Nova Scotia")
    canvas_tk.create_text(150,75,text="power supply")
    canvas_tk.create_text(250,75,text="power demand")
    canvas_tk.create_text(350,75,text="power supply")
    canvas_tk.create_text(450,75,text="power demand")
    canvas_tk.create_text(30,75,text="P unit: MW")
    
    for position in range(int((len(numbers_1)*50)/50)):
        next_y = start_y+unit_y
        canvas_tk.create_rectangle(0,start_y,500,next_y)#draw rectangles
        canvas_tk.create_text(30,75+start_y,text=times[position])# adding text
        canvas_tk.create_text(150,75+start_y,text=numbers_1[position])# adding text
        canvas_tk.create_text(250,75+start_y,text=numbers_2[position])# adding text
        canvas_tk.create_text(350,75+start_y,text=numbers_3[position])# adding text
        canvas_tk.create_text(450,75+start_y,text=numbers_4[position])# adding text
        start_y = start_y+unit_y
        
    canvas_tk.create_line(100,50,100,int(len(time_list)*50+100))#draw vertical line
    canvas_tk.create_line(200,50,200,int(len(time_list)*50+100))#draw vertical line
    canvas_tk.create_line(300,50,300,int(len(time_list)*50+100))#draw vertical line
    canvas_tk.create_line(400,50,400,int(len(time_list)*50+100))#draw vertical line
    
    return

def make_graph(numbers_1,numbers_2,numbers_3,numbers_4):
    start_x =0
    start_y = 250
    
    if(len(numbers_1)>len(numbers_3)):
        unit_x = 500/len(numbers_1)
    else:
        unit_x = 500/len(numbers_3)
    if(numbers_1[-1]>numbers_3[-1]):
        unit_y = 250/numbers_1[-1]
    else:
        unit_y = 250/numbers_3[-1]
    
    canvas_tk = Tk()
    canvas_tk = Canvas(canvas_tk,width = 500,height = 500)
    canvas_tk.pack()
    canvas_tk.create_line(0,250,500,250,fill = "red")#x-axis
    canvas_tk.create_line(0,0,5,500,fill = "red")#y-axis
    
    for position in range(len(numbers_1)):  #draw line AS part
        next_x = start_x+unit_x*position  #x keep increasing
        next_y = start_y-unit_y*numbers_1[position] # y keep decreasing
        canvas_tk.create_line(start_x,start_y,next_x,next_y,fill = "black")
        start_x = start_x+unit_x*position
        start_y = start_y-unit_y*numbers_1[position]
        
    start_x =0
    start_y = 250
    
    
    for position in range(len(numbers_2)):  #draw line AD part
        next_x = start_x+unit_x*position  #x keep increasing
        next_y = start_y-unit_y*numbers_2[position] # y keep decreasing
        canvas_tk.create_line(start_x,start_y,next_x,next_y,fill = "grey")
        start_x = start_x+unit_x*position
        start_y = start_y-unit_y*numbers_2[position]
    

    start_x =0
    start_y = 250

    for position in range(len(numbers_3)):  #draw line NS part
        next_x = start_x+unit_x*position  #x keep increasing
        next_y = start_y-unit_y*numbers_3[position] # y keep decreasing
        canvas_tk.create_line(start_x,start_y,next_x,next_y,fill = "blue")
        start_x = start_x+unit_x*position
        start_y = start_y-unit_y*numbers_3[position]
    

    start_x =0
    start_y = 250

    for position in range(len(numbers_4)):  #draw line ND part
        next_x = start_x+unit_x*position  #x keep increasing
        next_y = start_y-unit_y*numbers_4[position] # y keep decreasing
        canvas_tk.create_line(start_x,start_y,next_x,next_y,fill = "purple")
        start_x = start_x+unit_x*position
        start_y = start_y-unit_y*numbers_4[position]
    return

def graph_event():#protect from bug
    make_graph(data_list_AS,data_list_AD,data_list_NS,data_list_ND)
 
    return

def form_event():#protect from bug
    make_form(data_list_AS,data_list_AD,data_list_NS,data_list_ND,time_list)
    return

#main operating part
control_tk = Tk()
btn1 = Button(control_tk,text = "graph",command = graph_event)
btn2 = Button(control_tk,text = "form",command = form_event)
btn1.pack()
btn2.pack()


