# TRAINING A NEURAL NET

## Micrograd
Micrograd was first built by Andrej Karpathy which is like an Autograd (automatic gradient) engine which implements backpropagation (an algorithm that
allows you to efficiently evaluate the gradient of a loss function with respect to the weights of a neural network).
This allows us to iteratively tune the weights of that neural network to minimise the loss function and therefore improve the accuracy of the network.

It does this over a dynamically built DAG and a small neural networks on top of it with a PyTorch-like API.
> DAG operates over scalar values - we 'chop' each neuron into its individual add and multiple components.

### Consisting of total ~150 lines of code, this is sufficient to understand **neural network training** while 'everything' else is just efficiency.