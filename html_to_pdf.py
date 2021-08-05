# Simple app which takes in a URL and generates a PDF of the page

from tkinter import *
from tkinter import messagebox
import pdfkit

class SimpleWindow(object):

    def __init__(self, window):
        self.window = window
        self.window.wm_title("HTML to PDF Converter Application")

        self.create_labels(window)
        self.create_fields(window)

    def create_labels(self, window):
        lblURL = Label(window, text="URL")
        lblURL.grid(row=1, column=0)

        lblOutput = Label(window, text="Output")
        lblOutput.grid(row=2, column=0)

    def create_fields(self, window):

        self.url_text = StringVar(window)
        self.entURL = Entry(window, width=80, textvariable=self.url_text)
        self.entURL.grid(row=1, column=1)

        self.output_text = StringVar(window)
        self.entOutput = Entry(window, textvariable=self.output_text)
        self.entOutput.grid(row=2, column=1, sticky=W)  # sticky=W aligns field to left side of grid cell

        btnSearch = Button(window, text="Generate PDF", width=12, command=self.urltopdf)
        btnSearch.grid(row=4, column=1, sticky=W)

    def urltopdf(self):
        
        '''
            input
            - url : target url
            - pdffile : target pdf file name
        '''

        entered_url = self.url_text.get()
        entered_output = self.output_text.get()
        if entered_url is '' or entered_output is '':
            messagebox.showwarning("Invalid Entry", "Please enter both fields.")
            return
        else:
            output_dir = r"C:\Users\Inspiron3650\Desktop\HTML_to_PDF"
            path_wkthmltopdf = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
            config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

            pdfkit.from_url(entered_url, output_dir + "\\" + entered_output,configuration=config)


window = Tk()
simple_app = SimpleWindow(window)
window.geometry("600x150+300+300")  #(window width x window height + position right + position down)
window.grid_rowconfigure(3, minsize=20)
window.grid_rowconfigure(0, minsize=20)

window.mainloop()