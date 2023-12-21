from PyPDF2 import PdfReader
from gtts import gTTS
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter.messagebox import showinfo


pdf_file = ""

window = tk.Tk()
window.title("PDF CONVERTER")
window.minsize(width=500, height=300)
window.config(background="black")


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
        open_button.config(text="Convert", command=convert_to_text)
        success_label.config(text="Waiting...")


def convert_to_text():
    if pdf_file:
        try:
            reader = PdfReader(pdf_file)
            page = reader.pages[0]
            extracted_text = page.extract_text()
            output_path = fd.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
            tts = gTTS(extracted_text)
            tts.save(f'{output_path}')
            showinfo("Conversion Successful", "PDF successfully converted to MP3!")
            success_label.config(text="Converted!")
            open_button.config(text='Choose File', command=select_file)
            pdf_path_var.config(text="")
        except Exception as e:
            showinfo("Conversion Error", f"An error occurred during conversion:\n{str(e)}")
            success_label.config(text="Error!")



welcome_label = tk.Label(text="Welcome to PDF-to-MP3 Converter!")
welcome_label.grid(column=0, row=0, pady=10)
welcome_label.config(font=("Courier", 24), fg="white", background="black")

choose_file_label = tk.Label(text="Choose a file to convert", fg="white", background="black", font=("Courier", 14))
choose_file_label.grid(column=0, row=1)


pdf_path_var = tk.Label(text="", fg="white", background="black", font=("Courier", 10))
pdf_path_var.grid(column=0, row=2, pady=10)

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 14))
open_button = ttk.Button(window, text='Choose File', command=select_file)
open_button.grid(column=0, row=3, pady=10)

success_label = tk.Label(text="", fg="white", background="black", font=("Courier", 24))
success_label.grid(column=0, row=4, pady=10)


window.mainloop()
