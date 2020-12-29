import sys
import pip
import random

import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
matplotlib.use('Qt5Agg')

import numpy as np
from scipy import signal
from scipy.ndimage.interpolation import shift

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication, QSlider, QCheckBox, QLineEdit, QMessageBox)
from PyQt5.QtCore import Qt
from scipy import signal
import matplotlib.pyplot as plt


# Saves a Signal and its parameters
class MySignal(object):
    x = None
    y = None
    color = ''
    f_s = 0
    length = 0

    def __init__(self, y, x, color, f_s, length):
        self.x = x
        self.y = y
        self.color = color
        self.f_s = f_s
        self.length = length



# Class that plots our functions
class MplCanvas(FigureCanvasQTAgg):


        #  Layout
        #      1                              6                        12                          18
        #      _____________________________________________________________________________________     
        #    1 |                                    f(x) Plot                                       | 
        #      |                                    g(x) PLot                                       |
        #   14 |                                Convolution PLot                                    |
        #   15 |                               Convolution Slider                                   |
        #   16 | f(x) Dropbox (Function Type) | f(x) Slider Amplitude  | f(x) Slider Frequency      |
        #   17 | g(x) Dropbox (Function Type) | g(x) Slider Amplitude  | g(x) Slider Frequency      |
        #   18 |____________________________________________________________________________________|


    def __init__(self, parent=None, width=5, height=4, dpi=100):

        # Plot and its title
        fig = Figure(figsize=(width, height), dpi=dpi,tight_layout=True)

        # Format spaces between plots
        
        fig.subplots_adjust(left=0.125,
                  bottom=0.1, 
                  right=0.9, 
                  top=0.9, 
                  wspace=0.2, 
                  hspace=1)

        # The Plots and their formatting
        # PLOT 1
        self.fxPlot = fig.add_subplot(311, title='f(x)')
        self.fxPlot.set_xlabel('t [s]')
        self.fxPlot.set_ylabel('f(t)')
        self.fxPlot.set_ylim(0.0,10.0)
        
        # PLOT 2
        self.gxPlot = fig.add_subplot(312, title='g(x)')
        self.gxPlot.set_xlabel('t [s]')
        self.gxPlot.set_ylabel('f(t)')
        self.gxPlot.set_ylim(0.0,10.0)
        
        # PLOT 3
        self.convolutionPlot = fig.add_subplot(313, title='Convolution of f(x) and g(x)')
        self.convolutionPlot.set_xlabel('tau')
        self.convolutionPlot.set_ylabel('f(t)')
        self.convolutionPlot.set_xlim(-2,2)
        
        super(MplCanvas, self).__init__(fig)


