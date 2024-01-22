import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

root = tk.Tk()  # Initialize the Tkinter environment

def get_image_color(event):
    # Get the RGB color of the pixel
    r, g, b = rgb_im.getpixel((event.x, event.y))
    print(f"RGB color: ({r}, {g}, {b})")

    # Update the color display
    color_display.config(bg=f'#{r:02x}{g:02x}{b:02x}')
    rgb_display.config(text=f"RGB color: ({r}, {g}, {b})")

# Ask for the image file location
image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])

# Open the image file
im = Image.open(image_path)
# Convert the image to RGB for color information
rgb_im = im.convert('RGB')
# Create a PhotoImage object for use in a Tkinter canvas
photo = ImageTk.PhotoImage(im)

# Create a canvas and display the image
canvas = tk.Canvas(root, width=im.width, height=im.height)
canvas.pack()
canvas.create_image(0, 0, image=photo, anchor=tk.NW)

# Bind the mouse motion event to the get_image_color function
canvas.bind('<Motion>', get_image_color)

# Create a new window for the color display
color_window = tk.Toplevel(root)
color_window.title("Color Display")

# Create a label to display the color
color_display = tk.Label(color_window, text="Color", width=20, height=10)
color_display.pack()

# Create a label to display the RGB values
rgb_display = tk.Label(color_window, text="RGB color: (0, 0, 0)")
rgb_display.pack()

root.mainloop()
