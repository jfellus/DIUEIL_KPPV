import struct

import numpy as np


def read_train_images():
    return read_idx('mnist/train-images.idx3-ubyte').reshape(-1,784)
def read_test_images():
    return read_idx('mnist/t10k-images.idx3-ubyte').reshape(-1,784)
def read_train_labels():
    return read_idx('mnist/train-labels.idx1-ubyte')
def read_test_labels():
    return read_idx('mnist/t10k-labels.idx1-ubyte')

def read_idx(filename):
    with open(filename, 'rb') as f:
        zero, data_type, dims = struct.unpack('>HBB', f.read(4))
        shape = tuple(struct.unpack('>I', f.read(4))[0] for d in range(dims))
        return np.fromstring(f.read(), dtype=np.uint8).reshape(shape)
