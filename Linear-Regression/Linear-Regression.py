import numpy
import csv
import argparse

def executor():
    arg = parser.parse_args()
    data = arg.data
    eta = float(arg.eta)
    threshold = float(arg.threshold)
    
    with open(data) as input:
        reader = csv.reader(input, delimiter=',')
        X , Y = [], []
        for row in reader:
            X.append([1.0] + row[:-1])
            Y.append([row[-1]])
    
    length = len(X)
    X = numpy.array(X).astype(float)
    Y = numpy.array(Y).astype(float)
    W = numpy.zeros(X.shape[1]).astype(float)
    W = W.reshape(X.shape[1], 1)

    f_of_x = calculate_FofX(X, W)

    sse = calculate_sse(Y, f_of_x)

    output = "0,0,0,0," + str(sse) + "\n"
    gradient, W = calculate_gradient(W, X, Y, f_of_x, eta)

    i = 1
    while True:
        f_of_x = calculate_FofX(X, W)
        sseNew = calculate_sse(Y, f_of_x)

        if abs(sseNew - sse) > threshold:
            output += "," + str(i) + "," + str(W.T[0][0]) + "," + str(W.T[0][1]) + "," + str(W.T[0][2]) + "," + str(sseNew) + "\n"
            gradient, W = calculate_gradient(W, X, Y, f_of_x, eta)
            i += 1
            sse = sseNew
        else:
            break
    output += "," + str(i) + "," + str(W.T[0][0]) + "," + str(W.T[0][1]) + "," + str(W.T[0][2]) + "," + str(sseNew) + "\n"
    print(output)


def calculate_FofX(X, W):
    return numpy.dot(X, W)


def calculate_sse(Y, f_of_x):
    return numpy.sum(numpy.square(f_of_x - Y))


def calculate_gradient(W, X, Y, f_of_x, eta):
    g = (Y - f_of_x) * X
    gradient = numpy.sum(g, axis=0)
    t = numpy.array(eta * gradient).reshape(W.shape)
    W = W + t
    return gradient, W


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", help="Input file")
    parser.add_argument("-e", "--eta", help="Learning rate")
    parser.add_argument("-t", "--threshold", help="Threshold")
    executor()
