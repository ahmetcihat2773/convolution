#pragma once

#include <iostream>
#include <vector>
#include<opencv2/opencv.hpp>

class ConvolutionHelper final {
private:
    // Images and Matrices
    cv::Mat input;
    cv::Mat input_gray;
    cv::Mat output;
    cv::Mat detected_edges;
    int lowThreshold = 0;
    const int max_lowThreshold = 100;
    const int ratio = 3;
    const int kernel_size = 3;

public:
    int loadImage(int argc, char** argv);
    void displayImage();
    int displayImage(cv::Mat image);
    void convolution(cv::Mat kernel);
    static void onChange(int pos, void* ptr);
    void cannyThreshold(int);
    int cannyEdge();
};