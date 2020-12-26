#pragma once

#include <iostream>
#include <vector>
#include<opencv2/opencv.hpp>

class ConvolutionHelper final {
private:
    // Images
    cv::Mat input;
    cv::Mat output;

    // Canny Edge
    cv::Mat input_gray;
    cv::Mat detected_edges;
    int lowThreshold = 0;
    const int max_lowThreshold = 100;
    const int ratio = 3;
    const int kernel_size = 3;

    // Laplacian Edge
    int scale = 1;
    int delta = 0;
    int ddepth = CV_16S;
    cv::Mat abs_output;

    // Hough Line Transform
    cv::Mat cOutput;
    cv::Mat cOutputP;

public:
    bool loadImage(std::string name);
    bool displayImage();
    bool displayImage(cv::Mat image);
    bool convolution(cv::Mat kernel);
    static void onChange(int pos, void* ptr);
    void cannyThreshold(int);
    bool cannyEdge();
    bool laplacianEdge();
    bool houghLineTransform();

};