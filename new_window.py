from tkinter import *
from tkinter import messagebox
from functools import partial
from PIL import ImageTk,Image
import queries

def open():
    global background_image
    top = Toplevel()
    top.title('Queries')
    background_image = ImageTk.PhotoImage(Image.open("library4.jpg"))
    my_canvas= Canvas(top,width=500,height=500)
    my_canvas.pack(fill='both',expand=True)
    my_canvas.create_image(0,0, image=background_image,anchor='nw')

    query1_button = Button(top,text='query1',bg='brown',width='7',font="Helvetica 15",command=lambda:queries.query1())
    query2_button = Button(top,text='query2',bg='brown',width='7',font="Helvetica 15",command=lambda:queries.query2())
    query3_button = Button(top,text='query3',bg='brown',width='7',font="Helvetica 15",command=lambda:queries.query3())
    query4_button = Button(top,text='query4',bg='brown',width='7',font="Helvetica 15",command=lambda:queries.query4())
    query5_button = Button(top,text='query5',bg='brown',width='7',font="Helvetica 15",command=lambda:queries.query5())
    query6_button = Button(top,text='query6',bg='brown',width='7',font="Helvetica 15",command=lambda:queries.query6())
    query7_button = Button(top,text='query7',bg='brown',width='7',font="Helvetica 15",command=lambda:queries.query7())
    query8_button = Button(top,text='query8',bg='brown',width='7',font="Helvetica 15",command=lambda:queries.query8())
    query9_button = Button(top,text='query9',bg='brown',width='7',font="Helvetica 15",command=lambda:queries.query9())
    query10_button = Button(top,text='query10',bg='brown',width='7',font="Helvetica 15",command=lambda:queries.query10())
    query11_button = Button(top,text='create views',bg='brown',width='7',font="Helvetica 15",command=lambda:queries.create_views())
    query12_button = Button(top,text='drop views',bg='brown',width='7',font="Helvetica 15",command=lambda:queries.drop_views())

    query1_button_window = my_canvas.create_window(0,0,anchor='nw',window=query1_button)
    query2_button_window = my_canvas.create_window(0,50,anchor='nw',window=query2_button)
    query3_button_window = my_canvas.create_window(0,100,anchor='nw',window=query3_button)
    query4_button_window = my_canvas.create_window(0,150,anchor='nw',window=query4_button)
    query5_button_window = my_canvas.create_window(0,200,anchor='nw',window=query5_button)
    query6_button_window = my_canvas.create_window(0,250,anchor='nw',window=query6_button)
    query7_button_window = my_canvas.create_window(100,0,anchor='nw',window=query7_button)
    query8_button_window = my_canvas.create_window(100,50,anchor='nw',window=query8_button)
    query9_button_window = my_canvas.create_window(100,100,anchor='nw',window=query9_button)
    query10_button_window = my_canvas.create_window(100,150,anchor='nw',window=query10_button)
    query11_button_window = my_canvas.create_window(100,200,anchor='nw',window=query11_button)
    query12_button_window = my_canvas.create_window(100,250,anchor='nw',window=query12_button)
