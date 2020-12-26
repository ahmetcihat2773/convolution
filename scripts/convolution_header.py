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


        #  GRID Layout
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
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.suptitle('Functions: Time Domain | Fourier Domain')

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
        self.convolutionPlot.set_xlabel('t [s]')
        self.convolutionPlot.set_ylabel('f(t)')
        self.convolutionPlot.set_ylim(0.0,10.0)
        
        super(MplCanvas, self).__init__(fig)


# The Main window of our program
class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
  
    def initUI(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Set Window Size and Title
        self.setGeometry(200, 200, 1200, 900)
        self.setWindowTitle('Up- and Downsampling Demonstration - Armin Niedermüller')

        # Define a grid layout
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        # Define the Plot with its subplots
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)

        # Create a slider
        self.convolutionSlider = QSlider(Qt.Horizontal)
        self.convolutionSlider.setRange(0,10)               # maximum range is signal lenght * 2 ?
        self.convolutionSlider.setSingleStep(1) 
        self.convolutionSlider.setValue(1)
        self.convolutionSlider.setTickInterval(1)
        self.convolutionSlider.setTickPosition(QSlider.TicksBothSides)

            
        # Creat Buttons
        self.fxButton = QPushButton('Set', self)
        self.gxButton = QPushButton('Set', self)

        # Create Labels
        self.fxLabel = QtWidgets.QLabel()
        self.fxLabel.setText('Type in a function f(x):')
        self.gxLabel = QtWidgets.QLabel()
        self.gxLabel.setText('Type in a function g(x):')

        # Create Textboxes
        self.fxInput = QLineEdit(self)
        self.gxInput = QLineEdit(self)

        # Connect the sliders to our plots - if the slider value changes, the plot is updated
        self.convolutionSlider.valueChanged[int].connect(self.upsamplePlot)

        # Connect the Buttons to the input reading functions
        self.fxButton.clicked.connect(self.readFx)
        self.gxButton.clicked.connect(self.readGx)


        #  GRID Layout
        #      1                              6                        12                          18
        #      _____________________________________________________________________________________     
        #    1 |                                    f(x) Plot                                       | 
        #      |                                    g(x) PLot                                       |
        #   14 |                                Convolution PLot                                    |
        #   15 |                               Convolution Slider                                   |
        #   16 | f(x) Dropbox (Function Type) | f(x) Slider Amplitude  | f(x) Slider Frequency      |
        #   17 | g(x) Dropbox (Function Type) | g(x) Slider Amplitude  | g(x) Slider Frequency      |
        #   18 |____________________________________________________________________________________|



        # Lets make 20 Columns and 20 Rows
        grid_layout.addWidget(self.fxLabel, 3,1,1,2) # start from row=3, column=1, span over 1 row and 2 columns

        grid_layout.addWidget(self.fxInput, 3,3,1,2)    #  dropbox
        grid_layout.addWidget(self.fxButton, 3,6,1,2)   #  slider amp
        grid_layout.addWidget(self.gxLabel, 9,1,1,2)    #  slider freq
        grid_layout.addWidget(self.gxInput, 9,3,1,2)    #
        grid_layout.addWidget(self.gxButton, 9,6,1,2)   # s

        grid_layout.addWidget(self.canvas, 1,1,14,18) # start from row=1, column=1, span over 14 rows and 18 columns
        grid_layout.addWidget(self.convolutionSlider, 15,1,1,18)     

       
        # A dictionary where our functions are stored
        self.plot_refs = dict()
        self.signals = dict()

        self.show()


    # Function reader
    def readFx(self):
        functionValue = self.fxInput.text()
        QMessageBox.question(self, 'f(x)', "f(x): " + functionValue, QMessageBox.Ok, QMessageBox.Ok)
        self.fxInput.setText("")

    # Function reader
    def readGx(self):
        functionValue = self.gxInput.text()
        QMessageBox.question(self, 'g(x)', "g(x): " + functionValue, QMessageBox.Ok, QMessageBox.Ok)
        self.gxInput.setText("")


    # Add a function to our plots
    def addFunction(self, y, x, color, name, f_s, length):
        
        newSignal = MySignal(y, x, color, f_s, length)

        # SIGNAL - Add plot reference to our List of plot refs
        self.plot_refs[name] = self.canvas.fxPlot.plot(newSignal.y,
                                                newSignal.x,
                                                newSignal.color) 
        # And add the functions to our extra list
        self.signals[name] = newSignal

        # SPECTRUM
        X = np.fft.fft(x)

        # Add plot reference to our List of plot refs
        self.plot_refs[name + 'fft'] = self.canvas.original_fft_plot.plot(abs(X), newSignal.color) 

        # update Plots
        self.upsamplePlot(1)
        self.downsamplePlot(1)


    # Function to be called after using the slider
    def upsamplePlot(self, value):
        
        if self.signals['square signal'] is None:
            return False 

        f_s = self.signals['square signal'].f_s
        length = self.signals['square signal'].length

        # Upsampling
        # 0 er Array erstellen
        l_upsampling = value
        np.zeros(f_s * l_upsampling)

        # our function
        x = self.signals['square signal'].x
        

        # Calculate FFT
        X = np.fft.fft(x)
        freq = np.fft.fftfreq(len(x), 1/f_s)

        # Add zeros
        X_upsampled = np.insert(X, int(X.shape[0]/2), np.zeros(f_s * l_upsampling))
        Y_upsampled = np.arange(0, X.shape[0] + f_s * l_upsampling)

        # Inverse FFT
        x_upsampled = np.fft.ifft(X_upsampled)
       
        # Keep energy the same after transformations / up-downsampling
        if l_upsampling != 0:
            x_upsampled *= X_upsampled.shape[0] / X.shape[0]
            
        # Create vector from 0 to 1 - stepsize = 1/fs
        t_upsampled = np.linspace(0, length,
                                 f_s
                                 + f_s * l_upsampling)

        # Only upsample if Checkbox is active
        if self.activateUpsampling is True:
            upsampledSignal = MySignal(t_upsampled, x_upsampled, 'g', f_s, length)
        else:
            upsampledSignal = self.signals['square signal']
            upsampledSignal.color = 'g'
            X_upsampled = X
            Y_upsampled = np.arange(0, X.shape[0])


        # Add the upsampled signal to our plots
        if self.plot_refs.get('upsampled square signal') is None:

            # Add SIGNAL plot reference to our List of plot_refs
            self.plot_refs['upsampled square signal'] = self.canvas.gxPlot.plot(upsampledSignal.y,
                                                    upsampledSignal.x,
                                                    upsampledSignal.color) 

            # Add SPECTRUM plot reference to our List of plot_refs
            self.plot_refs['upsampled fft'] = self.canvas.upsampled_fft_plot.plot(
                                                    abs(X_upsampled),
                                                    upsampledSignal.color) 

        # change values over reference
        else:
            # SIGNAL
            self.plot_refs['upsampled square signal'][0].set_ydata(upsampledSignal.x)
            self.plot_refs['upsampled square signal'][0].set_xdata(upsampledSignal.y)
            self.plot_refs['upsampled square signal'][0].set_color(upsampledSignal.color)
            
            # SPECTRUM
            self.plot_refs['upsampled fft'][0].set_ydata(np.abs(X_upsampled))
            self.plot_refs['upsampled fft'][0].set_xdata(Y_upsampled)

            # SPECTRUM - change the x value range of the plot accordingly
            if self.activateUpsampling is True:
                self.canvas.upsampled_fft_plot.set_xlim(0,  X.shape[0] + f_s * l_upsampling)
            else:   
                self.canvas.upsampled_fft_plot.set_xlim(0,  X.shape[0])

        # Trigger the canvas to update and redraw.
        self.canvas.draw()



    # Function to be called after using the slider
    def downsamplePlot(self, value):
     
            if self.signals['square signal'] is None or value == 0:
                return False 

            # our function and sampling frequency
            x = self.signals['square signal'].x
            y = self.signals['square signal'].x
            f_s = self.signals['square signal'].f_s
            length = self.signals['square signal'].length

            # Our downsampling factor
            downsampling_factor = value

            # Create an FIR Anti-Aliasing Filter
            # Cutoff Frequency is f_s/2 
            # by - 0.01 we give a headroom for the filter of 1 %  
            b = signal.firwin(30, (1.0/downsampling_factor) - 0.01) 

            # Apply the Anti-Aliasgin Filter
            # Since a FIR filter only has b coefficients, set a = 1
            a=1
            lowpass = signal.lfilter(b, a, x) 

            # Create vector from 0 to 1 - stepsize = 1/fs
            t_downsampled = np.linspace(0, length,
                                 int(np.ceil(f_s / downsampling_factor)))

            # Perform the downsampling
            x_downsampled = lowpass[::downsampling_factor]
            
            # Calculate FFT
            X_downsampled = np.fft.fft(x_downsampled)
            Y_downsampled = np.arange(0, X_downsampled.shape[0])

            X = np.fft.fft(x)
            Y = np.arange(0, X.shape[0])

            # cancel time_shift
            x_shift = int(13/downsampling_factor)
                        
            # Keep energy the same after transformations / up-downsampling
            x_downsampled *= X_downsampled.shape[0] / X.shape[0]
            x_downsampled = np.concatenate((x_downsampled[x_shift:],x_downsampled[:x_shift]))

            # Only upsample if Checkbox is active
            if self.activateDownsampling is True:
                downsampledSignal = MySignal(t_downsampled, x_downsampled, 'b', f_s, length)
            else:
                downsampledSignal = self.signals['square signal']
                downsampledSignal.color = 'b'
                X_downsampled = X
                Y_downsampled = Y

            # Add the downsampled signal to our plots
            if self.plot_refs.get('downsampled square signal') is None:

                # Add SIGNAL plot reference to our List of plot_refs
                self.plot_refs['downsampled square signal'] = self.canvas.convolutionPlot.plot(downsampledSignal.y,
                                                        downsampledSignal.x,
                                                        downsampledSignal.color) 

                # Add SPECTRUM plot reference to our List of plot_refs
                self.plot_refs['downsampled fft'] = self.canvas.downsampled_fft_plot.plot(
                                                        abs(X_downsampled),
                                                        downsampledSignal.color) 
            else:
                # SIGNAL
                self.plot_refs['downsampled square signal'][0].set_ydata(downsampledSignal.x)
                self.plot_refs['downsampled square signal'][0].set_xdata(downsampledSignal.y)
                self.plot_refs['downsampled square signal'][0].set_color(downsampledSignal.color)
            
                # SPECTRUM
                self.plot_refs['downsampled fft'][0].set_ydata(np.abs(X_downsampled))
                self.plot_refs['downsampled fft'][0].set_xdata(Y_downsampled)

                # SPECTRUM - change the x value range of the plot accordingly
                self.canvas.downsampled_fft_plot.set_xlim(0,  X_downsampled.shape[0])

            
            # Trigger the canvas to downdate and redraw.
            self.canvas.draw()




# calculate a Fourier Series for a Square Signal
def myFourierSeries(fs_signal, h_signal, len_signal, k_max_signal, frequency):
    """
    Parameters
    ----------
    fs_signal:    int,    Sampling frequency of the signal
    h_signal:     double, Amplitude
    len_signal:   int,    Signal length in seconds
    k_max_signal: int,    variable Fourier Series length

    Returns
    ---------
    f:            array[double], Fourier Series of a square signal
    """

    # Generate evenly spaced timestamps
    #x = np.linspace(0, len_signal, fs_signal, endpoint=False) 
    time = np.arange(0, len_signal, 1/fs_signal)   # Create vector from 0 to 1 - stepsize = 1/fs
    
    # This will be our resulting signal
    f = np.zeros([len_signal])

    # Go over all samples for our signal and calculate its value via fourier series
    for x in range(0, len_signal):

      # The inner sum - see RHS of formula
      sum = 0
      for k in range(1, k_max_signal+1, 2):
        sum += k**(-1) * np.sin(2 * np.pi * k * time[x] * frequency)
            
      # The scalar in front of the sum - see RHS of formula
      f[x] =  sum * 4 * h_signal * np.pi**(-1)
    
    return f 
