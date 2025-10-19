import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def upload_image():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if file_path:
        img = Image.open(file_path)
        img = img.resize((400, 300), Image.Resampling.LANCZOS)

        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)
        label.image = photo  # keep a reference!

root = tk.Tk()
root.title("Basic Photo Frame App")

label = tk.Label(root)
label.pack(padx=10, pady=10)

btn = tk.Button(root, text="Upload Image", command=upload_image)
btn.pack(pady=10)

root.mainloop()
