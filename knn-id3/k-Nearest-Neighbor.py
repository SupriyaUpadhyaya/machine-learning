import argparse
import csv
import math


def calculateWeight(k, case, nearestNeighbours):
    weight = []
    for i in range(k):
        d_k = math.sqrt((case[1] - nearestNeighbours[k-1][1]) ** 2 + (case[2] - nearestNeighbours[k-1][2]) ** 2)
        d_1 = math.sqrt((case[1] - nearestNeighbours[0][1]) ** 2 + (case[2] - nearestNeighbours[0][2]) ** 2)
        if d_k == d_1:
            weight.append(1)
        else:
            d_i = math.sqrt((case[1] - nearestNeighbours[i][1]) ** 2 + (case[2] - nearestNeighbours[i][2]) ** 2)
            weight.append((d_k - d_i) / (d_k - d_1))
    return weight


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", help="Input file")
    parser.add_argument("-k", "--k", help="k value")

    arg = parser.parse_args()
    input = arg.data
    k = int(arg.k)

    ToClassify = []
    count = 0
    casebase = []
    with open(input) as file:
        data = csv.reader(file)
        i = 0
        for value in data:
            temp = [str(value[0]), float(value[1]), float(value[2])]
            if i == 0:
                casebase.append(temp)

            nearestNeighbour = sorted(casebase, key=lambda x: math.sqrt((temp[1] - x[1]) ** 2 + (temp[2] - x[2]) ** 2),)
            nearestNeighbour = nearestNeighbour[:1]
            if nearestNeighbour[0][0] != temp[0]:
                casebase.append(temp)
            else:
                ToClassify.append(temp)
            i += 1

    for case in ToClassify:
        classification = "none"
        caseWeight = [0, 0]
        nearestNeighbour = sorted(casebase, key=lambda x: math.sqrt((case[1] - x[1]) ** 2 + (case[2] - x[2]) ** 2),)
        nearestNeighbour = nearestNeighbour[:k]
        weight = calculateWeight(k, case, nearestNeighbour)
        for i in range(k):
            if nearestNeighbour[i][0] == "A":
                caseWeight[0] += weight[i]
            else:
                caseWeight[1] += weight[i]

        if (caseWeight[0] > caseWeight[1]):
            classification = "A"
        else:
            classification = "B"

        if (classification != case[0]):
            count += 1

    print(count)
    for case in casebase:
        print(case[0] + "," + str(case[1]) + "," + str(case[2]))