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