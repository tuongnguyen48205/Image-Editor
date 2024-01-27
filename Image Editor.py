# Image Editor
# Created by Tuong Bao Nguyen

# Import required libraries
from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import webbrowser
from time import sleep
from multiprocessing import Process

# Create instance of tkinter window and the labels found on the window (title, etc.)
window = Tk()
window.geometry("1920x1080")
window.title("Image Editor")

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

sidetracker = 0 # Tracks the current image
displayed = 'placeholder'
lbl_imageinfo = 'placeholder'
lbl_displayed = 'placeholder'


def display(num):
    '''
    displays the image in its full size and a summary of its 
    information
    '''
    global image_tracker
    global filename_tracker
    global sidetracker
    global displayed
    global lbl_imageinfo
    global lbl_displayed
    sidetracker = 0
    # Make a new window
    displayed = Toplevel()
    displayed.geometry("1920x1080")
    displayed.resizable(False, False)
    # Place in the first image resizing it appropriately to fit
    selected_img = image_tracker[0]
    width, height = selected_img.size
    while height > 850 or width > 3000:
        width = int(width/2)
        height = int(height/2)
    selected_img = selected_img.resize((width,height))
    selected_img = ImageTk.PhotoImage(selected_img)
    selected_img.image = selected_img
    lbl_displayed = Label(master = displayed, image = selected_img)
    lbl_displayed.image = selected_img
    lbl_displayed.pack()
    # Time to display the images info
    lbl_Imageinfo_title = Label(text = "\nImage Summary:", fg = "black", font = ("times", 23, "bold"),
                          master = displayed)
    lbl_Imageinfo_title.pack()
    filepath_list = reversed(list(filename_tracker[0]))
    filename2 = []
    for i in filepath_list:
        if i == '/':
            break
        else:
            filename2.append(i)
    lbl_imageinfo = Label(text = f"Filename: {''.join(reversed(filename2))}\nFilepath: {filename_tracker[0]}\nMode: {image_tracker[0].mode}\nWidth: {image_tracker[0].width}px\n Height: {image_tracker[0].height}px",
                          font = ("ariel", 17), master = displayed, fg = "black")
    lbl_imageinfo.pack()
    # Add the left and right navigation buttons
    btn_right = Button(master = displayed, text = '>', font = ("ariel", 50), command = lambda: scrollright(num))
    btn_right.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
    btn_left = Button(master = displayed, text = '<', font = ("ariel", 50), command = lambda: scrollleft(num))
    btn_left.place(x = 0, y = 950)

def scrollright(num):
    '''
    Moves to the next image 
    '''
    global image_tracker
    global filename_tracker
    global sidetracker
    global lbl_imageinfo
    global lbl_displayed

    sidetracker += 1
    if sidetracker > num:
        sidetracker = 0
    # Place in the image resizing it appropriately to fit
    selected_img = image_tracker[sidetracker]
    width, height = selected_img.size
    while height > 850 or width > 3000:
        width = int(width/2)
        height = int(height/2)
    selected_img = selected_img.resize((width,height))
    selected_img = ImageTk.PhotoImage(selected_img)
    selected_img.image = selected_img
    lbl_displayed.config(image = selected_img)
    lbl_displayed.image = selected_img
    # Time to display the images info
    filepath_list = reversed(list(filename_tracker[sidetracker]))
    filename2 = []
    for i in filepath_list:
        if i == '/':
            break
        else:
            filename2.append(i)
    lbl_imageinfo.config(text = f"Filename: {''.join(reversed(filename2))}\nFilepath: {filename_tracker[sidetracker]}\nMode: {image_tracker[0].mode}\nWidth: {image_tracker[sidetracker].width}px\n Height: {image_tracker[sidetracker].height}px",
                          font = ("ariel", 17), fg = "black")

