# Self-Driving-Car-in-UdaCity
This project implements a Convolutional Neural Network (CNN) to control the steering of a simulated self-driving car using camera images. Built using Python and TensorFlow/Keras, the model is trained on driving data collected from the Udacity Self-Driving Car Simulator.

The pipeline includes image preprocessing (resizing, normalization, color space transformation), data augmentation, model creation inspired by NVIDIA’s end-to-end architecture, and model training using Mean Squared Error loss. The output is a trained model capable of predicting steering angles in real-time based on visual input.

This project demonstrates a foundational step in behavioral cloning for autonomous vehicle control.

##                           Left                 |                         Center                              |                               Right

![Left](https://github.com/Agastya122/Self-Driving-Car-in-UdaCity/blob/main/left_2025_08_02_19_45_39_421.jpg?raw=true) | ![Center](https://github.com/Agastya122/Self-Driving-Car-in-UdaCity/blob/main/center_2025_08_02_19_45_39_421.jpg?raw=true) | ![Right](https://github.com/Agastya122/Self-Driving-Car-in-UdaCity/blob/main/right_2025_08_02_19_45_39_421.jpg?raw=true)


## Output

Before feeding the images into the model, a series of preprocessing steps are applied to ensure that the input data is clean, focused, and standardized. First, each image is cropped to remove the top portion containing the sky and the bottom portion showing the car’s hood, allowing the model to concentrate on the road ahead. After cropping, the images are resized to a fixed shape, typically 66x200 pixels, to match the input requirements of the NVIDIA architecture. The pixel values are then normalized, usually by scaling them to a range between 0 and 1, which helps in faster and more stable model training. The color space of the image is converted from RGB to YUV, as used in the original NVIDIA model.

![Output](https://github.com/Agastya122/Self-Driving-Car-in-UdaCity/blob/main/output.png?raw=true)
