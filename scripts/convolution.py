import sys
import pip
from convolution_header import *
import numpy as np
from PyQt5.QtWidgets import QApplication

# MAIN
# Our Application
app = QtWidgets.QApplication(sys.argv)
mainWindow = MainWindow()

# Add a function to our Application - y, x, color, name, sample frequency, duration in seconds
#mainWindow.addFunction(t, x, 'r', 'square signal', fs, length)

app.exec_()
