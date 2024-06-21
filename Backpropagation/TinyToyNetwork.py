import numpy as np

# sigmoid function
def nonlin(x,deriv=False):      # Maps a sigmoid function (mapping any value to a value between 0 and 1)
    if(deriv==True):            #
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
# input dataset, each row is a single 'training example', each column is one input node. (i.e., 3 input nodes and 4 training examples)
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])
    
# output dataset, (one output).
y = np.array([[0,0,1,1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((3,1)) - 1        # since we only have 2 layers (input,output) we only need 1 matrix of weights to connect them. dimension is (3,1) since 3 inputs, 1 output

for iter in range(10000):

    # forward propagation
    l0 = X                                  # first layer is simply our data. processing all our training examples (4) at the same time = "full batch" training. we have 4 different l0 rows.
    l1 = nonlin(np.dot(l0,syn0))            # prediction step. we let network try to predict output given input.

    # how much did we miss?
    l1_error = y - l1                       # a vector of psoitive and negative numbers reflecting how much the network missed

    # multiply how much we missed by the 
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1,True)   # computes the weight updates for each weight for each training example, sums them, and updates the weights

    # update weights
    syn0 += np.dot(l0.T,l1_delta)

print("Output After Training:")
print(l1)



"""
    This is a Layer Neural Network

    Variables:
        X:          Input dataset matrix where each row is a training example.
        y:          Output dataset matrix where each row is a training example.
        l0:         First Layer of the Network, specified by the input data.
        l1:	        Second Layer of the Network, otherwise known as the hidden layer.
        syn0:	    First layer of weights, Synapse 0, connecting l0 to l1.
        * :	        Elementwise multiplication, so two vectors of equal size are 
                    multiplying corresponding values 1-to-1 to generate a final vector of 
                    identical size.
        - :	        Elementwise subtraction, so two vectors of equal size are subtracting 
                    corresponding values 1-to-1 to generate a final vector of identical size.
        x.dot(y): 	If x and y are vectors, this is a dot product. If both are matrices, it's 
                    a matrix-matrix multiplication. If only one is a matrix, then it's vector 
                    matrix multiplication.
    
    Returns:

"""

# Numpy is a linear algebra library