#pragma once

#include <iostream>
#include <vector>
#include<opencv2/opencv.hpp>

class TransformationCalculator final
{
    // Step counter
    uint step = 1;

    // Steps switch
    bool parameter1 = false;

    // Loaded Image
    cv::Mat img;

public:
    int run(int argc, char** argv);

private:
    void loadImage();
    void displayImage();
    std::pair<bool, int> ProcessArguments(int argc, char** argv);
};