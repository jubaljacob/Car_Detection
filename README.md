# Car and Pedestrian Detection Project

![Car and Pedestrian Detection](images/demo.gif)

This project demonstrates real-time car and pedestrian detection using Python, Mediapipe, Haar cascades, and OpenCV. The combination of these technologies allows us to identify and track vehicles and pedestrians in a video stream or from a webcam.

## Features

- Real-time car and pedestrian detection
- Detection using Haar cascades and Mediapipe
- Tracking of detected objects
- Video stream or webcam support
- Easy-to-use Python script

## Requirements

To run this project, you need to have the following dependencies installed:

- Python 3.7+
- OpenCV (`pip install opencv-python`)
- Mediapipe (`pip install mediapipe`)

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/car-pedestrian-detection.git
```

2. Change into the project directory:

```bash
cd Car_Detection
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the car and pedestrian detection script, use the following command:

```bash
python car_ai.py
```

The script will open a video stream from your webcam by default. You can modify the `detect.py` file to process a different video file or modify other parameters such as the detection confidence threshold.

## How it Works

The car and pedestrian detection algorithm works as follows:

1. Capturing video frames from a webcam or a video file.
2. Preprocessing the frames for better detection performance.
3. Applying the Haar cascades classifier to detect cars and pedestrians.
4. Drawing bounding boxes around the detected objects.
5. Tracking the detected objects across frames using Mediapipe.
6. Displaying the processed frames with the detected objects.

The Haar cascades provide trained models for detecting cars and pedestrians based on their specific features. Mediapipe helps with object tracking, ensuring that the objects are consistently tracked even when they move within the frame.

## Example Output

Here is an example output of the car and pedestrian detection:

![Example Output](https://github.com/jubaljacob/Car_Detection/blob/main/car.gif)

## Contributing

Contributions are welcome! If you find any issues or want to enhance the project, feel free to submit a pull request. Please make sure to follow the project's coding style and guidelines.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

This project was inspired by the amazing work done by the OpenCV, Mediapipe, and Haar cascades communities. Special thanks to all the contributors and the open-source community for their valuable contributions.

