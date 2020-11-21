# Hardware Oriented Signal Processing
<sub>Armin Niederm�ller, Ahmet Cihat Bozkurt</sub>
Using convolution for Image-Processing such as Filtering, Edge Detection. Convolutionional Neural Networks

# Introduction

The convolution f \* g is a mathematical operation on two functions f and g. The function g is mirrored on and then then shifted (both on the x-axis) over the function f.
The result of f \* g  is the value of the area between the two overlapping functions f and g at each point when shifting g over f. The following image gives an intuitive idea 
about what the convolution is doing:

![Convolution](https://upload.wikimedia.org/wikipedia/commons/6/6a/Convolution_of_box_signal_with_itself2.gif)\
<sub>Image Source: [Wikipedia](https://en.wikipedia.org/wiki/Convolution)</sub>

The convolution formula...:\
![Convolution](https://github.com/nerovalerius/convolution/blob/main/images/convolution_formula.jpg)


# Applications

## Signal Filtering
FIR Filter?

## Image Processing

An digital image can be interpreted as a two dimensional signal with coordinates x,y for each Pixel P(x,y).
The brightness of the pixel P(x,y) signal is seen as the current signal value f(x,y) and x,y as the current position. 
An 2D image convolution is realized by shifting a so-called convolution kernel over an image).
Both are represented as matrices, where the kernel is smaller than the image, usually 3x3.
When shifting the kernel over the image, it performis an elementwise multiplication with the part of the iamge it is currently on.
The results of this operation are then summed up and written into a single output pixel as seen in the following images:

<img src="/images/image_convolution.gif" width="100" height="100"/>

<sub>Image Source: [TowardsDataScience](https://towardsdatascience.com/intuitively-understanding-convolutions-for-deep-learning-1f6f42faee1)</sub>

<img src="/images/image_convolution_2.gif" width="100" height="100"/>

<sub>Image Source: [TowardsDataScience](https://towardsdatascience.com/intuitively-understanding-convolutions-for-deep-learning-1f6f42faee1)</sub>


The convolution in image processing can be used, amongst others, for the following fields:
### Blur / Denoising (C++ / Python)
Ahmet
### Canny Edge Detection (C++ / Python)
Armin
### Sobel Edge Operator (C++ / Python)
Ahmet
### Laplace operator (C++ / Python)
Armin
### Hough Line/Circle Transform (C++ / Python)
Armin

## Audio Processing
Ahmet
### Cross-Correlation
Ahmet
### Auto-Correlation
Ahmet

## Artificial Intelligence / Deep Learning
Armin + Ahmet
### Convolutional Neural Networks
Armin + Ahmet
### Image Classification with CNNs and Tensorflow 2.0 / Keras
Armin + Ahmet



# Showcase
Armin + Ahmet


