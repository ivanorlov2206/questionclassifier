import os
import threading
import tkinter.filedialog
from tkinter import *
from tkinter import ttk
import webbrowser
from Classifiers.ParaphraseClassifier import ParaphraseClassifier
from Utils.ReadingUtils import proceedXLS
from Utils.StringUtils import processStringList
from Writers.HtmlWriter import HtmlWriter

from Frontend.BasicFrontend import BasicFrontend


class TkFrontend(BasicFrontend):
    def __init__(self, classifier):
        self.classifier = classifier
        self._drawUi()

    def _openFileSelector(self):
        filepath = tkinter.filedialog.askopenfile(filetypes=[("Excel files", ".xlsx .xls")])
        if filepath:
            self.filePathEntry.delete(0, END)
            self.filePathEntry.insert(0, filepath.name)

    def _processFunction(self):
        col = self.columnSelector.get()
        path = self.filePathEntry.get()
        if not os.path.exists(path):
            self.mainLabelVar.set("File does not exist!")
            return
        if not path.lower().endswith(".xls") and not path.lower().endswith(".xlsx"):
            self.mainLabelVar.set("Wrong file type")
            return
        self.mainLabelVar.set("Loading libraries(this may take a while)")
        self.classifier.load()
        self.mainLabelVar.set("Question classifier v0.1")
        self.mainLabelVar.set("Processing file...")
        data = proceedXLS(path, col)
        data = processStringList(data)
        predictionResult = self.classifier.classify(data)
        newfile = tkinter.filedialog.asksaveasfilename(filetypes=[("HTML files", ".html")])
        if not newfile:
            return
        if not newfile.lower().endswith(".html"):
            newfile += ".html"
        writer = HtmlWriter(newfile)
        writer.write(predictionResult)
        self.mainLabelVar.set("Ready!")
        webbrowser.open("file://" + newfile)

    def _process(self):
        t = threading.Thread(target=self._processFunction)
        t.start()

    def _drawUi(self):
        self.window = Tk()
        self.window.title("Question Classifier 0.1")
        self.window.geometry("350x250")
        self.window.resizable(False, False)

        self.mainLabelVar = tkinter.StringVar()

        self.mainLabel = tkinter.Label(self.window, textvariable=self.mainLabelVar)
        self.mainLabel.config(font=('Helvetica bold', 15))
        self.mainLabelVar.set("Question classifier v0.1")
        self.mainLabel.pack(pady=20)

        frame = tkinter.Frame(self.window)
        frame.pack()

        self.filePathEntry = tkinter.Entry(frame, font=('Helvetica', 14), text="Select file")
        self.filePathEntry.grid(row=2, column=0, sticky=W, padx=5)
        self.fileSelectButton = tkinter.Button(frame, text="Select file", font=('Helvetica', 10),
                                               command=self._openFileSelector)
        self.fileSelectButton.grid(row=2, column=1, sticky=W)
        self.columnSelectorLabel = tkinter.Label(frame, text="Column to process:", font=("Helvetica bold", 13))
        self.columnSelectorLabel.grid(row=3, column=0, sticky=W, pady=10)
        self.columnSelector = ttk.Combobox(frame, values=[chr(ord('A') + i) for i in range(0, 26)], width=7,
                                           state="readonly")
        self.columnSelector.current(0)
        self.columnSelector.grid(row=3, column=1, sticky=W)

        processBtn = Button(frame, text="Process!", font=('Helvetica', 13), command=self._process)
        processBtn.grid(row=5, column=0, sticky=W)

        frame.grid_rowconfigure(1, minsize=30)

    def start(self):
        self.window.mainloop()
