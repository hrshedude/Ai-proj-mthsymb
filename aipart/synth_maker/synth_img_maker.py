import tkinter as tk
from tkinter import font as tkfont

from PIL import ImageGrab

import os
import random



def prob(probp:int,x, fallback):
    
    flip = random.randint(1,100)

    if probp > flip:
        return x
    else:
        return fallback

def rndc(x): 
    """return random.choice(x)"""
    
    return random.choice(x)

def rndcs(x):
    """
    return str(random.choice(x))
    """
    return str(random.choice(x))

    
    flip = random.randint(0,101)

    if probp >= flip:
        return x
    else:
        return fallback

def fake_eq():
    da = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    dn = "1234567890" *7
    do = "+-/*"
    dso = "^"

    rr = lambda fn: [f() for f in [fn]*random.randint(1,3)]
    rc = lambda: rndc(rndc([da,dn]))

    ftxt_ = lambda: [rr(rc)] +  [dso]+[rc()]  + [rndc(do)] + [rr(rc)]
        
    txt_ = ftxt_() + prob(50, [rndc(do)]+ftxt_(),[])  +prob(20,[rndc(do)]  +ftxt_(), [])

    txt = str(txt_).replace("[","").replace("]","").replace('"','').replace("'","").replace(",","").replace(" ","")

    return txt

def save_as_image(fn):
    # Get the window coordinates
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    width = root.winfo_width()
    height = root.winfo_height()
    
    # Capture the window content
    image = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    
    # Save the image
    with open(f"C:/Users/alima/OneDrive/Documents/GitHub/Ai-proj-mthsymb/aipart/imgset_synth/{fn}", "wb") as f:
        image.save(f)

# Create the main application window
root = tk.Tk()
root.title("E> uwu <3")


# Define custom fonts
main_font = tkfont.Font(family="Helvetica", size=20, weight="bold")
subscript_font = tkfont.Font(family="Helvetica", size=12)
superscript_font = tkfont.Font(family="Helvetica", size=12)


# Create a frame to hold the text
main_frame = tk.Frame(root, bg="white")
main_frame.pack(padx=5, pady=5)

def txt2grid(txt): # Known Problem: can only take 1 following symbol as superscript

    txt_ls = []
    txt_ls_wrd =[]
    just_before=False

    for s in txt:

        if just_before == True:
            txt_ls.append(s)
            just_before = False

        elif s == "^":
            txt_ls.append(txt_ls_wrd)
            txt_ls_wrd=[]
            txt_ls.append(s)
            just_before=True
        else:
            txt_ls_wrd.append(s)
    if len(txt_ls_wrd)>0:txt_ls.append(txt_ls_wrd)
    print(txt_ls)

    column_no = 0
    for sno,part in enumerate(txt_ls):
        
        if type(part) == type([]):
            
            if sno!=0 and type(txt_ls[sno-1]) == type(" "):
                column_no += 1
            else:
                pass

            label = tk.Label(main_frame, text="".join(part), font=main_font, fg="black", bg="white")
            label.grid(row=0, column=column_no)
        
        elif type(part) == type(" "):
            
            if part =="^":                              # <<--------- Change part for adding other super script stuff
                pass # probaly could use continue

            else:
                column_no += 1
                
                superscript_label = tk.Label(main_frame, text="".join(part), font=superscript_font, fg="black", bg="white")
                superscript_label.grid(row=0, column=column_no, sticky='nw')#, padx=(0, 0))


n = 10

for i in range(n):

    txt2grid(fake_eq())
    save_as_image(f"../imgset_eq_synth/img{i}.jpg")
    
    # clear screen
    for widget in main_frame.winfo_children():
        widget.destroy()


# save_button = tk.Button(root, text="Save as Image", command=lambda: save_as_image("tri.jpg"))
# save_button.pack(pady=10)




# Run the application
root.mainloop()




