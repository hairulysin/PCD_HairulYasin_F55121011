# Nama : Hairul Yasin
# NIM : F551121011

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

def smoothing(img):
    smoothed_img = cv2.GaussianBlur(img, (5, 5), 0)
    return smoothed_img

def grayscale(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_img

def sharpening(img):
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharp_img = cv2.filter2D(img, -1, kernel)
    return sharp_img

# fungsi untuk menampilkan gambar dalam kotak
def show_image(img, x, y, title):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=img)
    label.image = img
    label.place(x=x, y=y)
    title_label = tk.Label(root, text=title)
    title_label.place(x=x, y=y-20)

# fungsi untuk memproses citra dan menampilkan hasilnya
def process_image(method):
    global original_img
    if method == 'smoothing':
        corrected_img = smoothing(original_img)
        show_image(corrected_img, 350, 200, '           Metode 1')
        draw_box(corrected_img, 350, 200)
    elif method == 'grayscale':
        corrected_img = grayscale(original_img)
        show_image(corrected_img, 630, 200, '           Metode 2')
        draw_box(corrected_img, 630, 200)
    elif method == 'sharpening' :
        corrected_img = sharpening(original_img)
        show_image(corrected_img, 910, 200, '           Metode 3')
        draw_box(corrected_img, 910, 200)

# fungsi untuk menggambar kotak pada gambar
def draw_box(img, x, y):
    img_copy = img.copy()
    cv2.rectangle(img_copy, (0, 0), (img_copy.shape[1], img_copy.shape[0]), (0, 0, 255), 2)
    show_image(img_copy, x, y, 'Hasil')

# fungsi untuk menampilkan informasi pembuat program
def show_creator():
    creator_label = tk.Label(root, text='Nama : Hairul Yasin  |  NIM : F55121011  |  Kelas : A')
    creator_label.place(x=510, y=650)

# fungsi untuk membuka gambar
def open_image():
    global original_img
    file_path = filedialog.askopenfilename()
    if file_path:
        original_img = cv2.imread(file_path)
        original_img = cv2.resize(original_img, (250, 300))
        show_image(original_img, 70, 200, 'Gambar Original')
        size_label.config(text='Dimensi: {} x {}'.format(original_img.shape[1], original_img.shape[0]))

# membuat jendela utama
root = tk.Tk()
root.geometry('1400x1000')
root.title('GUI Aplikasi Penerapan Perbaikan Citra')

# menambahkan judul gambar original
title_label = tk.Label(root, text='Gambar Original')
title_label.place(x=100, y=20)

# menambahkan tombol untuk membuka gambar
open_button = tk.Button(root, text='Buka Gambar', command=open_image)
open_button.place(x=100, y=50)

# menambahkan label untuk menampilkan dimensi gambar
size_label = tk.Label(root, text='Dimensi : -')
size_label.place(x=200, y=50)

# menambahkan kotak untuk perbaikan citra
correction_box = tk.LabelFrame(root, text='Metode Perbaikan Citra', padx=5, pady=5)
correction_box.place(x=500, y=25, width=250, height=70)

# tombol untuk perbaikan metode 1 (brigghtness)
smoothing_button = tk.Button(correction_box, text='Smoothing', command=lambda: process_image('smoothing'))
smoothing_button.pack(side=tk.LEFT, padx=5)

# tombol untuk perbaikan metode 2 (grayscalling)
smoothing_button = tk.Button(correction_box, text='Grayscaling', command=lambda: process_image('grayscale'))
smoothing_button.pack(side=tk.LEFT, padx=5)

# tombol untuk perbaikan metode 3 (sharpening)
sharpening_button = tk.Button(correction_box, text='Sharpening', command=lambda: process_image('sharpening'))
sharpening_button.pack(side=tk.LEFT, padx=5)

# menambahkan kotak untuk informasi pembuat program
creator_box = tk.LabelFrame(root, text='Dibuat Oleh :', padx=5, pady=5)
creator_box.place(x=450, y=620, width=400, height=70)

# menampilkan informasi pembuat program
show_creator()

# menjalankan program
root.mainloop()

