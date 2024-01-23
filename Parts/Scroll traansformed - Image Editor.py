def transform_scrollright():
    '''
    Moves to the next image 
    '''
    global image_tracker
    global transformed
    global filename_tracker
    global transform_sidetracker
    global lbl_imageinfo
    global lbl_displayed
    global num_of_images

    transform_sidetracker += 1
    if transform_sidetracker >= num_of_images:
        transform_sidetracker = 0
    # Place in the image resizing it appropriately to fit
    transform_selected_img = transformed[transform_sidetracker]
    width, height = transform_selected_img.size
    while height > 850 or width > 3000:
        width = int(width/2)
        height = int(height/2)
    transform_selected_img = transform_selected_img.resize((width,height))
    transform_selected_img = ImageTk.PhotoImage(transform_selected_img)
    transform_selected_img.image = transform_selected_img
    lbl_transform_displayed.config(image = transform_selected_img)
    lbl_transform_displayed.image = transform_selected_img
    # Time to display the images info
    filepath_list = reversed(list(filename_tracker[transform_sidetracker]))
    filename2 = []
    for i in filepath_list:
        if i == '/':
            break
        else:
            filename2.append(i)
    lbl_transform_imageinfo.config(text = f"Filename: {''.join(reversed(filename2))}(transformed)\nMode: {transformed[transform_sidetracker].mode}\nWidth: {transformed[transform_sidetracker].width}px\n Height: {transformed[transform_sidetracker].height}px",
                          font = ("ariel", 17))

def transform_scrollleft():
    '''
    Moves to the next image 
    '''
    global image_tracker
    global transformed
    global filename_tracker
    global transform_sidetracker
    global lbl_imageinfo
    global lbl_displayed
    global num_of_images

    transform_sidetracker -= 1
    if transform_sidetracker < 0:
        transform_sidetracker = num_of_images - 1
    # Place in the image resizing it appropriately to fit
    transform_selected_img = transformed[transform_sidetracker]
    width, height = transform_selected_img.size
    while height > 850 or width > 3000:
        width = int(width/2)
        height = int(height/2)
    transform_selected_img = transform_selected_img.resize((width,height))
    transform_selected_img = ImageTk.PhotoImage(transform_selected_img)
    transform_selected_img.image = transform_selected_img
    lbl_transform_displayed.config(image = transform_selected_img)
    lbl_transform_displayed.image = transform_selected_img
    # Time to display the images info
    filepath_list = reversed(list(filename_tracker[transform_sidetracker]))
    filename2 = []
    for i in filepath_list:
        if i == '/':
            break
        else:
            filename2.append(i)
    lbl_transform_imageinfo.config(text = f"Filename: {''.join(reversed(filename2))} (transformed)\nMode: {transformed[transform_sidetracker].mode}\nWidth: {transformed[transform_sidetracker].width}px\n Height: {transformed[transform_sidetracker].height}px",
                          font = ("ariel", 17), fg = "black")
