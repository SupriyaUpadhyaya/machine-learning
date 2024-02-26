import argparse
import csv
import math


def executor():
    w_bias_h1, w_a_h1, w_b_h1 = 0.20000, -0.30000,	0.40000
    w_bias_h2, w_a_h2, w_b_h2 = -0.50000, -0.10000, -0.40000
    w_bias_h3, w_a_h3, w_b_h3 = 0.30000, 0.20000, 0.10000
    w_bias_o, w_h1_o, w_h2_o, w_h3_o = -0.10000, 0.10000, 0.30000, -0.40000

    arg = parser.parse_args()
    data = arg.data
    learning = float(arg.eta)
    iterations = int(arg.iterations)
    #print("a,b,h1,h2,h3,o,t,delta_h1,delta_h2,delta_h3,delta_o,w_bias_h1,w_a_h1,w_b_h1,w_bias_h2,w_a_h2,w_b_h2,w_bias_h3,w_a_h3,w_b_h3,w_bias_o,w_h1_o,w_h2_o,w_h3_o")
    print("- - - - - - - - - - - " + str(w_bias_h1) + " " + str(w_a_h1) + " " + str(w_b_h1) + " " + str(w_bias_h2) + " " + str(w_a_h2) + " " + str(w_b_h2) + " " + str(w_bias_h3) + " " + str(w_a_h3) + " " + str(w_b_h3) + " " + str(w_bias_o) + " " + str(w_h1_o) + " " + str(w_h2_o) + " " + str(w_h3_o))
    for i in range(iterations):
        w_bias_h1, w_a_h1, w_b_h1, w_bias_h2, w_a_h2, w_b_h2, w_bias_h3, w_a_h3, w_b_h3, w_bias_o, w_h1_o, w_h2_o, w_h3_o = update_weights(data, learning, w_bias_h1, w_a_h1, w_b_h1, w_bias_h2, w_a_h2, w_b_h2, w_bias_h3, w_a_h3, w_b_h3, w_bias_o, w_h1_o, w_h2_o, w_h3_o)

    pass


def update_weights(data, learning, w_bias_h1, w_a_h1, w_b_h1, w_bias_h2, w_a_h2, w_b_h2, w_bias_h3, w_a_h3, w_b_h3, w_bias_o, w_h1_o, w_h2_o, w_h3_o):
    with open(data) as input:
        reader = csv.reader(input, delimiter=',')
        a, b, t = [], [], []
        for dataA, dataB, dataC in reader:
            a.append(float(dataA))
            b.append(float(dataB))
            t.append(float(dataC))

    length = len(a)
    bias = 1
    for i in range(length):
        h1 = calculate_hidden_layer_output(w_a_h1, w_b_h1, w_bias_h1, a[i], b[i], bias)
        h2 = calculate_hidden_layer_output(w_a_h2, w_b_h2, w_bias_h2, a[i], b[i], bias)
        h3 = calculate_hidden_layer_output(w_a_h3, w_b_h3, w_bias_h3, a[i], b[i], bias)
        o = calculate_output(w_h1_o, w_h2_o, w_h3_o, w_bias_o, h1, h2, h3, bias)
        delta_o = calculate_delta_output(o, t[i])
        delta_h1 = calculate_delta_hidden_layer(h1, delta_o, w_h1_o)
        delta_h2 = calculate_delta_hidden_layer(h2, delta_o, w_h2_o)
        delta_h3 = calculate_delta_hidden_layer(h3, delta_o, w_h3_o)

        w_a_h1 = calculate_updated_weight(w_a_h1, learning, delta_h1, a[i])
        w_b_h1 = calculate_updated_weight(w_b_h1, learning, delta_h1, b[i])
        w_bias_h1 = calculate_updated_weight(w_bias_h1, learning, delta_h1, bias)

        w_a_h2 = calculate_updated_weight(w_a_h2, learning, delta_h2, a[i])
        w_b_h2 = calculate_updated_weight(w_b_h2, learning, delta_h2, b[i])
        w_bias_h2 = calculate_updated_weight(w_bias_h2, learning, delta_h2, bias)

        w_a_h3 = calculate_updated_weight(w_a_h3, learning, delta_h3, a[i])
        w_b_h3 = calculate_updated_weight(w_b_h3, learning, delta_h3, b[i])
        w_bias_h3 = calculate_updated_weight(w_bias_h3, learning, delta_h3, bias)

        w_h1_o = calculate_updated_weight(w_h1_o, learning, delta_o, h1)
        w_h2_o = calculate_updated_weight(w_h2_o, learning, delta_o, h2)
        w_h3_o = calculate_updated_weight(w_h3_o, learning, delta_o, h3)
        w_bias_o = calculate_updated_weight(w_bias_o, learning, delta_o, bias)
        print(str(round(a[i], 5)) + " " + str(round(b[i], 5)) + " " + str(round(h1, 5)) + " " + str(round(h2, 5)) + " " + str(round(h3, 5)) + " " + str(round(o, 5)) + " " + str(int(t[i])) + " " + str(round(delta_h1, 5)) + " " + str(round(delta_h2, 5)) + " " + str(round(delta_h3, 5)) + " " + str(round(delta_o, 5)) + " " + str(round(w_bias_h1, 5)) + " " + str(round(w_a_h1, 5)) + " " + str(round(w_b_h1, 5)) + " " + str(round(w_bias_h2, 5)) + " " + str(round(w_a_h2, 5)) + " " + str(round(w_b_h2, 5)) + " " + str(round(w_bias_h3, 5)) + " " + str(round(w_a_h3, 5)) + " " + str(round(w_b_h3, 5)) + " " + str(round(w_bias_o, 5)) + " " + str(round(w_h1_o, 5)) + " " + str(round(w_h2_o, 5)) + " " + str(round(w_h3_o, 5)))
        i += 1

    return (w_bias_h1, w_a_h1, w_b_h1, w_bias_h2, w_a_h2, w_b_h2, w_bias_h3, w_a_h3, w_b_h3, w_bias_o, w_h1_o, w_h2_o, w_h3_o)


def calculate_hidden_layer_output(w_a: float, w_b: float, w_bias: float, a: float, b: float, bias: float) -> float:
    net = (w_a * a) + (w_b * b) + (w_bias * bias)
    output = 1 / (math.exp(-net) + 1)
    return output


def calculate_output(w_h1_o: float, w_h2_o: float, w_h3_o: float, w_bias_o: float, h1: float, h2: float, h3: float, bias: float) -> float:
    net = (w_h1_o * h1) + (w_h2_o * h2) + (w_h3_o * h3) + (w_bias_o * bias)
    output = 1 / (math.exp(-net) + 1)
    return output


def calculate_delta_output(output: float, targer: float) -> float:
    return (output * (1 - output) * (targer - output))


def calculate_delta_hidden_layer(h: float, output: float, weight: float) -> float:
    return (h * (1 - h) * (weight * output))


def calculate_updated_weight(old_weight: float, learning: float, delta: float, input: float):
    return (old_weight + (learning * delta * input))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", help="Input file")
    parser.add_argument("-e", "--eta", help="Learning rate")
    parser.add_argument("-t", "--iterations", help="Number of iterations")
    executor()