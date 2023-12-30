# Ask the user how many images they would like to upload and edit
lbl_upload = Label(text = "\nHow many images would you like to upload:", fg = "black", 
               font = ("Times", 30))
lbl_tracker = Label(text = "Between 1 to 10 (inclusive). Press 'Okay' when ready.\n", 
                    fg = "black", font = ("Times", 20))
lbl_upload.pack()
lbl_tracker.pack()
ent_upload = Entry(font = 15)
ent_upload.pack()
frm_verify = Frame(master=window, relief = RAISED, borderwidth=5)
frm_verify.pack(pady=15)
btn_verify = Button(master=frm_verify, text="Okay", fg="black", font = 20,
                    command = lambda:verify_entry())
btn_verify.pack()
counter = 0 # Keeps track of how many images have been uploaded
num_of_images = 0

def verify_entry():
    '''
    Verifies that the number in the entry is in fact between 1 and 10 (inclusive).
    Returns the number if it is or gives an error message if it is not. returns None
    '''
    global ent_upload
    global btn_verify
    defaultbg = window.cget('bg')
    entry_data = ent_upload.get()

    # Determines whether or not the number of images the user wants to edit 
    # is valid or not
    if entry_data.isdigit() and 1 <= int(entry_data) <= 10:
        btn_verify.config(bg = "green")
        cleanup()
        transition(int(entry_data))
    # If it is not valid, then let the user know
    else:
        btn_verify.config(bg = "red")
        unknown_entry = Tk()
        unknown_entry.resizable(False, False)
        unknown_entry.title("Error!")
        lbl_error = Label(text = "Please type an integer number between 1 and 10 (inclusive).",
                fg = "black", master = unknown_entry, font = ("ariel", 15))
        lbl_error.pack()
        btn_verify.config(bg = defaultbg)

def cleanup():
    '''
    Has no arguments and returns None. It cleans up all the now
    unnecessary things on the window
    '''
    global btn_verify
    global frm_verify
    global ent_upload
    global lbl_tracker
    global lbl_upload
    btn_verify.forget()
    frm_verify.forget()
    ent_upload.forget()
    lbl_tracker.forget()
    lbl_upload.forget()
