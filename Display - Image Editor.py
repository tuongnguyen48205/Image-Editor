sidetracker = 0 # Tracks the current image
displayed = 'placeholder'
lbl_imageinfo = 'placeholder'
lbl_displayed = 'placeholder'


def display(num):
    '''
    displays the image in its full size and a summary of its 
    information
    '''
    global image_tracker
    global filename_tracker
    global sidetracker
    global displayed
    global lbl_imageinfo
    global lbl_displayed
    sidetracker = 0
    # Make a new window
    displayed = Toplevel()
    displayed.geometry("1920x1080")
    displayed.resizable(False, False)
    # Place in the first image resizing it appropriately to fit
    selected_img = image_tracker[0]
    width, height = selected_img.size
    while height > 850 or width > 3000:
        width = int(width/2)
        height = int(height/2)
    selected_img = selected_img.resize((width,height))
    selected_img = ImageTk.PhotoImage(selected_img)
    selected_img.image = selected_img
    lbl_displayed = Label(master = displayed, image = selected_img)
    lbl_displayed.image = selected_img
    lbl_displayed.pack()
    # Time to display the images info
    lbl_Imageinfo_title = Label(text = "\nImage Summary:", fg = "black", font = ("times", 23, "bold"),
                          master = displayed)
    lbl_Imageinfo_title.pack()
    filepath_list = reversed(list(filename_tracker[0]))
    filename2 = []
    for i in filepath_list:
        if i == '/':
            break
        else:
            filename2.append(i)
    lbl_imageinfo = Label(text = f"Filename: {''.join(reversed(filename2))}\nFilepath: {filename_tracker[0]}\nMode: {image_tracker[0].mode}\nWidth: {image_tracker[0].width}px\n Height: {image_tracker[0].height}px",
                          font = ("ariel", 17), master = displayed, fg = "black")
    lbl_imageinfo.pack()
    # Add the left and right navigation buttons
    btn_right = Button(master = displayed, text = '>', font = ("ariel", 50), command = lambda: scrollright(num))
    btn_right.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
    btn_left = Button(master = displayed, text = '<', font = ("ariel", 50), command = lambda: scrollleft(num))
    btn_left.place(x = 0, y = 950)