def scrollleft(num):
    '''
    Goes back to the previous image 
    '''
    global image_tracker
    global filename_tracker
    global sidetracker
    global lbl_imageinfo
    global lbl_displayed

    sidetracker -= 1
    if sidetracker < 0:
        sidetracker = num
    # Place in the image resizing it appropriately to fit
    selected_img = image_tracker[sidetracker]
    width, height = selected_img.size
    while height > 850 or width > 3000:
        width = int(width/2)
        height = int(height/2)
    selected_img = selected_img.resize((width,height))
    selected_img = ImageTk.PhotoImage(selected_img)
    selected_img.image = selected_img
    lbl_displayed.config(image = selected_img)
    lbl_displayed.image = selected_img
    # Time to display the images info
    filepath_list = reversed(list(filename_tracker[sidetracker]))
    filename2 = []
    for i in filepath_list:
        if i == '/':
            break
        else:
            filename2.append(i)
    lbl_imageinfo.config(text = f"Filename: {''.join(reversed(filename2))}\nFilepath: {filename_tracker[sidetracker]}\nMode: {image_tracker[0].mode}\nWidth: {image_tracker[sidetracker].width}px\n Height: {image_tracker[sidetracker].height}px",
                          font = ("ariel", 17), fg = "black")

# Create a new frame and transformation button
frm_transform = Frame(master = window, relief = RAISED, borderwidth = 10)
btn_transform = Button(master = frm_transform, text = "Transform",
                       fg="black", font = ("Times", 30), command = lambda:do_transform())

# The following two functions are to change the colour of the transformation
# button when the mouse hovers over it
def on_enter(e):
    btn_transform['background'] = 'black'
    btn_transform['foreground'] = 'white'

def on_leave(e):
    btn_transform['background'] = 'SystemButtonFace'
    btn_transform['foreground'] = 'black'

btn_transform.bind("<Enter>", on_enter)
btn_transform.bind("<Leave>", on_leave)

transformation = [0, [0, 1], 0, 0, 0, 0, 0, [0, 1, 1], [0, 1]] # Representing the respective transformations
inverse = IntVar()
threshold = IntVar()
greyscale = IntVar()
flipx = IntVar()
flipy = IntVar()
pinch = IntVar()
rotater = IntVar()
rotatel = IntVar()
opacity = IntVar()

frm_placeholder = Frame(master = frm_selection)

# Place in the transformation options
for i in range(9):
    frm_innerselection = Frame(master = frm_placeholder)
    frm_innerselection.grid(row = 0, column = i, padx = 10)
    if i == 0:
        cbtn_inverse = Checkbutton(master = frm_innerselection, text = "Inverse", 
                                   variable = inverse, onvalue = 1, offvalue = 0,
                                   font = ("arial", 15), command = lambda:selection())
        cbtn_inverse.pack()
    if i == 1:
        cbtn_threshold = Checkbutton(master = frm_innerselection, text = "Threshold",
                                    variable = threshold, onvalue = 1, offvalue = 0,
                                    font = ("arial", 15), command = lambda:selection())
        cbtn_threshold.pack()
    if i == 2:
        cbtn_greyscale = Checkbutton(master = frm_innerselection, text = "Greyscale", 
                                   variable = greyscale, onvalue = 1, offvalue = 0,
                                   font = ("arial", 15), command = lambda:selection())
        cbtn_greyscale.pack()
    if i == 3:
        cbtn_flipx = Checkbutton(master = frm_innerselection, text = "Flip x", 
                                 variable = flipx, onvalue = 1, offvalue = 0,
                                font = ("arial", 15), command = lambda:selection())
        cbtn_flipx.pack()
    if i == 4:
        cbtn_flipy = Checkbutton(master = frm_innerselection, text= "Flip y", 
                                 variable = flipy, onvalue = 1, offvalue = 0,
                                font = ("arial", 15), command = lambda:selection())
        cbtn_flipy.pack()
    if i == 5:
        cbtn_rotater = Checkbutton(master = frm_innerselection, text= "Rotate Right", 
                                 variable = rotater, onvalue = 1, offvalue = 0,
                                font = ("arial", 15), command = lambda:selection())
        cbtn_rotater.pack()
    if i == 6:
        cbtn_rotatel = Checkbutton(master = frm_innerselection, text= "Rotate Left", 
                                 variable = rotatel, onvalue = 1, offvalue = 0,
                                font = ("arial", 15), command = lambda:selection())
        cbtn_rotatel.pack()
    if i == 7:
        cbtn_pinch = Checkbutton(master = frm_innerselection, text = "Pinch and Zoom", 
                                 variable = pinch, onvalue = 1, offvalue = 0,
                                font = ("arial", 15), command = lambda:selection())
        cbtn_pinch.pack()
    if i == 8:
        cbtn_opacity = Checkbutton(master = frm_innerselection, text = "Opacity percentage", 
                                 variable = opacity, onvalue = 1, offvalue = 0,
                                font = ("arial", 15), command = lambda:selection())
        cbtn_opacity.pack()

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

