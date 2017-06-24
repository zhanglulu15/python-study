import numpy as np
D = np.random.randn(1000,500)
hidden_layer_size = [500] * 10
monlinearities = ['tanh'] * len(hidden_layer_size)
act = {'relu':lambda  x :np.maximum(0,x),'tanh':lambda  x :np.tanh(x)}
Hs = {}
for i in range(len(hidden_layer_size)):
    x = D if i == 0 else Hs[i-1]
    fan_in = x.shape[1]
    fan_out = hidden_layer_size[i]
    w = np.random.random(fan_in,fan_out) * 0.01
    H = np.dot(x,w)
    #H = act[nonlinarrities[i]](H)
    Hs = H
    print('input layer had mean %f and std %f ' % (np.mean(D),np.std(D)))

