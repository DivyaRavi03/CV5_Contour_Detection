# Project 05: Contour Detection with OpenCV

This project finds and draws the contours of objects within an image. It uses the grayscale conversion and binary thresholding of an image to perform higher-level shape analysis.

## Features

-   Loads an image and converts it to grayscale.
-   Applies a binary threshold to create a high-contrast, that is black-and-white image with no shades of gray which is suitable for contour detection.
-   Uses 'cv2.findContours()' to detect all distinct object outlines.
-   Visualizes and draws the results by of all found contours onto the color copied image using 'cv2.drawContours()'.

## Technologies Used

-   Python
-   OpenCV
-   NumPy

## Key Concepts Learned

-   **Image Thresholding:** The process of converting a grayscale image to a binary image, a critical preprocessing step for many CV tasks.
-   **Contour Detection:** The process of identifying the boundaries of objects in a binary image and providing a list of shapes for further analysis.
-   **Data Visualization:** Overlaying the results (the contours) on the copied image to provide clear, visual feedback.
