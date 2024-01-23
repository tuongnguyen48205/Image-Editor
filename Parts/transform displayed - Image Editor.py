def display_transformed(number):
    '''
    displays the transformed image in its full size and a summary of its 
    information
    '''
    global transformed
    global image_tracker
    global filename_tracker
    global transform_sidetracker
    global transform_displayed
    global lbl_transform_imageinfo
    global lbl_transform_displayed
    global frm_download
    global btn_download
    
    transform_sidetracker = 0

    # Make a new window
    transform_displayed = Toplevel()
    transform_displayed.geometry("1920x1080")
    transform_displayed.resizable(False, False)
    # Place in the first image resizing it appropriately to fit
    transform_selected_img = transformed[0]
    width, height = transform_selected_img.size
    while height > 850 or width > 3000:
        width = int(width/2)
        height = int(height/2)
    transform_selected_img = transform_selected_img.resize((width,height))
    transform_selected_img = ImageTk.PhotoImage(transform_selected_img)
    transform_selected_img.image = transform_selected_img
    lbl_transform_displayed = Label(master = transform_displayed, image = transform_selected_img)
    lbl_transform_displayed.image = transform_selected_img
    lbl_transform_displayed.pack()
    # Time to display the images info
    lbl_transform_Imageinfo_title = Label(text = "\nImage Summary:", fg = "black", font = ("times", 23, "bold"),
                          master = transform_displayed)
    lbl_transform_Imageinfo_title.pack()
    filepath_list = reversed(list(filename_tracker[0]))
    filename2 = []
    for i in filepath_list:
        if i == '/':
            break
        else:
            filename2.append(i)
    lbl_transform_imageinfo = Label(text = f"Filename: {''.join(reversed(filename2))}(transformed)\nMode: {transformed[0].mode}\nWidth: {transformed[0].width}px\n Height: {transformed[0].height}px",
                          font = ("ariel", 17), master = transform_displayed, fg = "black")
    lbl_transform_imageinfo.pack()
    # Add the left and right navigation buttons
    btn_right = Button(master = transform_displayed, text = '>', font = ("ariel", 50), command = lambda: transform_scrollright())
    btn_right.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
    btn_left = Button(master = transform_displayed, text = '<', font = ("ariel", 50), command = lambda: transform_scrollleft())
    btn_left.place(x = 0, y = 950)

    # Add the download button
    frm_download = Frame(master = transform_displayed, relief = RAISED, borderwidth = 10)
    frm_download.pack(side = BOTTOM, pady = 15)
    btn_download = Button(master = frm_download, text = "Download",
                       fg="black", font = ("Times", 30), command = lambda:download(transform_sidetracker))
    btn_download.pack()