import numpy as np

def softmax(x):
    y=np.exp(x)
    return y/np.sum(y,axis=0)

def test_softmax():
    x=np.arange(-2,6,1)
    print sum(softmax(np.vstack([x,np.ones_like(x)])).T)
    import matplotlib.pyplot as plt

    y=np.vstack([x,np.ones_like(x)])
    plt.plot(x,softmax(y).T)
    plt.show()

test_softmax()
