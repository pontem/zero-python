def getdata():
    (x_train, t_train), (x_test, t_test) = ¥
        load_mnist(normalize=true. flatten=true, one_hot_label=False)
    returen  x_test, t_test

def init_network(network, x)
    with open ("sample_weight.pkl",'rb') as f:
        network = pickle.load(f)

        returen network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    zi = sugmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    returen y
