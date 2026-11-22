from itertools import cycle
from PIL import Image,ImageTk
import time
import tkinter as tk

root=tk.Tk()
root.title("Image Slideshow viewer")

#list of image path
image_paths=[
    r"D:\My phone backup\My Photoes sep to nov\IMG_20260901_203331.jpg",
    r"D:\My phone backup\My Photoes sep to nov\IMG_20260907_201924.jpg",
    r"D:\My phone backup\My Photoes sep to nov\IMG_20260920_114643.jpg",
    r"D:\My phone backup\My Photoes sep to nov\IMG_20261011_061327.jpg",
    r"D:\My phone backup\My Photoes sep to nov\IMG_20261103_163251.jpg",
]

#Resize the images to 1080x1080
image_size=(1080,1080)
images=[Image.open(path).resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label=tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow=cycle(photo_images)
def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

paly_button = tk.Button(root,text='paly slideshow',command=start_slideshow)
paly_button.pack()

root.mainloop()