# The Main window of our program
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
  
    def initUI(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Set Window Size and Title

        self.setWindowTitle('Convolution Demo')
        self.setFixedWidth(1000)
        self.setFixedHeight(800)

        self.mainWindow = QtWidgets.QVBoxLayout()
        self.mainWidget = QtWidgets.QWidget()
        self.mainWidget.setLayout(self.mainWindow)

        # Define the Plot with its subplots
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.mainWindow.addWidget(self.canvas,stretch=5)

        # Sliders
        self.convolutionSlider = self.createSlider(-20,20,1,-10)
        self.convolutionSlider.valueChanged.connect(self.convolutionUpdater)
        self.fxAmpSlider = self.createSlider(0,10,1,0)
        self.fxAmpSlider.valueChanged.connect(self.fxAmpUpdater)
        self.fxFreqSlider = self.createSlider(0,10,1,0)
        self.fxFreqSlider.valueChanged.connect(self.fxFreqUpdater)
        self.gxAmpSlider = self.createSlider(0,10,1,0)
        self.gxAmpSlider.valueChanged.connect(self.gxAmpUpdater)
        self.gxFreqSlider = self.createSlider(0,10,1,0)
        self.gxFreqSlider.valueChanged.connect(self.gxFreqUpdater)
       
        # Dropboxes
        self.fxDropbox = QtWidgets.QComboBox()
        self.fxDropbox.addItem('Sine')
        self.fxDropbox.addItem('Square')
        self.fxDropbox.addItem('Triangle')
        self.fxDropbox.addItem('Sawtooth')
        self.fxDropbox.activated[str].connect(self.fxWaveFormUpdater)
        self.gxDropbox = QtWidgets.QComboBox()
        self.gxDropbox.addItem('Sine')
        self.gxDropbox.addItem('Square')
        self.gxDropbox.addItem('Triangle')
        self.gxDropbox.addItem('Sawtooth')
        self.gxDropbox.activated[str].connect(self.gxWaveFormUpdater)

        # Create Labels
        # f(x) Labels
        self.fxLabel = QtWidgets.QLabel()
        self.fxLabel.setText('f(x):')
        self.fxAmpLabel = QtWidgets.QLabel()
        self.fxAmpLabel.setText('Amplitude: ')
        self.fxAmpLabel.setStyleSheet("padding :5px") 
        self.fxAmpSliderValueLabel = QtWidgets.QLabel()
        self.fxAmpSliderValueLabel.setText('1')
        self.fxAmpSliderValueLabel.setFixedSize(20, 20)
        self.fxFreqLabel = QtWidgets.QLabel()
        self.fxFreqLabel.setText('Frequency [Hz]: ')
        self.fxFreqLabel.setStyleSheet("padding :5px") 
        self.fxFreqSliderValueLabel = QtWidgets.QLabel()
        self.fxFreqSliderValueLabel.setText('1')
        self.fxFreqSliderValueLabel.setFixedSize(20, 20)


        # g(x) Labels
        self.gxAmpLabel = QtWidgets.QLabel()
        self.gxAmpLabel.setText('Amplitude: ')
        self.gxAmpLabel.setStyleSheet("padding :5px") 
        self.gxAmpSliderValueLabel = QtWidgets.QLabel()
        self.gxAmpSliderValueLabel.setText('1')
        self.gxAmpSliderValueLabel.setFixedSize(20, 20)
        self.gxFreqLabel = QtWidgets.QLabel()
        self.gxFreqLabel.setText('Frequency [Hz]: ')
        self.gxFreqLabel.setStyleSheet("padding :5px") 
        self.gxLabel = QtWidgets.QLabel()
        self.gxLabel.setText('g(x):')
        self.gxFreqSliderValueLabel = QtWidgets.QLabel()
        self.gxFreqSliderValueLabel.setText('1')
        self.gxFreqSliderValueLabel.setFixedSize(20, 20)
  
        # convolution Labels
        self.convolutionLabel = QtWidgets.QLabel()
        self.convolutionLabel.setText('Convolution [\u03C4]: ')
        self.convolutionSliderValueLabel = QtWidgets.QLabel()
        self.convolutionSliderValueLabel.setText('0')
        self.convolutionSliderValueLabel.setFixedSize(20, 20)

        #  Layout
        #      1                              6                        12                          18
        #      _____________________________________________________________________________________     
        #    1 |                                    f(x) Plot                                       | 
        #      |                                    g(x) PLot                                       |
        #   14 |                                Convolution PLot                                    |
        #   15 |                               Convolution Slider                                   |
        #   16 | f(x) Dropbox (Function Type) | f(x) Slider Amplitude  | f(x) Slider Frequency      |
        #   17 | g(x) Dropbox (Function Type) | g(x) Slider Amplitude  | g(x) Slider Frequency      |
        #   18 |____________________________________________________________________________________|

        # f(x) Layout
        fxWidget = QtWidgets.QWidget()
        self.fxLayout = QtWidgets.QHBoxLayout()
        self.fxLayout.addWidget(self.fxLabel)
        self.fxLayout.addWidget(self.fxDropbox)
        self.fxLayout.addWidget(self.fxAmpLabel)
        self.fxLayout.addWidget(self.fxAmpSliderValueLabel)
        self.fxLayout.addWidget(self.fxAmpSlider)
        self.fxLayout.addWidget(self.fxFreqLabel)
        self.fxLayout.addWidget(self.fxFreqSliderValueLabel)
        self.fxLayout.addWidget(self.fxFreqSlider)

        fxWidget.setLayout(self.fxLayout)
        self.mainWindow.addWidget(fxWidget)

        # g(x) Layout
        gxWidget = QtWidgets.QWidget()
        self.gxLayout = QtWidgets.QHBoxLayout()
        self.gxLayout.addWidget(self.gxLabel)
        self.gxLayout.addWidget(self.gxDropbox)
        self.gxLayout.addWidget(self.gxAmpLabel)
        self.gxLayout.addWidget(self.gxAmpSliderValueLabel)
        self.gxLayout.addWidget(self.gxAmpSlider)
        self.gxLayout.addWidget(self.gxFreqLabel)
        self.gxLayout.addWidget(self.gxFreqSliderValueLabel)
        self.gxLayout.addWidget(self.gxFreqSlider)

        gxWidget.setLayout(self.gxLayout)
        self.mainWindow.addWidget(gxWidget)

        # Convolution Layout 
        convolutionWidget = QtWidgets.QWidget()
        self.convolutionLayout = QtWidgets.QHBoxLayout()
        self.convolutionLayout.addWidget(self.convolutionLabel)
        self.convolutionLayout.addWidget(self.convolutionSliderValueLabel)
        self.convolutionLayout.addWidget(self.convolutionSlider)

        convolutionWidget.setLayout(self.convolutionLayout)
        self.mainWindow.addWidget(convolutionWidget)

        self.setCentralWidget(self.mainWidget)
               
        # A dictionary where our functions are stored
        self.plot_refs = dict()
        self.signals = dict()


        # initialize Signals and plots
        self.fs = 1000       # sampling frequency
        self.fLength = 1     # signal duration

        self.x = np.linspace(0, self.fLength, self.fs, endpoint=False)

        self.fxFreq = 1
        self.fxAmp = 0
        self.fx = np.ones(self.fs * self.fLength)

        self.gxFreq = 1
        self.gxAmp = 0
        self.gx = np.ones(self.fs * self.fLength)


        self.hxFreq = 1
        self.hxAmp = 0
        convolution_x = np.ones(self.fs * self.fLength)

        # SIGNAL - Add plot reference to our List of plot refs
        self.plot_refs['fx'] = self.canvas.fxPlot.plot(self.x, self.fx, 'b') 
        self.plot_refs['gx'] = self.canvas.gxPlot.plot(self.x, self.gx, 'b') 
        self.t_fx = np.linspace(0,self.fLength,len(self.fx))
        self.t_gx = np.linspace(-1,0,len(self.gx))
        self.canvas.convolutionPlot.plot(self.t_fx,self.fx)
        self.canvas.convolutionPlot.plot(self.t_gx,self.gx)
        self.canvas.convolutionPlot.set_xlim(-2,2)

        # Set Plot limits
        self.canvas.fxPlot.set_ylim(-11,11)
        self.canvas.gxPlot.set_ylim(-11,11)
        

        self.show()


    # Chosen Function WaveForm from Dropbox
    def fxWaveFormUpdater(self, value):
        if value == 'Sine':
            self.fx = self.fxAmp * np.sin(2 * np.pi * self.fxFreq * self.x)
        elif value == 'Square':
            self.fx = self.fxAmp * signal.square(2 * np.pi * self.fxFreq * self.x, 0.5)
        elif value == 'Triangle':
            self.fx = self.fxAmp * signal.sawtooth(2 * np.pi * self.fxFreq * self.x, 0.5)
        elif value == 'Sawtooth':
            self.fx = self.fxAmp * signal.sawtooth(2 * np.pi * self.fxFreq * self.x, 1)
        # change our plots
        self.canvas.convolutionPlot.clear()
        self.plot_refs['fx'][0].set_ydata(self.fx)
        self.canvas.convolutionPlot.plot(self.t_fx,self.fx)
        self.canvas.convolutionPlot.plot(self.t_gx,self.gx)
        self.canvas.convolutionPlot.set_xlim(-2,2)
        # Trigger the canvas to update and redraw.
        self.canvas.draw()
        # Update colvolution with new signal
        self.update_convol()


    # Chosen Function WaveForm from Dropbox
    def gxWaveFormUpdater(self, value):
        if value == 'Sine':
            self.gx = self.gxAmp * np.sin(2 * np.pi * self.gxFreq * self.x)
        elif value == 'Square':
            self.gx = self.gxAmp * signal.square(2 * np.pi * self.gxFreq * self.x, 0.5)
        elif value == 'Triangle':
            self.gx = self.gxAmp * signal.sawtooth(2 * np.pi * self.gxFreq * self.x, 0.5)
        elif value == 'Sawtooth':
            self.gx = self.gxAmp * signal.sawtooth(2 * np.pi * self.gxFreq * self.x, 1)
        # change our plots
        self.canvas.convolutionPlot.clear()
        self.plot_refs['gx'][0].set_ydata(self.gx) 
        self.canvas.convolutionPlot.plot(self.t_gx,self.gx)
        self.canvas.convolutionPlot.plot(self.t_fx,self.fx)
        self.canvas.convolutionPlot.set_xlim(-2,2)


        # Trigger the canvas to update and redraw.
        self.canvas.draw()

        # Update colvolution with new signal
        self.update_convol()

    def update_convol(self):
        self.conv = signal.convolve(self.fx,self.gx)
        self.conv = self.conv/len(self.conv)        
    # Function for the convolution slider
    def convolutionUpdater(self, value):
        value = value/10
        self.update_convol()
        self.canvas.convolutionPlot.clear()
        self.convolutionSliderValueLabel.setText(str(value))
       
        if value >=-1 and value <=1:
            if value < 0:
                till = int(round((1+value),1)*self.fs)
                t = np.linspace(-1,value,len(self.conv[:till]))
                self.canvas.convolutionPlot.plot(t,self.conv[:till])
            elif value >0:
                till = int(len(self.conv)/2)+int(value*self.fs)
                t = np.linspace(-1,value,len(self.conv[:till]))
                self.canvas.convolutionPlot.plot(t,self.conv[:till])
            else:
                t = np.linspace(-1,0,int(len(self.conv)/2))
                self.canvas.convolutionPlot.plot(t,self.conv[:int(len(self.conv)/2)])


            
        #t = np.linspace(-self.fLength,self.fLength,len(self.conv))
        #self.canvas.convolutionPlot.plot(t_fx,self.fx)
        
        t_gx = np.linspace(value,value+1,len(self.gx))
        self.canvas.convolutionPlot.plot(self.t_fx,self.fx)
        self.canvas.convolutionPlot.plot(t_gx,self.gx)
        self.canvas.convolutionPlot.set_xlim(-2,2)
        self.canvas.draw()
        
        # self.plot_refs['convolution'][0].set_ydata()
        # plot 3 functions in one plot pyqt5 matplotlib, maybe with different colors
        # fx, gx, and convolution of both
        
    # Change amplitude of fx
    def fxAmpUpdater(self, value):
        self.fxAmpSliderValueLabel.setText(str(value))
        self.fxAmp = int(value)
        self.fxWaveFormUpdater(self.fxDropbox.currentText())
        
    # Change frequency of fx
    def fxFreqUpdater(self, value):
        self.fxFreqSliderValueLabel.setText(str(value))
        self.fxFreq = int(value)
        self.fxWaveFormUpdater(self.fxDropbox.currentText())

    # Change amplitude of gx
    def gxAmpUpdater(self, value):
        self.gxAmpSliderValueLabel.setText(str(value))
        self.gxAmp = int(value)
        self.gxWaveFormUpdater(self.gxDropbox.currentText())
        
    # Change frequency of gx
    def gxFreqUpdater(self, value):
        self.gxFreqSliderValueLabel.setText(str(value))
        self.gxFreq = int(value)
        self.gxWaveFormUpdater(self.gxDropbox.currentText())
        
    # Function readers
    def createSlider(self,min,max,val,start):
        slider = QSlider(Qt.Horizontal)
        slider.setRange(min,max)           
        slider.setSingleStep(val) 
        slider.setValue(start)
        slider.setTickInterval(val)
        slider.setTickPosition(QSlider.TicksBothSides)
        return slider