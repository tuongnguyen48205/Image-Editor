def verify2():
    '''
    When the user clicks the verify button, this function is called. The user
    does not need to click the verify button. This function verifies that the
    numbers that the user has chosen are indeed valid.
    '''
    global transformation
    global ent_width
    global ent_height
    global ent_threshold
    global ent_opacity

    # The following is responsible for determining whether the transformation
    # is valid or not
    passed = True
    if transformation[1][0] == 1:
        thresholdval = ent_threshold.get()
        if thresholdval.isdigit() == False:
            passed = False
        else:
            transformation[1][1] = int(thresholdval)
    if transformation[7][0] == 1:
        widthval = ent_width.get()
        heightval = ent_height.get()
        if widthval == '':
            widthval = '1'
        if heightval == '':
            heightval = '1'
        if widthval.isdigit() == False or heightval.isdigit() == False:
            passed = False
        elif int(widthval) <= 0 or int(heightval) <= 0:
            passed = False
        else:
            transformation[7][1] = int(widthval)
            transformation[7][2] = int(heightval)
    if transformation[8][0] == 1:
        opacityval = ent_opacity.get()
        if opacityval.isdigit() == False:
            passed = False
        elif int(opacityval) < 0 or int(opacityval) > 100:
            passed = False
        else:
            transformation[8][1] = int(opacityval)

    global tranformation_verified
    # This means that the transformation is not valid
    if passed == False:
        tranformation_verified = False
        unverified = Tk()
        unverified.resizable(False, False)
        unverified.title("Invalid values")
        lbl_unverified_title = Label(master = unverified, text = "Invalid Values!",
                                     font = ("Times", 19, "bold"), bg = "red")
        lbl_unverified_title.pack(fill = X)
        lbl_unverified = Label(master = unverified, text = "This transformation cannot be done since the values you have\n entered are not supported. For 'threshold value', please ensure the\n value entered is an integer. For the 'width multiplier' and 'height multiplier', \nplease ensure that the values are non-zero positive integers.\n If they are left blank, they default to the value 1. For the 'opacity percentage', please\ninput an integer value between 0 and 100 (inclusive).",
                               font = ("ariel", 15))
        lbl_unverified.pack()
        pass
    else:
        # determine if it is called by the transform button or not
        if transformation_calling == True:
            tranformation_verified = True
        else:
            verified = Tk()
            verified.resizable(False, False)
            verified.title("Values verified!")
            lbl_verified_title = Label(master = verified, text = "Valid!",
                                     font = ("Times", 19, "bold"), bg = "green")
            lbl_verified_title.pack(fill = X)
            lbl_verified = Label(master = verified, text = "The values you have chosen are valid. This transformation is possible!",
                               font = ("Times", 15))
            lbl_verified.pack()

transformed = [] # Contains all the images after they've been transformed