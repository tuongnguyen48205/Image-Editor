image_tracker = [] # Stores all the images that are uploaded
filename_tracker = [] # Stores all the image filenames used

def upload_file():
    '''
    Allows the user to upload images from their system in order
    to edit them
    '''
    global counter
    global num_of_images
    global btn_upload
    global frm_upload
    counter += 1 

    # The part where the user chooses an image
    global img
    global image_tracker
    f_types = [('Png Files','*.png'), ('Jpg Files', '*.jpg')]   # type of files to select 
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    image_tracker.append(ImageTk.getimage(img))
    filename_tracker.append(filename)

    # If there is only one image, it can be large so resize it so it fits while
    # maintaining the correct aspect ratio.
    global frm_main_image_frame
    if num_of_images == 1:
        img = ImageTk.getimage(img)
        width, height = img.size
        while height > 450 or width > 3000:
            width = int(width/2)
            height = int(height/2)
        img = img.resize((width,height))
        img = ImageTk.PhotoImage(img)
        frm_images = Frame(master = frm_main_image_frame, relief = RIDGE,
                    borderwidth = 12)
        frm_images.pack()
        lbl_image = Button(master = frm_images, image = img, command = lambda:display(counter - 1))
        lbl_image.pack()
    else:
        # Resize the images 
        img = ImageTk.getimage(img)
        width, height = img.size
        if (num_of_images == 2 or num_of_images == 3):
            img = img.resize((450, 450))
        elif (num_of_images == 4):
            img = img.resize((300, 300))
        elif (num_of_images == 5):
            img = img.resize((250, 250))
        else:
            img = img.resize((200, 200))

        img = ImageTk.PhotoImage(img)

        # Now to display the chosen images
        global column_tracker
        global row_tracker
    
        if column_tracker == 5:
            row_tracker += 1
            if column_tracker >= 5:
                column_tracker -= 5
        
        # Create a grid
        img.image = img # To keep the photos displayed
        frm_images = Frame(master = frm_main_image_frame, relief = RIDGE,
                    borderwidth = 12)
        frm_images.grid(row = row_tracker, column = column_tracker, padx = 40, pady = 20)
        lbl_newimage = Button(master = frm_images, image = img, command = lambda:display(counter - 1))
        lbl_newimage.image = img
        lbl_newimage.pack()

        column_tracker += 1

    # When the correct number of images have been uploaded, delete the upload
    # button so no more images may be uploaded
    if counter == num_of_images:
        btn_upload.forget()
        frm_upload.config(relief = FLAT, borderwidth = 6)
        transform()
