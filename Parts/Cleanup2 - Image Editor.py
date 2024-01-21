btn_viewimages = Button(master = frm_upload, text = "View images", font = ("Times", 15),
                        fg = "black", command = lambda:display_transformed(num_of_images))
btn_another = Button(master = frm_transform, text = "Transform again", font = ("Times", 15),
                        fg = "black", command = lambda:restart())

def cleanup2():
    '''
    Cleans up the screen a bit
    '''
    global lbl_images_num
    global num_of_images
    global frm_placeholder
    global frm_main_image_frame
    global frm_transform
    global lbl_threshold 
    global ent_threshold 
    global btn_verify2
    global lbl_width                         
    global ent_width 
    global lbl_height 
    global ent_height 
    global lbl_opacity
    global ent_opacity
    global frm_upload
    global btn_viewimages
    global btn_transform
    global btn_another
    
    if num_of_images == 1:
        lbl_images_num.config(text = "\nTransformation Complete!")
    else:
        lbl_images_num.config(text = "\nTransformations Complete!")
    
    frm_placeholder.forget()
    frm_main_image_frame.forget()
    lbl_threshold.forget()
    ent_threshold.forget() 
    btn_verify2.forget()
    lbl_width.forget()                         
    ent_width.forget() 
    lbl_height.forget() 
    ent_height.forget() 
    lbl_opacity.forget()
    ent_opacity.forget()
    btn_transform.forget()

    # add view transformation buttons
    # place transformed image icons below
    # Do another transformation button below

    frm_transform.config(borderwidth = 6)
    frm_upload.config(relief = RAISED)
    btn_viewimages.pack()
    btn_another.pack()

    place_transformed()

frm_main_transformed_images = Frame(master = window)