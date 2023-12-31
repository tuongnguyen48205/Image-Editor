def scrollright(num):
    '''
    Moves to the next image 
    '''
    global image_tracker
    global filename_tracker
    global sidetracker
    global lbl_imageinfo
    global lbl_displayed

    sidetracker += 1
    if sidetracker > num:
        sidetracker = 0
    # Place in the image resizing it appropriately to fit
    selected_img = image_tracker[sidetracker]
    width, height = selected_img.size
    while height > 850 or width > 3000:
        width = int(width/2)
        height = int(height/2)
    selected_img = selected_img.resize((width,height))
    selected_img = ImageTk.PhotoImage(selected_img)
    selected_img.image = selected_img
    lbl_displayed.config(image = selected_img)
    lbl_displayed.image = selected_img
    # Time to display the images info
    filepath_list = reversed(list(filename_tracker[sidetracker]))
    filename2 = []
    for i in filepath_list:
        if i == '/':
            break
        else:
            filename2.append(i)
    lbl_imageinfo.config(text = f"Filename: {''.join(reversed(filename2))}\nFilepath: {filename_tracker[sidetracker]}\nMode: {image_tracker[0].mode}\nWidth: {image_tracker[sidetracker].width}px\n Height: {image_tracker[sidetracker].height}px",
                          font = ("ariel", 17), fg = "black")

def scrollleft(num):
    '''
    Goes back to the previous image 
    '''
    global image_tracker
    global filename_tracker
    global sidetracker
    global lbl_imageinfo
    global lbl_displayed

    sidetracker -= 1
    if sidetracker < 0:
        sidetracker = num
    # Place in the image resizing it appropriately to fit
    selected_img = image_tracker[sidetracker]
    width, height = selected_img.size
    while height > 850 or width > 3000:
        width = int(width/2)
        height = int(height/2)
    selected_img = selected_img.resize((width,height))
    selected_img = ImageTk.PhotoImage(selected_img)
    selected_img.image = selected_img
    lbl_displayed.config(image = selected_img)
    lbl_displayed.image = selected_img
    # Time to display the images info
    filepath_list = reversed(list(filename_tracker[sidetracker]))
    filename2 = []
    for i in filepath_list:
        if i == '/':
            break
        else:
            filename2.append(i)
    lbl_imageinfo.config(text = f"Filename: {''.join(reversed(filename2))}\nFilepath: {filename_tracker[sidetracker]}\nMode: {image_tracker[0].mode}\nWidth: {image_tracker[sidetracker].width}px\n Height: {image_tracker[sidetracker].height}px",
                          font = ("ariel", 17), fg = "black")