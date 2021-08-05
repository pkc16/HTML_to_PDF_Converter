# Simple app which takes in a URL and generates a PDF of the page

from tkinter import *
from tkinter import messagebox
import pdfkit
import configparser
import os

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
            # get settings from config file
            # first get the current directory
            cur_dir = os.path.dirname(__file__)

            # generate the absolute filepath of the output file
            config_filename = "html_to_pdf_config.txt"
            config_filepath = os.path.join(cur_dir, config_filename)

            # now get the info from the config file and set variables
            parser = configparser.ConfigParser()
            parser.read_file(open(config_filepath))
            output_dir = parser.get('Settings', 'output_directory')
            path_wkthmltopdf = parser.get('Settings', 'wkhtmltopdf_path')
            config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

            # now generate the pdf
            pdfkit.from_url(entered_url, output_dir + "\\" + entered_output,configuration=config)


window = Tk()
simple_app = SimpleWindow(window)
window.geometry("600x150+300+300")  #(window width x window height + position right + position down)
window.grid_rowconfigure(3, minsize=20)
window.grid_rowconfigure(0, minsize=20)

window.mainloop()