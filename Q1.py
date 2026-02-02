def perceptron_epoch(X, y, w, b, lr):
    for i in range(len(X)):
        activation = sum(w[j] * X[i][j] for j in range(len(w))) + b
        if y[i] * activation <= 0:
            for j in range(len(w)):
                w[j] += lr * y[i] * X[i][j]
            b += lr * y[i]
    return [w, b]
