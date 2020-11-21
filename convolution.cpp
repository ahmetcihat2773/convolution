/*
*   ___ ___  _  ___   _____  _   _   _ _____ ___ ___  _  _
*  / __/ _ \| \| \ \ / / _ \| | | | | |_   _|_ _/ _ \| \| |
* | (_| (_) | .` |\ V / (_) | |_| |_| | | |  | | (_) | .` |
*  \___\___/|_|\_| \_/ \___/|____\___/  |_| |___\___/|_|\_|
*
*   Armin Niedermüller, Ahmet Cihat Bozkur
*
*/


#include <iostream>
#include<opencv2/opencv.hpp>


// ------------------------------------------------------------------------------------------------------------
//                                                  THE MAIN
// ------------------------------------------------------------------------------------------------------------

int main(int argc, char** argv)
{

    // Load our Image -
    cv::Mat img = cv::imread("images/harold_original.jpg");
    cv::namedWindow("image", cv::WINDOW_NORMAL);
    cv::imshow("image", img);
    cv::waitKey(0);
    return 0;

}
