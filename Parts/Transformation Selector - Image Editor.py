# Create a new frame and transformation button
frm_transform = Frame(master = window, relief = RAISED, borderwidth = 10)
btn_transform = Button(master = frm_transform, text = "Transform",
                       fg="black", font = ("Times", 30), command = lambda:do_transform())

# The following two functions are to change the colour of the transformation
# button when the mouse hovers over it
def on_enter(e):
    btn_transform['background'] = 'black'
    btn_transform['foreground'] = 'white'

def on_leave(e):
    btn_transform['background'] = 'SystemButtonFace'
    btn_transform['foreground'] = 'black'

btn_transform.bind("<Enter>", on_enter)
btn_transform.bind("<Leave>", on_leave)

transformation = [0, [0, 1], 0, 0, 0, 0, 0, [0, 1, 1], [0, 1]] # Representing the respective transformations
inverse = IntVar()
threshold = IntVar()
greyscale = IntVar()
flipx = IntVar()
flipy = IntVar()
pinch = IntVar()
rotater = IntVar()
rotatel = IntVar()
opacity = IntVar()

frm_placeholder = Frame(master = frm_selection)

# Place in the transformation options
for i in range(9):
    frm_innerselection = Frame(master = frm_placeholder)
    frm_innerselection.grid(row = 0, column = i, padx = 10)
    if i == 0:
        cbtn_inverse = Checkbutton(master = frm_innerselection, text = "Inverse", 
                                   variable = inverse, onvalue = 1, offvalue = 0,
                                   font = ("arial", 15), command = lambda:selection())
        cbtn_inverse.pack()
    if i == 1:
        cbtn_threshold = Checkbutton(master = frm_innerselection, text = "Threshold",
                                    variable = threshold, onvalue = 1, offvalue = 0,
                                    font = ("arial", 15), command = lambda:selection())
        cbtn_threshold.pack()
    if i == 2:
        cbtn_greyscale = Checkbutton(master = frm_innerselection, text = "Greyscale", 
                                   variable = greyscale, onvalue = 1, offvalue = 0,
                                   font = ("arial", 15), command = lambda:selection())
        cbtn_greyscale.pack()
    if i == 3:
        cbtn_flipx = Checkbutton(master = frm_innerselection, text = "Flip x", 
                                 variable = flipx, onvalue = 1, offvalue = 0,
                                font = ("arial", 15), command = lambda:selection())
        cbtn_flipx.pack()
    if i == 4:
        cbtn_flipy = Checkbutton(master = frm_innerselection, text= "Flip y", 
                                 variable = flipy, onvalue = 1, offvalue = 0,
                                font = ("arial", 15), command = lambda:selection())
        cbtn_flipy.pack()
    if i == 5:
        cbtn_rotater = Checkbutton(master = frm_innerselection, text= "Rotate Right", 
                                 variable = rotater, onvalue = 1, offvalue = 0,
                                font = ("arial", 15), command = lambda:selection())
        cbtn_rotater.pack()
    if i == 6:
        cbtn_rotatel = Checkbutton(master = frm_innerselection, text= "Rotate Left", 
                                 variable = rotatel, onvalue = 1, offvalue = 0,
                                font = ("arial", 15), command = lambda:selection())
        cbtn_rotatel.pack()
    if i == 7:
        cbtn_pinch = Checkbutton(master = frm_innerselection, text = "Pinch and Zoom", 
                                 variable = pinch, onvalue = 1, offvalue = 0,
                                font = ("arial", 15), command = lambda:selection())
        cbtn_pinch.pack()
    if i == 8:
        cbtn_opacity = Checkbutton(master = frm_innerselection, text = "Opacity percentage", 
                                 variable = opacity, onvalue = 1, offvalue = 0,
                                font = ("arial", 15), command = lambda:selection())
        cbtn_opacity.pack()