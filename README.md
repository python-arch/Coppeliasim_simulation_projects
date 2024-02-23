# Introduction
This repository showcases how Python can be integrated with CoppeliaSim, a versatile robotics simulation software, using its remote API. The remote API allows Python scripts to interact with CoppeliaSim, enabling a wide range of applications such as robot control, simulation automation, Autonomous and Deep learning related tasks.
## Green Object Tracker
This Python script uses the CoppeliaSim remote API to track a green object in a vision sensor and overlay a rectangle marker around it. If you are a beginner to Coppeliasim this project will be a good start for you to get familiar with the primitive shapes objects , Vision Sensors , interacting with coppeliasim through `zmqremoteAPI`

### Requirements
- Python 3
- OpenCV (`pip install opencv-python`)
- numpy (`pip install numpy`)
- CoppeliaSim

### Usage
1. Start CoppeliaSim and load your scene.
2. Adjust the vision sensor handles (`v_0_handle` and `v_1_handle`) to match your scene.
3. Run the script and enter the simulation time in seconds when prompted.
4. The script will track the green object in the vision sensor and save images with rectangles to the `output` directory.

## Sample Output
![project 1 Image](project1_output.png)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
