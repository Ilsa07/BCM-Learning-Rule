# Bienenstock Cooper Munro (BCM) Learning Rule

### Output of the Neuron

![output_equation](https://latex.codecogs.com/gif.latex?y%28t%29%3Dw%5ETx%28t%29)

### BCM Weight Update

![weight_update](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bdw%7D%7Bdt%7D%3D%5Ceta%20x%20y%28y-%5Ctheta%29)

### Sliding Threshold

![sliding_threshold](https://latex.codecogs.com/gif.latex?%5Ctau%20%5Cfrac%7Bd%20%5Ctheta%7D%7Bdt%7D%3D-%5Ctheta%20&plus;%20%5Cfrac%7By%28t%29%5E2%7D%7By_0%7D)

## Getting Started
1. Clone the project and create a virtual environment
2. Install the required packages in the virtual environment
      ```
      pip3 install -r requirements.txt
      ```
