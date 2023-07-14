# Image Carousel

# pip install tk
# pip install pillow

import tkinter as tk
from PIL import ImageTk, Image

class ImageCarousel:
    def __init__(self, images):
        self.images = images
        self.current_image_index = 0

        self.root = tk.Tk()
        self.root.title("Image Carousel")

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.btn_prev = tk.Button(self.root, text="Previous", command=self.show_previous_image)
        self.btn_prev.pack(side=tk.LEFT)

        self.btn_next = tk.Button(self.root, text="Next", command=self.show_next_image)
        self.btn_next.pack(side=tk.RIGHT)

    def show_image(self):
        image_path = self.images[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((400, 400), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def show_previous_image(self):
        self.current_image_index -= 1
        if self.current_image_index < 0:
            self.current_image_index = len(self.images) - 1
        self.show_image()

    def show_next_image(self):
        self.current_image_index += 1
        if self.current_image_index >= len(self.images):
            self.current_image_index = 0
        self.show_image()

    def start(self):
        self.show_image()
        self.root.mainloop()

# Test the Image Carousel
image_paths = ["img1.png", "img2.png", "img3.png", "img4.png"]
carousel = ImageCarousel(image_paths)
carousel.start()
