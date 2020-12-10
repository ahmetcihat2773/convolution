# Hardware Oriented Signal Processing
<sub>Armin Niedermueller, Ahmet Cihat Bozkurt</sub>

Using convolution for Image-Processing such as Filtering, Edge Detection. Convolutionional Neural Networks

# Introduction

The convolution f \* g is a mathematical operation on two functions f and g. The function g is mirrored on and then then shifted (both on the x-axis) over the function f.
The result of f \* g  is the value of the area between the two overlapping functions f and g at each point when shifting g over f. The following image gives an intuitive idea 
about what the convolution is doing:

<img src="https://upload.wikimedia.org/wikipedia/commons/6/6a/Convolution_of_box_signal_with_itself2.gif" width="400"/>
<sub>Image Source: [Wikipedia](https://en.wikipedia.org/wiki/Convolution)</sub>

The convolution formula...:\
<img src="/images/convolution_formula.jpg"/>

# Applications

## Signal Filtering
What is a filter ? 

For image processing or signal processing, unwanted components or features can be suppressed by applying filters. Filters can be used for different kinds of purposes such as anti-aliasing, power supply smoothing, noise suppression, etc. Filter types can be divided into different classes based on their construction, frequency response, impulse response.  

## Based on Construction
### Passive Filter
Passive filters are designed with passive electronic components such as resistors, inductors ,and capacitors. Since electronic components are consuming energy during functioning, the energy of the input signal always less then the output signal energy in application.   
### Active Filter
In active filters, apart from passive components which are mentioned above, active components are also used such as transistors, and amplifiers. Thanks to the active filters, unwanted parts of a signal can be suppressed and rest of the signal can be impowered.
## Based on Frequency Response
Filters are mainly classified into four classes which are lowpass filter, highpass filter, bandpass filter, and band-reject filter. The following picture shows the frequency response of each type of the filter.

<img src="https://www.electricaltechnology.org/wp-content/uploads/2019/05/Types-Of-Filters-768x461.png" width="400"/>
<sub>Image Source: [Electricaltechnology](https://www.electricaltechnology.org)</sub>


### Low Pass Filter 
Low pass filters are designed to allow frequencies which are lower than cutoff frequency and attenuate the rest. They are used in suppressing the noise, blocking high pitches in speakers, etc.
### High Pass Filter
High pass filters are designed to allow frequencies which are higher than cutoff frequency and attenuate rest. They are used in low-frequency noise reduction, audio amplifiers etc. 
### Band Pass Filter 
Bandpass filters  have upper and lower cutoff frequencies and allow frequencies that are between these cutoff frequencies and attenuate the rest. They are used in wireless transmitters and receivers
### Band Reject Filter 
Band reject filters have upper and lower cutoff frequencies like band-pass filters and attenuate the frequencies which are between the cutoff frequencies and allow the rest.This type of filter is also used in telecommunication, audio signal processing, and many more.
## Based on Frequncy Response

### FIR Filter
FIR(finite impulse response) filters don't have a feedback that's why output signal depends only on the current and previous input values. This can be seen in the given formula below.  It is called as finite impulse response because there is no feedback in the filter and this make the output signal drops to zero after some time interval. This can be observed in the figure SS. Another interesting property is FIR filters have linear phase response which means all the frequencies are shifted equally in frequency domain after filtering operation.


<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/FIR_Filter.svg/600px-FIR_Filter.svg.png" width="400"/>
<sub>Image Source: [Wikipedia](https://en.wikipedia.org/wiki/Finite_impulse_response)</sub>



<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/c43ba6c329a471401e87fe17c6130d801602ffdf" width="400"/>
<sub>Image Source: [Wikipedia](https://en.wikipedia.org/wiki/Finite_impulse_response)</sub>


Here x[n] is the input signal, y[n] is the output signal, N is the filter order, b_i is the ith coefficient of filter.  

### IIR Filter
IIR(infinite impulse response) filters have feedback from output to input that's why output depends on current and previous inputs and previous outputs. The feed back can be observed in the given figure SAS. TODO: give some information about IIR filter formula. 

<img src="https://i1.wp.com/technobyte.org/wp-content/uploads/2019/12/IIR-filter-bloack-diagram-FIR-vs-IIR.jpg?w=371&ssl=1" width="400"/>
<sub>Image Source: [Technobyte](https://technobyte.org)</sub>





## Image Processing

An digital image can be interpreted as a two dimensional signal with coordinates x,y for each Pixel P(x,y).
The brightness of the pixel P(x,y) signal is seen as the current signal value f(x,y) and x,y as the current position. 
An 2D image convolution is realized by shifting a so-called convolution kernel over an image).
Both are represented as matrices, where the kernel is smaller than the image, usually 3x3.
When shifting the kernel over the image, it performis an elementwise multiplication with the part of the iamge it is currently on.
The results of this operation are then summed up and written into a single output pixel as seen in the following images:

<img src="/images/image_convolution.gif" width="300"/>

<sub>Image Source: [TowardsDataScience](https://towardsdatascience.com/intuitively-understanding-convolutions-for-deep-learning-1f6f42faee1)</sub>

<img src="/images/image_convolution_2.gif" width="300"/>

<sub>Image Source: [TowardsDataScience](https://towardsdatascience.com/intuitively-understanding-convolutions-for-deep-learning-1f6f42faee1)</sub>


The convolution in image processing can be used, amongst others, for the following fields:
### Blur / Denoising (C++ / Python)
Blurring method is generally used in the preprocessing of image to remove the noise or remove details in image. This can be done via a linear or nonlinear filter. 
#### Linear Filter : 
Averaging filters are linear filters and they are used to reduce the noise in an image. This type of the filter, replace the center values with the average of the neighborhood values to decrease the sharp transition if there is. Although it is really useful for noise removing, smoothing the image reduces the edge information which is lied inside the image ,so this is a trade-off for the averaging filter. For illustration, an averaging filter is applied to a noisy image. You can see the original, noisy, and filter result images below. 

$$X = \begin{bmatrix}1 & 1 & 1\\
1 & 1 & 1\\
1 & 1 & 1\\
1 & 1 & 1
\end{bmatrix}$$
#### Original Image
Original Image | Image with Noise | Filtered Image
:-----------------:|:---------------:|:----:
<img src="/images/harold_gray.jpg" width="300"/>|<img src="/images/harold_gray_noise.png" width="300"/>| <img src="/images/harold_gray_filtered.jpg" width="300"/>

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


