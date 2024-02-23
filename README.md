# Coppeliasim Simulations Integrations with python

## Green Object Tracker Project
This Python script uses the CoppeliaSim remote API to track a green object in a vision sensor and overlay a rectangle marker around it.

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

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
