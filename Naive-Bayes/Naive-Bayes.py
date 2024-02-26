import argparse
import csv
import math
from statistics import mean 

def getValues(feature, category):
    
    class_a, class_b, data_a, data_b = [], [], [], []

    for i in range(len(category)):
        if category[i]=='A':
            class_a.append(category[i])
            data_a.append(feature[i])
        elif category[i]=='B':
            class_b.append(category[i])
            data_b.append(feature[i])

    return data_a, data_b, class_a, class_b

def calculate_variance(numbers, mean_num):
    avg = mean_num
    variance = sum([(x-avg)**2 for x in numbers]) / float(len(numbers)-1)
    return variance


def calculate_probability(x, mean, variance):
    exponent = math.exp(-((x-mean)**2 / (2 * variance )))
    return (1 / (math.sqrt(2 * math.pi*variance))) * exponent

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", help="Input file")

    arg = parser.parse_args()
    data = arg.data

    with open(data) as input:
        reader = csv.reader(input, delimiter=',')
        category, feature1, feature2 = [], [], []
        for dataA, dataB, dataC in reader:
            category.append(dataA)
            feature1.append(float(dataB))
            feature2.append(float(dataC))

    length = len(category)

    data_a_1, data_b_1, class_a_1, class_b_1 = getValues(feature1, category)
    data_a_2, data_b_2, class_a_2, class_b_2 = getValues(feature2, category)


    prob_a_1 = len(class_a_1)/len(category)
    prob_b_1 = len(class_b_1)/len(category)

    prob_a_2 = len(class_a_2)/len(category)
    prob_b_2 = len(class_b_2)/len(category)

    mu_a_1 = mean(data_a_1)
    mu_b_1 = mean(data_b_1)

    mu_a_2 = mean(data_a_2)
    mu_b_2 = mean(data_b_2)

    variance_a_1 = calculate_variance(data_a_1, mu_a_1)
    variance_b_1 = calculate_variance(data_b_1, mu_b_1)

    variance_a_2 = calculate_variance(data_a_2, mu_a_2)
    variance_b_2 = calculate_variance(data_b_2, mu_b_2)


    failure = 0
    for i in range(length):

        gaus_a_1 = calculate_probability(feature1[i], mu_a_1, variance_a_1)
        gaus_b_1 = calculate_probability(feature1[i], mu_b_1, variance_b_1)

        gaus_a_2 = calculate_probability(feature2[i], mu_a_2, variance_a_2)
        gaus_b_2 = calculate_probability(feature2[i], mu_b_2, variance_b_2)



        p_a = prob_a_1*gaus_a_1*gaus_a_2
        p_b = prob_b_1*gaus_b_1*gaus_b_2


        if p_a > p_b:
            clss = "A"
        elif p_b > p_a:
            clss = "B"
        else:
            pass

        if category[i]!=clss:
            failure+=1

    print(str(mu_a_1) + " " + str(variance_a_1) + " " + str(mu_a_2) + " " + str(variance_a_2) + " " + str(prob_a_1))
    print(str(mu_b_1) + " " + str(variance_b_1) + " " + str(mu_b_2) + " " + str(variance_b_2) + " " + str(prob_b_1))
    print(failure)