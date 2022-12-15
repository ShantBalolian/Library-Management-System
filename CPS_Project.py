from tkinter import *
from tkinter import messagebox
from functools import partial
from PIL import ImageTk,Image

import populate
import create
import delete
import new_window


# create a GUI window
window = Tk()
# window.geometry("1350x700+0+0")
window.title("Manager window")
window.geometry("910x607+100+50")
window.resizable(False,False)
path = "C:/Users/reals/OneDrive/Desktop/CPSPROJECT/285-2850805_black-framed-eyeglasses-on-book-beside-cappuccino-coffee.jpg"
background_image = ImageTk.PhotoImage(Image.open(path))

# Create a canvas
my_canvas= Canvas(window,width=1000,height=1000)
my_canvas.pack(fill='both',expand=True)


def logout():
    window.destroy()
    import library

# Set image in canvas
my_canvas.create_image(0,0, image=background_image,anchor='nw')

# Add a text saying welcome back
my_canvas.create_text(350, 100, text ="Welcome back Manager!", font="Helvetica 45",fill="white")

# create tables button
create_button = Button(window,text='Create Tables',bg='brown',width='15',font="Helvetica 15",command=lambda: create.create_tables())
# delete tables button
delete_button = Button(window,text='Delete Tables',width='15',font="Helvetica 15",bg='brown',command=lambda: delete.drop_tables())
# populate tables button
populate_button = Button(window,text='Populate Tables',bg='brown',width='15',font="Helvetica 15",command=lambda:populate.populate_tables())

#new_window_button = Button(window,text='Database Queries',bg='brown',width='15',font="Helvetica 15", command=lambda:new_window.open())

logout = Button(window,text='Logout',bg='brown',width='15',font="Helvetica 15", command=logout)

# put the buttons on the screen
create_button_window = my_canvas.create_window(500,200,anchor='nw',window=create_button)
delete_button_window = my_canvas.create_window(500,250,anchor='nw',window=delete_button)
populate_button_window = my_canvas.create_window(500,300,anchor='nw',window=populate_button)
#new_window_button_window = my_canvas.create_window(500,350,anchor='nw',window=new_window_button)

logout_button_window = my_canvas.create_window(500,350,anchor='nw',window=logout)




window.mainloop()
