def selection():
    '''
    This edits the list that keeps track of the transformations that need
    to be done by noting whether a transformation box has been ticked or not
    '''
    global transformation
    global frm_upload
    global lbl_threshold
    global ent_threshold
    global btn_verify2
    global lbl_height
    global lbl_width
    global ent_height
    global ent_width
    global lbl_opacity
    global ent_opacity
    if inverse.get() == 1:  
        transformation[0] = 1
    if inverse.get() == 0:
        transformation[0] = 0
    if threshold.get() == 1:  
        transformation[1][0] = 1
        # Make sure that the enter threshold entry is always on the left side
        # and the height and width multipliers are always on the right side
        if opacity.get() == 1 and pinch.get() == 1:
            lbl_width.forget()
            ent_width.forget()
            lbl_height.forget()
            ent_height.forget()
            lbl_opacity.forget()
            ent_opacity.forget()
            lbl_threshold.pack(side = LEFT)
            ent_threshold.pack(side = LEFT)
            lbl_width.pack(side = LEFT)
            ent_width.pack(side = LEFT)
            lbl_height.pack(side = LEFT)
            ent_height.pack(side = LEFT)
            lbl_opacity.pack(side = LEFT)
            ent_opacity.pack(side = LEFT)
        elif opacity.get() == 1 and pinch.get() == 0:
            lbl_opacity.forget()
            ent_opacity.forget()
            lbl_threshold.pack(side = LEFT)
            ent_threshold.pack(side = LEFT)
            lbl_opacity.pack(side = LEFT)
            ent_opacity.pack(side = LEFT)
        elif opacity.get() == 0 and pinch.get() == 1:
            lbl_width.forget()
            ent_width.forget()
            lbl_height.forget()
            ent_height.forget()
            lbl_threshold.pack(side = LEFT)
            ent_threshold.pack(side = LEFT)
            lbl_width.pack(side = LEFT)
            ent_width.pack(side = LEFT)
            lbl_height.pack(side = LEFT)
            ent_height.pack(side = LEFT)
        else:
            lbl_threshold.pack(side = LEFT)
            ent_threshold.pack(side = LEFT)
    if threshold.get() == 0:  
        transformation[1][0] = 0
        lbl_threshold.forget()
        ent_threshold.forget()
    if greyscale.get() == 1:
        transformation[2] = 1
    if greyscale.get() == 0:
        transformation[2] = 0
    if flipx.get() == 1:
        transformation[3] = 1
    if flipx.get() == 0:
        transformation[3] = 0
    if flipy.get() == 1:
        transformation[4] = 1
    if flipy.get() == 0:
        transformation[4] = 0
    if rotater.get() == 1:
        transformation[5] = 1
    if rotater.get() == 0:
        transformation[5] = 0
    if rotatel.get() == 1:
        transformation[6] = 1
    if rotatel.get() == 0:
        transformation[6] = 0
    if pinch.get() == 1:
        transformation[7][0] = 1
        # Always keep pinch and zoom in the middle
        if opacity.get() == 1:
            lbl_opacity.forget()
            ent_opacity.forget()
            lbl_width.pack(side = LEFT)
            ent_width.pack(side = LEFT)
            lbl_height.pack(side = LEFT)
            ent_height.pack(side = LEFT)
            lbl_opacity.pack(side = LEFT)
            ent_opacity.pack(side = LEFT)
        else:
            lbl_width.pack(side = LEFT)
            ent_width.pack(side = LEFT)
            lbl_height.pack(side = LEFT)
            ent_height.pack(side = LEFT)
    if pinch.get() == 0:
        transformation[7][0] = 0
        lbl_width.forget()
        ent_width.forget()
        lbl_height.forget()
        ent_height.forget()
    if opacity.get() == 1:
        transformation[8][0] = 1
        lbl_opacity.pack(side = LEFT)
        ent_opacity.pack(side = LEFT)
    if opacity.get() == 0:
        transformation[8][0] = 0
        lbl_opacity.forget()
        ent_opacity.forget()
    # Always keep the verify button on the right
    if threshold.get() == 0 and pinch.get() == 0 and opacity.get() == 0:
        btn_verify2.forget()
    if threshold.get() == 1 or pinch.get() == 1 or opacity.get() == 1:
        btn_verify2.forget()
        btn_verify2.pack(side = LEFT, padx = 25)

transformation_calling = False # Lets the function verify2 know whether the
# do transformation function is calling it or not
tranformation_verified = False # Verifies if the transformation can go through
# or not