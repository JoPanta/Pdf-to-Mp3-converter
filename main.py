import tkinter
import requests
from PyPDF2 import PdfReader
from gtts import gTTS
import tkinter as tk   # from tkinter import Tk for Python 3.x
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter.messagebox import showinfo

#
# print(extracted_text)
#


pdf_file = ""

window = tk.Tk()
window.title("PDF CONVERTER")
window.minsize(width=200, height=200)

def select_file():
    global pdf_file
    filetypes = (
        ('PDF files', '*.pdf'),
        ('All files', '*.*')
    )

    pdf_file = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    if pdf_file:
        pdf_path_var.config(text=pdf_file)


def convert_to_text():
    if pdf_file:
        reader = PdfReader(pdf_file)
        page = reader.pages[0]
        extracted_text = page.extract_text()
        output_path = fd.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        tts = gTTS(extracted_text)
        tts.save(f'{output_path}')
        if tts:
            success_label.config(text="Success!")




# open button
open_button = ttk.Button(
    window,
    text='Choose File',
    command=select_file
)

# convert button
convert_button = ttk.Button(
    window,
    text='Convert',
    command=convert_to_text
)

success_label = tk.Label(text="")
success_label.grid(column=0, row=4)
welcome_label = tk.Label(text="Choose a file to convert")
welcome_label.grid(column=0, row=0)
choose_file_label = tk.Label(text="Choose a file to convert")
open_button.grid(column=0, row=2)
convert_button.grid(column=0, row=3)
pdf_path_var = tk.Label(text="")
pdf_path_var.grid(column=0, row=1)


window.mainloop()