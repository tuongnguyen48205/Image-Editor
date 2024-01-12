def transform():
    '''
    This function presents the options for the user to select which transformations
    they would like to apply for their chosen images
    '''
    global lbl_images_num
    global frm_transform
    global btn_transform
    global lbl_subtext
    global frm_selection
    global frm_placeholder

    # Transformations appear at the top after all the images have been chosen
    # TRANSFORM button appears at the bottom as well
    lbl_images_num.config(text = "\nChoose your transformations:")
    lbl_subtext.forget()
    frm_placeholder.pack()
    frm_transform.pack(side = BOTTOM, pady = 15)
    btn_transform.pack()

# These are used for the function below
lbl_threshold = Label(master = frm_upload, text = "Threshold value: ", 
                              fg = "black", font = ("arial", 11))
ent_threshold = Entry(master = frm_upload, font = ("arial", 11))
btn_verify2 = Button(master = frm_upload, text = "Verify", fg ="black",
                     font = ("arial", 11), command = lambda: verify2()) 
lbl_width = Label(master = frm_upload, text = "   Width multiplier: ", 
                              fg = "black", font = ("arial", 11))
ent_width = Entry(master = frm_upload, font = ("arial", 11))
lbl_height = Label(master = frm_upload, text = "   Height multiplier: ", 
                              fg = "black", font = ("arial", 11))
ent_height = Entry(master = frm_upload, font = ("arial", 11))
lbl_opacity = Label(master = frm_upload, text = "   Opacity percentage: ", 
                              fg = "black", font = ("arial", 11))
ent_opacity = Entry(master = frm_upload, font = ("arial", 11))