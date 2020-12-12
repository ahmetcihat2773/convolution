# Hardware Oriented Signal Processing
<sub>Armin Niedermueller, Ahmet Cihat Bozkurt</sub>

Using convolution for Image-Processing such as Filtering, Edge Detection. Convolutionional Neural Networks

# Introduction

The convolution f \* g is a mathematical operation on two functions f and g. The function g is mirrored on and then then shifted (both on the x-axis) over the function f.
The result of f \* g  is the value of the area between the two overlapping functions f and g at each point when shifting g over f. The following image gives an intuitive idea 
about what the convolution is doing:

<img src="https://upload.wikimedia.org/wikipedia/commons/6/6a/Convolution_of_box_signal_with_itself2.gif" width="400"/>
<sub>Image Source: [Wikipedia - Convolution](https://en.wikipedia.org/wiki/Convolution)</sub>

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
<sub>Image Source: https://en.wikipedia.org/wiki/Finite_impulse_response</sub>

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/c43ba6c329a471401e87fe17c6130d801602ffdf" width="400"/>
<sub>Image Source: https://en.wikipedia.org/wiki/Finite_impulse_response</sub>

Here x[n] is the input signal, y[n] is the output signal, N is the filter order, b_i is the ith coefficient of filter.  

### IIR Filter
IIR(infinite impulse response) filters have feedback from output to input that's why output depends on current and previous inputs and previous outputs. The feed back can be observed in the given figure SAS. TODO: give some information about IIR filter formula. 

<img src="https://i1.wp.com/technobyte.org/wp-content/uploads/2019/12/IIR-filter-bloack-diagram-FIR-vs-IIR.jpg?w=371&ssl=1" width="350"/>
<sub>Image Source: https://technobyte.org </sub>



## Image Processing

An digital image can be interpreted as a two dimensional signal with coordinates x,y for each Pixel P(x,y).
The brightness of the pixel P(x,y) signal is seen as the current signal value f(x,y) and x,y as the current position. 
An 2D image convolution is realized by shifting a so-called convolution kernel over an image).
Both are represented as matrices, where the kernel is smaller than the image, usually 3x3.
When shifting the kernel over the image, it performis an elementwise multiplication with the part of the iamge it is currently on.
The results of this operation are then summed up and written into a single output pixel as seen in the following images:

<img src="/images/image_convolution.gif" width="300"/>
<sub>Image Source: https://towardsdatascience.com/intuitively-understanding-convolutions-for-deep-learning-1f6f42faee1 </sub>

<img src="/images/image_convolution_2.gif" width="300"/>
<sub>Image Source: https://towardsdatascience.com/intuitively-understanding-convolutions-for-deep-learning-1f6f42faee1 </sub>

The convolution in image processing can be used, amongst others, for the following fields:
### Blur / Denoising
Blurring method is generally used in the preprocessing of image to remove the noise or remove details in image. This can be done via a linear or nonlinear filter. 
#### Linear Filter : 
Averaging filters are linear filters and they are used to reduce the noise in an image. This type of the filter, replace the center values with the average of the neighborhood values to decrease the sharp transition if there is.
Although it is really useful for noise removing, smoothing the image reduces the edge information which is lied inside the image ,so this is a trade-off for the averaging filter.
A possible kernel is given below for averaging operation. Each of the element is 1 and at the end of the filter operation the result has to be normalized with the number of element in the kernel.