def do_transform():
    '''
    this function is responsible for doing the actual transformation
    '''
    global transformation
    global image_tracker
    global transformed 

    # Verify that the transformation is valid one more time
    # since the user does not need to click the verify button
    global transformation_calling
    global tranformation_verified
    transformation_calling = True
    verify2()
    transformation_calling = False
    # The following returns the function if the transformation 
    # cannot be done
    if tranformation_verified == False:
        return
    else:
        pass

    # Complete transformation for each image
    for image in image_tracker:
        # For the inverse transformation
        if transformation[0] == 1:
            for x in range(image.width):
                for y in range(image.height):
                    old_colour = image.getpixel((x, y))
                    new_colour = (255 - old_colour[0], 255 - old_colour[1], 
                                  255 - old_colour[2], old_colour[3])
                    image.putpixel((x, y), new_colour)
        # For the threshold transformation
        if transformation[1][0] == 1:
            threshold_val = transformation[1][1]
            threshold_list = []
            for x in range(image.width):
                for y in range(image.height):
                    old_colour = image.getpixel((x, y))
                    for i in range(3):
                        if old_colour[i] >= threshold_val:
                            threshold_list.append(255)
                        else:
                            threshold_list.append(0)
                    threshold_list.append(old_colour[3])
                    image.putpixel((x, y), tuple(threshold_list))
                    threshold_list = []
        # For the average transformation (greyscale)
        if transformation[2] == 1:
            for x in range(image.width):
                for y in range(image.height):
                    r, g, b, a = image.getpixel((x, y))
                    avg_val = int((r + g + b) / 3)
                    image.putpixel((x, y), (avg_val, avg_val, avg_val, a))
        # For flipping in the x direction
        if transformation[3] == 1:
            new_image = Image.new("RGBA", image.size)
            for x in range(image.width):
                for y in range(image.height):
                    pixel = image.getpixel((x, y))
                    new_image.putpixel((new_image.width - 1 - x, y), pixel)
            image = new_image
        # For flipping in the y direction
        if transformation[4] == 1:
            new_image = Image.new("RGBA", image.size)
            for x in range(image.width):
                for y in range(image.height):
                    pixel = image.getpixel((x, y))
                    new_image.putpixel((x, new_image.height - 1 - y), pixel)
            image = new_image
        # For rotation in the clockwise direction
        if transformation[5] == 1:
            new_image = Image.new("RGBA", (image.height, image.width))
            for x in range(image.width):
                for y in range(image.height):
                    pixel = image.getpixel((x, y))
                    new_image.putpixel((new_image.width - 1 - y, x), pixel)
            image.resize((image.height, image.width))
            image = new_image
        # For rotation in the anticlockwise direction
        if transformation[6] == 1:
            new_image = Image.new("RGBA", (image.height, image.width))
            for x in range(image.width):
                for y in range(image.height):
                    pixel = image.getpixel((x, y))
                    new_image.putpixel((y, new_image.height -1 - x), pixel)
            image.resize((image.height, image.width))
            image = new_image
        # For pinch and zoom
        if transformation[7][0] == 1:
            width = transformation[7][1]
            height = transformation[7][2]
            new_image = Image.new("RGBA", (image.width * width, image.height * height))
            counter3 = -1 * height
            for y in range(image.height):
                counter3 += height
                counter = -1
                for x in range(image.width):
                    pixel = image.getpixel((x, y))
                    for x2 in range(width):
                        counter += 1
                        counter2 = -1
                        for y2 in range(height):
                            counter2 += 1
                            new_image.putpixel((counter, counter3 + counter2), pixel)
            image.resize((image.width * width, image.height * height))
            image = new_image
        # For opacity change
        if transformation[8][0] == 1:
             opacity_percentage = transformation[8][1]
             for x in range(image.width):
                for y in range(image.height):
                    old_opacity = image.getpixel((x, y))
                    new_opacity = (old_opacity[0], old_opacity[1],
                                   old_opacity[2], int(old_opacity[3] * (opacity_percentage / 100)))
                    image.putpixel((x, y), new_opacity)
        # make list for outputs
        transformed.append(image)

    # Clean up the window a little
    cleanup2()

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

