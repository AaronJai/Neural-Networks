import math
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline                    # Won't work outside jupyter notebook, use .show() instead. Example below.

# Example
# # Create data
# x = np.linspace(0, 2 * math.pi, 100)
# y = np.sin(x)

# # Create the plot
# plt.plot(x, y)

# # Add labels and title
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Plot of sin(x)')

# # Display the plot
# plt.show()

class Value:
    
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self._prev = set(_children)
        self._op = _op
        
    def __repr__(self):                             # __repr__ is used to return a string representation of the object, otherwise it returns an address
        return f"Value(data={self.data})"

    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), '+')
        return out
    
    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), '*')
        return out


a = Value(2.0)
b = Value(-3.0)
c = Value(10.0)
d = a * b + c
print(a)
print(b)
print(a + b)                                        # internally calls a.__add__(b)                         -- (a is self, b is other)
print(a * b + c)                                    # internally calls (a.__mul__(b)).__add__(c)            -- (a is self, b is other)
print(d)
print(d._prev)
print(d._op)

# From here, expressions get larger and we want a way to visualise these expressions.

from graphviz import Digraph

def trace(root):
    # builds a set of all nodes and edges in a graph
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add(child, v)
                build(child)
    build(root)
    return nodes, edges

# create a new function 'draw_dot' we can call on some root node and visualise it.
def draw_dot(root):
    dot = Digraph(format='svg', graph_attr={'rankdir': 'LR'}) # LR = left to right
    
    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))
        # for any value in the graph, create a rectangular ('record') node for it
        dot.node(name = uid, label = "{ data %.4f }" % (n.data, ), shape='record')
        if n._op:
            # if this value is a result of some operation, create an op node for it
            dot.node(name = uid + n._op, label = n._op)
            # and connect this node to it
            dot.edge(uid + n._op, uid)
    
    for n1, n2 in edges:
        # connect n1 to the op node of n2
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)

    return dot

draw_dot(d)