# Bienenstock Cooper Munro (BCM) Learning Rule
The BCM learning rule targets to explain how learning works on the neuron level. This simulations shows how a neruon becomes selective, or learns to respond to only one type of stimulus, to input stimulus by randomly inputting one of two patterns to the neuron and implementing the rule. The BCM learning rule implements a sliding threshold simulating synaptic plasticity in the brain. It can be seen on the graphs at the end of the simulation that one synaptic weight increases and the other decreases for the two inputs and the output of the neuron is either high or low, depending on what is inputted to the neuron, depicting selectivity learning.

### Output of the Neuron
The output of the neuron depends on the input and the synaptic weights and is determined by the following equation, where w is the synaptic weight and x is the input.

![output_equation](https://latex.codecogs.com/gif.latex?y%28t%29%3Dw%5ETx%28t%29)

### BCM Weight Update
The following equation is used to update the synaptic weights of the neuron depending, where w are the synaptic weights, x is the input, y is the output of the neuron and theta is the threshold.

![weight_update](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bdw%7D%7Bdt%7D%3D%5Ceta%20x%20y%28y-%5Ctheta%29)

### Sliding Threshold
The following equation is used to update the sliding threshold, where tau is the time constant, theta  is the threshold and y is the output of the neuron with y0 being the target response.This is computed online in the program.

![sliding_threshold](https://latex.codecogs.com/gif.latex?%5Ctau%20%5Cfrac%7Bd%20%5Ctheta%7D%7Bdt%7D%3D-%5Ctheta%20&plus;%20%5Cfrac%7By%28t%29%5E2%7D%7By_0%7D)

## Getting Started
1. Clone the project and create a virtual environment
2. Install the required packages in the virtual environment
      ```
      pip3 install -r requirements.txt
      ```
