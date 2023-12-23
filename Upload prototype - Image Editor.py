# Create a frame and upload button and labels
lbl_images_num = Label(fg = "black", font = ("Times", 30))
frm_upload = Frame(master=window, relief = RAISED, borderwidth=5)
btn_upload = Button(master = frm_upload, text="Choose Image", fg="black", 
                    font = 20, command = lambda:upload_file())
frm_selection = Frame(master=window)
lbl_subtext = Label(master = frm_selection, text = "(One at a time)", 
                    fg = "black", font = ("Times", 20))
lbl_subtext.pack()

# Create a main frame
frm_main_image_frame = Frame(master = window)
column_tracker = 0
row_tracker = 0

# If the entered value is valid then proceed to the next steps    
def transition(images_num):
    '''
    Creates a label and transitions to the next step of the image
    editing process
    '''
    global lbl_images_num
    global num_of_images
    global lbl_subtext
    global frm_selection
    num_of_images = images_num
    # Create a label
    lbl_images_num.config(text = f"\nPlease upload {images_num} images:")
    lbl_images_num.pack()
    frm_selection.pack()

    # Insert choose image button
    global frm_main_image_frame
    frm_upload.pack(pady = 15)
    btn_upload.pack()
    frm_main_image_frame.pack()