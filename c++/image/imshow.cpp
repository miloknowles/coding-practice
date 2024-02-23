#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <string>
#include <cstdio>

int main( int argc, char** argv )
{
    printf("OpenCV: %s", cv::getBuildInformation().c_str());
    cv::Mat image;
    std::string path = "/home/milo/datasets/asl/vicon_room_01/cam0/data/1403715273462142976.png";
    image = cv::imread(path, CV_LOAD_IMAGE_GRAYSCALE);   // Read the file

    if(!image.data) {
        std::cout <<  "Could not open or find the image" << std::endl ;
        return -1;
    }
    namedWindow( "Display window", cv::WINDOW_AUTOSIZE );
    cv::imshow( "Display window", image);
    cv::waitKey(0);
    return 0;
}

// Compile: g++ imshow.cpp `pkg-config --libs --cflags opencv`