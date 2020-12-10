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
#include <opencv2/opencv.hpp>
#include "ConvolutionHelper.h"


// ------------------------------------------------------------------------------------------------------------
//                                                  THE MAIN
// ------------------------------------------------------------------------------------------------------------

int main(int argc, char** argv)
{

    // Create our helper class
    ConvolutionHelper convolutionHelper;

    // convolutionHelper.displayImage();

    // Canny Edge Detection
    //convolutionHelper.cannyEdge();

    // Laplacian Edge Detection
    convolutionHelper.laplacianEdge();

    // Hough Line Transform
    //convolutionHelper.houghLineTransform();

    return 0;

}
