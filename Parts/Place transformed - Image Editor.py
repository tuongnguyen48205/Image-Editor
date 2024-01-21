def place_transformed():
    '''
    Display the transformed images
    '''
    global transformed
    global num_of_images
    global frm_main_transformed_images

    frm_main_transformed_images.pack()
    
    column_tracker2 = 0
    row_tracker2 = 0

    for img in transformed:
        if num_of_images == 1:
            width, height = img.size
            while height > 450 or width > 3000:
                width = int(width/2)
                height = int(height/2)
            img = img.resize((width,height))
            img = ImageTk.PhotoImage(img)
            img.image = img
            frm_transformed_images = Frame(master = frm_main_transformed_images, relief = RIDGE,
                        borderwidth = 12)
            frm_transformed_images.pack()
            lbl_image = Button(master = frm_transformed_images, image = img, command = lambda:display_transformed(num_of_images))
            lbl_image.image = img
            lbl_image.pack()
        else:
            # Resize the images 
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

            if column_tracker2 == 5:
                row_tracker2 += 1
                if column_tracker2 >= 5:
                    column_tracker2 -= 5
            
            # Create a grid
            img.image = img # To keep the photos displayed
            frm_transformed_images = Frame(master = frm_main_transformed_images, relief = RIDGE,
                        borderwidth = 12)
            frm_transformed_images.grid(row = row_tracker2, column = column_tracker2, padx = 40, pady = 20)
            lbl_newimage = Button(master = frm_transformed_images, image = img, command = lambda:display_transformed(num_of_images))
            lbl_newimage.image = img
            lbl_newimage.pack()

            column_tracker2 += 1

transform_sidetracker = 0 # Keeps track of what image is currently displayed
transform_displayed = 'placeholder'
lbl_transform_imageinfo = 'placeholder'
lbl_transform_displayed = 'placeholder'
frm_download = 'placeholder'
btn_download = 'placeholder'