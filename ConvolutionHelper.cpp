#include "ConvolutionHelper.h"
#include "opencv2/imgproc.hpp"
#include "opencv2/highgui.hpp"
#include <iostream>

using namespace cv;

int ConvolutionHelper::loadImage(int argc, char** argv) {

    // Parse Arguments and save image into cv::Mat
    CommandLineParser parser(argc, argv, "{@input | images/harold_original.jpg | input image}");
    input = imread(samples::findFile(parser.get<String>("@input")), IMREAD_COLOR); // Load an image

    // Check if image is loaded properly
    if (input.empty()) {
        std::cout << "Could not open or find the image!\n" << std::endl;
        std::cout << "Usage: " << argv[0] << " <Input image>" << std::endl;
        return -1;
    }
}

void ConvolutionHelper::displayImage(){

    // Load our Image
    input = cv::imread("images/harold_original.jpg");
    cv::namedWindow("input image", cv::WINDOW_NORMAL);
    cv::imshow("input image", input);

    // Wait for keystroke of user 
    cv::waitKey(0);
}

int ConvolutionHelper::displayImage(cv::Mat image) {

    // Check if image is empty
    if (image.empty()) {
        std::cout << "Image is empty!\n" << std::endl;
        return -1;
    }

    cv::namedWindow("image", cv::WINDOW_NORMAL);
    cv::imshow("image", image);

    // Wait for keystroke of user 
    cv::waitKey(0);
}



void ConvolutionHelper::convolution(cv::Mat kernel){
}


void ConvolutionHelper::onChange(int pos, void* ptr) {

    // resolve 'this':
    ConvolutionHelper* that = (ConvolutionHelper*)ptr;
    that->cannyThreshold(pos);
}


void ConvolutionHelper::cannyThreshold(int pos)  {

    blur(input_gray, detected_edges, Size(3, 3));
    Canny(detected_edges, detected_edges, lowThreshold, lowThreshold * ratio, kernel_size);
    output = Scalar::all(0);
    input.copyTo(output, detected_edges);
    imshow("Edge Map", output);
}


int ConvolutionHelper::cannyEdge(){

    // Check if image is empty
    if (input.empty()) {
        std::cout << "Image is empty!\n" << std::endl;
        return -1;
    }
       
    // Create the same sized output image as the input image
    output.create(input.size(), input.type());

    // Create greyscale image of the input image
    cvtColor(input, input_gray, COLOR_BGR2GRAY);

    // Create Window 
    namedWindow("Edge Map", WINDOW_AUTOSIZE);
    
    // Create mouse slider inside the window
    createTrackbar("Min Threshold:", "Edge Map", &lowThreshold, max_lowThreshold, &ConvolutionHelper::onChange, this);

    // Define initial thresholds for canny algorithm
    onChange(0, this);

    // Wait for keystroke of the user
    waitKey(0);

    return 0;

}