def display_transformed(number):
    '''
    displays the transformed image in its full size and a summary of its 
    information
    '''
    global transformed
    global image_tracker
    global filename_tracker
    global transform_sidetracker
    global transform_displayed
    global lbl_transform_imageinfo
    global lbl_transform_displayed
    global frm_download
    global btn_download
    
    transform_sidetracker = 0

    # Make a new window
    transform_displayed = Toplevel()
    transform_displayed.geometry("1920x1080")
    transform_displayed.resizable(False, False)
    # Place in the first image resizing it appropriately to fit
    transform_selected_img = transformed[0]
    width, height = transform_selected_img.size
    while height > 850 or width > 3000:
        width = int(width/2)
        height = int(height/2)
    transform_selected_img = transform_selected_img.resize((width,height))
    transform_selected_img = ImageTk.PhotoImage(transform_selected_img)
    transform_selected_img.image = transform_selected_img
    lbl_transform_displayed = Label(master = transform_displayed, image = transform_selected_img)
    lbl_transform_displayed.image = transform_selected_img
    lbl_transform_displayed.pack()
    # Time to display the images info
    lbl_transform_Imageinfo_title = Label(text = "\nImage Summary:", fg = "black", font = ("times", 23, "bold"),
                          master = transform_displayed)
    lbl_transform_Imageinfo_title.pack()
    filepath_list = reversed(list(filename_tracker[0]))
    filename2 = []
    for i in filepath_list:
        if i == '/':
            break
        else:
            filename2.append(i)
    lbl_transform_imageinfo = Label(text = f"Filename: {''.join(reversed(filename2))}(transformed)\nMode: {transformed[0].mode}\nWidth: {transformed[0].width}px\n Height: {transformed[0].height}px",
                          font = ("ariel", 17), master = transform_displayed, fg = "black")
    lbl_transform_imageinfo.pack()
    # Add the left and right navigation buttons
    btn_right = Button(master = transform_displayed, text = '>', font = ("ariel", 50), command = lambda: transform_scrollright())
    btn_right.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
    btn_left = Button(master = transform_displayed, text = '<', font = ("ariel", 50), command = lambda: transform_scrollleft())
    btn_left.place(x = 0, y = 950)

    # Add the download button
    frm_download = Frame(master = transform_displayed, relief = RAISED, borderwidth = 10)
    frm_download.pack(side = BOTTOM, pady = 15)
    btn_download = Button(master = frm_download, text = "Download",
                       fg="black", font = ("Times", 30), command = lambda:download(transform_sidetracker))
    btn_download.pack()

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

def download(num):
    '''
    Downloads the selected image
    '''
    global transformed
    global filepath_list
    filepath_list = reversed(list(filename_tracker[num]))
    filename2 = []
    for i in filepath_list:
        if i == '/':
            break
        else:
            filename2.append(i)
    transformed[num].save(f"{''.join(reversed(filename2))} (transformed).png")
    return

window.resizable(False,False)
window.mainloop()

