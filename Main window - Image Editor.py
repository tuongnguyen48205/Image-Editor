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