# General information buttons that are found in the help bar at the top of the page
frm_top = Frame(master=window, bg = "black")
frm_top.pack(fill=X)
for i in range(5):
    frm_helpbar = Frame(master=frm_top, relief=RAISED, 
                            borderwidth=5)
    frm_helpbar.grid(row=0, column=i)
    if (i == 0):
        btn_exit = Button(master = frm_helpbar, text = "Exit", bg = "red4",
                              fg = "white", command = lambda:exit())
        btn_exit.pack()
    if (i == 1):
        btn_restart = Button(master = frm_helpbar, text = "Restart", 
                            command = lambda:restart())
        btn_restart.pack()
    if (i == 2):
        btn_fullscreen = Button(master=frm_helpbar, text = "Fullscreen", 
                                command = lambda:fullscreen())
        btn_fullscreen.pack()
    if (i == 3):
        btn_info = Button(master=frm_helpbar, text = "Info", command = lambda:info())
        btn_info.pack()
    if (i == 4):
        btn_help = Button(master = frm_helpbar, text = "Help", command = lambda:webbrowser.open_new(r"https://github.com/tuongnguyen48205/Image-Editor/blob/main/README.md"))
        btn_help.pack()
        
                
def info():
    '''
    This function opens up a new window which shows all the information
    '''
    info = Tk()
    info.title("Information")
    lbl_info_title = Label(text = "Information\n",
                     fg = "black", master = info, font = ("Times", 25, "underline"))
    lbl_info = Label(text = "This Image Editor project was created by Tuong Bao Nguyen as a way to learn how to develop software,\n GUI interfaces. This application uses the popular tkinter already installed as part of the Python library.\n As such, this project was developed in the programming language of Python.",
                     fg = "black", master = info, font = ("Times", 15))
    lbl_info_title.pack()
    lbl_info.pack()
    return

def restart():
    '''
    This function restarts the program
    '''
    window.destroy()
    process = Process(target=task)
    process.start()
    process.join()
    process.start()

def task():
    sleep(1)

fullscreen_tracker = False # Keeps track of whether the window is in full screen or not
def fullscreen():
    '''
    Makes the window fullscreen
    '''
    global fullscreen_tracker
    if fullscreen_tracker == False: 
        window.attributes('-fullscreen', True)
        fullscreen_tracker = True
    elif fullscreen_tracker == True:
        window.attributes('-fullscreen', False)
        fullscreen_tracker = False

# Places in the buttons and other things at the top of the window
frm_padding = Frame(bg = "black")
frm_padding.pack(fill=X)
lbl_padding = Label(master = frm_padding, text = "", height = 2, bg = "black")
lbl_padding.pack()
lbl_title = Label(text = "Image Editor!", fg= "white", bg="black",
                width = 100, font = ("Times", 60, "bold"))
lbl_title.pack(fill=X)
frm_authorship = Frame(relief = FLAT, bg = "black")
frm_authorship.pack(fill=X)
btn_authorship = Button(master = frm_authorship, text = "By Tuong Bao Nguyen", height = 3,
                        bg = "black", fg = "white", border=FALSE, font = ('Times', 15),
                        activebackground = "black", activeforeground = "white",
                        command = lambda:webbrowser.open_new(r"https://github.com/tuongnguyen48205"))
btn_authorship.pack()
