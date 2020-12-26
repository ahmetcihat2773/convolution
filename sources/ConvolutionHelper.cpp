#include "ConvolutionHelper.h"
#include "opencv2/imgproc.hpp"
#include "opencv2/highgui.hpp"
#include <iostream>
#include <vector>

using namespace cv;

bool ConvolutionHelper::loadImage(std::string name) {

    // Parse Arguments and save image into cv::Mat
    input = cv::imread("images/" + name);

    // Check if image is loaded properly
    if (input.empty()) {
        std::cout << "Could not open or find the image!\n" << std::endl;
        return false;
    }
    else {
        return true;
    }
}

bool ConvolutionHelper::displayImage(){

    // Load our Image
    if (!loadImage("church.jpg"))
        return false;

    cv::namedWindow("input image", cv::WINDOW_NORMAL);
    cv::imshow("input image", input);

    // Wait for keystroke of user 
    cv::waitKey(0);
}

bool ConvolutionHelper::displayImage(cv::Mat image) {

    // Check if image is empty
    if (image.empty()) {
        std::cout << "Image is empty!\n" << std::endl;
        return false;
    }

    cv::namedWindow("image", cv::WINDOW_NORMAL);
    cv::imshow("image", image);

    // Wait for keystroke of user 
    cv::waitKey(0);
}



bool ConvolutionHelper::convolution(cv::Mat kernel){
    return true;
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


bool ConvolutionHelper::cannyEdge(){

    // Load our Image
    if (!loadImage("church.jpg"))
        return false;
           
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

bool ConvolutionHelper::laplacianEdge() {

    // Load our Image
    if (!loadImage("trump.jpg"))
        return false;

    // Reduce noise by blurring with a Gaussian filter ( kernel size = 3 )
    GaussianBlur(input, input, Size(3, 3), 0, 0, BORDER_DEFAULT);
    cvtColor(input, input_gray, COLOR_BGR2GRAY); // Convert the image to grayscale

    // Calculate the Laplacian Image
    Laplacian(input_gray, output, ddepth, kernel_size, scale, delta, BORDER_DEFAULT);

    // converting back to CV_8U
    convertScaleAbs(output, abs_output);
    imshow("Laplace Demo", abs_output);

    // Wait for user
    waitKey(0);

    return 0;
}

bool ConvolutionHelper::houghLineTransform() {

    // Load our Image
    if (!loadImage("chess.jpg"))
        return false;

    // Edge detection
    Canny(input, output, 50, 200, 3);

    // Copy edges to the images that will display the results in BGR
    cvtColor(output, cOutput, COLOR_GRAY2BGR);
    cOutputP = cOutput.clone();

    // Standard Hough Line Transform
    std::vector<Vec2f> lines; // will hold the results of the detection
    HoughLines(output, lines, 1, CV_PI / 180, 150, 0, 0); // runs the actual detection

    // Draw the lines
    for (size_t i = 0; i < lines.size(); i++) {
        float rho = lines[i][0], theta = lines[i][1];
        Point pt1, pt2;
        double a = cos(theta), b = sin(theta);
        double x0 = a * rho, y0 = b * rho;
        pt1.x = cvRound(x0 + 1000 * (-b));
        pt1.y = cvRound(y0 + 1000 * (a));
        pt2.x = cvRound(x0 - 1000 * (-b));
        pt2.y = cvRound(y0 - 1000 * (a));
        line(cOutput, pt1, pt2, Scalar(0, 0, 255), 3, LINE_AA);
    }

    // Probabilistic Line Transform
    std::vector<Vec4i> linesP; // will hold the results of the detection
    HoughLinesP(output, linesP, 1, CV_PI / 180, 50, 50, 10); // runs the actual detection

    // Draw the lines
    for (size_t i = 0; i < linesP.size(); i++) {
        Vec4i l = linesP[i];
        line(cOutputP, Point(l[0], l[1]), Point(l[2], l[3]), Scalar(0, 0, 255), 3, LINE_AA);
    }

    // Show results
    imshow("Input Image", input);
    imshow("Detected Lines (in red) - Standard Hough Line Transform", cOutput);
    imshow("Detected Lines (in red) - Probabilistic Line Transform", cOutputP);

    // Wait and Exit
    waitKey();

    return 0;
}

