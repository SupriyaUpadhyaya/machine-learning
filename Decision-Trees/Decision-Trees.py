import sys
import math
import argparse
import pandas as pd
import numpy as np


def getfeatures(df_value):
    op = {}
    for i in df_value.keys()[:-1]:
        op[i] = getEntropy(df_value)-getFeatureEntropy(df_value, i)
    return max(op, key=op.get)


def getFeatureEntropy(df_value, item):
    Class = df_value.keys()[-1]
    target_variables = df_value[Class].unique()
    variables = df_value[item].unique()
    weighted_entropy = 0
    for variable in variables:
        entropy = 0
        for target_variable in target_variables:
            numerator = len(df_value[item][df_value[item] == variable][df_value[Class] == target_variable])
            denominator = len(df_value[item][df_value[item] == variable])
            fraction = numerator/(denominator)
            entropy += -fraction*math.log(fraction + eps, log_base)
        weights = denominator/len(df_value)
        weighted_entropy += -weights*entropy
    return abs(weighted_entropy)


def getSubset(df_value, newNode, value):
    return df_value[df_value[newNode] == value].drop(newNode, axis=1).reset_index(drop=True)


def getEntropy(df_value):
    new_class = df_value.keys()[-1]
    entropy_value = 0
    values = df_value[new_class].unique()
    for item in values:
        fraction = df_value[new_class].value_counts()[item]/len(df_value[new_class])
        entropy_value += -fraction*math.log(fraction, log_base)
    return entropy_value


def getCommonClass(df_value):
    classes = list(df_value.iloc[:, -1])
    return max(set(classes), key=classes.count)


def growtree(df_value, depth=None):
    if depth is None:
        depth = 0
        print('{},root,{},no_leaf'.format(depth, getEntropy(df_value)))
        depth = depth+1

    newNode = getfeatures(df_value)

    attributeValue = np.unique(df_value[newNode])

    for item in attributeValue:

        subset = getSubset(df_value, newNode, item)
        value, counts = np.unique(subset['y'], return_counts=True)

        if len(counts) == 1:
            print('{},{}={},{},{}'.format(depth, newNode, item, getEntropy(subset), value[0]))

        elif len(df_value.columns) == 1:
            print('{},{}={},{},{}'.format(depth, newNode, item, getEntropy(subset), getCommonClass(subset)))

        else:
            print('{},{}={},{},no_leaf'.format(depth, newNode, item, getEntropy(subset)))
            growtree(subset, depth+1)

    return None


if __name__ == "__main__":
    sys.stdout = open('my_sol.txt','w')

    parser = argparse.ArgumentParser()
    parser.add_argument("--data", help="dateset")
    args = parser.parse_args()
    data = args.data
    df_value = pd.read_csv(data)

    names = ['att'+str(i) for i in range(len(df_value.columns)-1)]
    names.append('y')
    df_value = pd.read_csv(data, names=names)
    log_base = len(df_value.iloc[:, -1].unique())
    eps = np.finfo(float).eps

    growtree(df_value)

    with open("my_sol.txt", "w+") as file:
        for line in file:
            print(line)