![](https://latex.codecogs.com/gif.latex?K%20%3D%20%5Cdfrac%7B1%7D%7B9%7D%5Cbegin%7Bbmatrix%7D%201%20%26%201%20%26%201%20%5C%5C%201%20%26%201%20%26%201%20%5C%5C%201%20%26%201%20%26%201%20%5Cend%7Bbmatrix%7D)

For illustration, an averaging filter is applied to a noisy image. You can see the original, noisy, and filter result images below.

Original Image | Image with Noise | Filtered Image
:-----------------:|:---------------:|:----:
<img src="/images/harold_gray.jpg" width="300"/>|<img src="/images/harold_gray_noise.png" width="300"/>| <img src="/images/harold_gray_filtered.jpg" width="300"/>

### Canny Edge Detector

The canny edge detector is used to extract structural information from images. It reduces the data amount to be processed<sup>1</sup>.
The following steps are conducted to extract edge information from an image with the canny algorithm<sup>2</sup>:
* Convolving the image with a gaussian filter kernel to filter out noise

	![](https://latex.codecogs.com/gif.latex?K%20%3D%20%5Cdfrac%7B1%7D%7B16%7D%5Cbegin%7Bbmatrix%7D%201%20%26%202%20%26%201%20%5C%5C%202%20%26%204%20%26%202%20%5C%5C%201%20%26%202%20%26%201%20%5Cend%7Bbmatrix%7D)

* Convolution with a pair of sobel kernels in X- and Y-direction an calculate the gradient of the image

	![](https://latex.codecogs.com/gif.latex?G_%7Bx%7D%20%3D%20%5Cbegin%7Bbmatrix%7D%20-1%20%26%200%20%26%20&plus;1%20%5C%5C%20-2%20%26%200%20%26%20&plus;2%20%5C%5C%20-1%20%26%200%20%26%20&plus;1%20%5Cend%7Bbmatrix%7D)
<br /><br />
	![](https://latex.codecogs.com/gif.latex?G_%7By%7D%20%3D%20%5Cbegin%7Bbmatrix%7D%20-1%20%26%20-2%20%26%20-1%20%5C%5C%200%20%26%200%20%26%200%20%5C%5C%20&plus;1%20%26%20&plus;2%20%26%20&plus;1%20%5Cend%7Bbmatrix%7D)
<br /><br />
	![](https://latex.codecogs.com/gif.latex?%5Cbegin%7Barray%7D%7Bl%7D%20G%20%3D%20%5Csqrt%7B%20G_%7Bx%7D%5E%7B2%7D%20&plus;%20G_%7By%7D%5E%7B2%7D%20%7D%20%5C%5C%20%5Ctheta%20%3D%20%5Carctan%28%5Cdfrac%7B%20G_%7By%7D%20%7D%7B%20G_%7Bx%7D%20%7D%29%20%5Cend%7Barray%7D)

* Remove pixels which are not considered to be part of and edge, i.e. only thin lines will remain.
* Apply a thresholding<sup>2</sup>: 
	- If a pixel gradient is higher than the upper threshold, the pixel is accepted as an edge.
	- If a pixel gradient value is below the lower threshold, then it is rejected.
	- If the pixel gradient is between the two thresholds, then it will be accepted only if it is connected to a pixel that is above the upper threshold.

Original Image | Canny Edge Output |
:-------------:|:-----------------:|
<img src="/images/church.jpg" width="350"/>|<img src="/images/church_canny.jpg" width="350"/>

### Sobel Edge Operator
Ahmet

![](https://latex.codecogs.com/gif.latex?G_%7Bx%7D%20%3D%20%5Cbegin%7Bbmatrix%7D%20-1%20%26%200%20%26%20&plus;1%20%5C%5C%20-2%20%26%200%20%26%20&plus;2%20%5C%5C%20-1%20%26%200%20%26%20&plus;1%20%5Cend%7Bbmatrix%7D)
<br /><br />
![](https://latex.codecogs.com/gif.latex?G_%7By%7D%20%3D%20%5Cbegin%7Bbmatrix%7D%20-1%20%26%20-2%20%26%20-1%20%5C%5C%200%20%26%200%20%26%200%20%5C%5C%20&plus;1%20%26%20&plus;2%20%26%20&plus;1%20%5Cend%7Bbmatrix%7D)
<br /><br />
![](https://latex.codecogs.com/gif.latex?%5Cbegin%7Barray%7D%7Bl%7D%20G%20%3D%20%5Csqrt%7B%20G_%7Bx%7D%5E%7B2%7D%20&plus;%20G_%7By%7D%5E%7B2%7D%20%7D%20%5C%5C%20%5Ctheta%20%3D%20%5Carctan%28%5Cdfrac%7B%20G_%7By%7D%20%7D%7B%20G_%7Bx%7D%20%7D%29%20%5Cend%7Barray%7D)

### Laplace operator
While the Sobel Operator takes the first derivative of the image pixels, the Laplace Operator takes the second derivative.
On edges, the second derivative is zero. Since an image can be interpreted as a signal in 2 dimensions, the Laplacian Operator is calculated for the whole image.
Before calculating the Laplacian, a Gaussian blur is applied to remove noise<sup>3</sup>.

![](https://latex.codecogs.com/gif.latex?Laplace%28f%29%20%3D%20%5Cdfrac%7B%5Cpartial%5E%7B2%7D%20f%7D%7B%5Cpartial%20x%5E%7B2%7D%7D%20&plus;%20%5Cdfrac%7B%5Cpartial%5E%7B2%7D%20f%7D%7B%5Cpartial%20y%5E%7B2%7D%7D)

Original Image | Laplace Output |
:-------------:|:--------------:|
<img src="/images/trump.jpg" width="350"/>|<img src="/images/trump_laplacian.jpg" width="350"/>

### Hough Line/Circle Transform

After detecting edges inside an image by convolving with the Laplace/Sobel Operator, lines can be detected by conducting a Hugh Line Transform.

Imagine a straight line represented by its function: k*x + d. The line is drawn by using different values of x. 
Now imagine  a specific point P = (x_0, y_0) on this very same line. This point can be also represented by different values of k and d, each representing a line in the k,d space.


All those lines inside the k,d space intersect at a specific point, this means that all the points in x,y space (which are a line in k,d space) lie on the same line in x,y space

The hough transform works with polar coordinates, meaning that each point is defined by and angle θ and a radius ρ. Its a similar concept as the k,d space.
The following image shows, that many different angles and radii can be used to define the point P. Each line is a point inside the angle/radius space, the so-called Hough-Space.


![](https://miro.medium.com/max/700/0*JT-hhPkp-Tx4ywtu.jpg)

<sub>Image Source: [Hough Line Transform - Medium](https://medium.com/@tomasz.kacmajor/hough-lines-transform-explained-645feda072ab)</sub>


If every line is printed, a sinoid function appears.

![](https://miro.medium.com/max/700/0*pJDI5sW6oEBDQQqd.jpg)

<sub>Image Source: [Hough Line Transform - Medium](https://medium.com/@tomasz.kacmajor/hough-lines-transform-explained-645feda072ab)</sub>

When different points are on a line with other points, each of their sinusoids intersect at one point as seen in the image.

![](https://miro.medium.com/max/700/0*VPVsLApWiEayRGdQ.jpg)

<sub>Image Source: [Hough Line Transform - Medium](https://medium.com/@tomasz.kacmajor/hough-lines-transform-explained-645feda072ab)</sub>

That process is iteratively repated for every edge point in the image. Thats why before a Hough-Transform is conducted, a edge detection is needed.


Original Image | Hough Line Transform |
:-------------:|:--------------------:|
<img src="/images/chess.jpg" width="350"/>|<img src="/images/chess_hough_line.jpg" width="350"/>

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


### Sources
1. [Canny edge detector](https://en.wikipedia.org/wiki/Canny_edge_detector)
2. [Canny edge detector - OpenCV](https://docs.opencv.org/4.2.0/da/d5c/tutorial_canny_detector.html)
3. [Laplace operator - OpenCV](https://docs.opencv.org/4.2.0/d5/db5/tutorial_laplace_operator.html)
4. [Hough line transform - OpenCV](https://docs.opencv.org/4.2.0/d9/db0/tutorial_hough_lines.html)