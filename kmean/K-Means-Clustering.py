import argparse
import csv
import math

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", help="Input file")

    arg = parser.parse_args()
    input = arg.data
    instances = []
    with open(input) as file:
        data = csv.reader(file)
        for value in data:
            temp = [float(value[1]), float(value[2])]
            instances.append(temp)
    
    output_centers = []
    output_msw = []
    mse = 0
    c1_center = [0, 5]
    c2_center = [0, 4]
    c3_center = [0, 3]

    new_centers = str(c1_center[0]) + "," + str(c1_center[1]) + "\t" + str(c2_center[0]) + "," + str(c2_center[1]) + "\t" + str(c3_center[0]) + "," + str(c3_center[1])
    output_centers.append(new_centers)

    flag = True
    while flag == True:
        c1_instances = []
        c2_instances = []
        c3_instances = []
        mse = 0

        for item in instances:
            dist_c1_center = (c1_center[0] - item[0]) ** 2 + (c1_center[1] - item[1]) ** 2
            dist_c2_center = (c2_center[0] - item[0]) ** 2 + (c2_center[1] - item[1]) ** 2
            dist_c3_center = (c3_center[0] - item[0]) ** 2 + (c3_center[1] - item[1]) ** 2

            minimum = min(dist_c1_center, dist_c2_center, dist_c3_center)
            mse += minimum
            if minimum == dist_c1_center:
                c1_instances.append(item)
            elif minimum == dist_c2_center:
                c2_instances.append(item)
            elif minimum == dist_c3_center:
                c3_instances.append(item)

        c1_x, c2_x, c3_x, c1_y, c2_y, c3_y = 0, 0, 0, 0, 0, 0
        for item in c1_instances:
            c1_x += (item[0])
            c1_y += (item[1])

        for item in c2_instances:
            c2_x += (item[0])
            c2_y += (item[1])
        
        for item in c3_instances:
            c3_x += (item[0])
            c3_y += (item[1])

        if len(output_msw) > 1:
            if mse == output_msw[len(output_msw) - 1]:
                flag = False
            else:
                output_msw.append(mse)
        else:
            output_msw.append(mse)

        c1_center[0] = (c1_x / len(c1_instances))
        c1_center[1] = (c1_y / len(c1_instances))

        c2_center[0] = (c2_x / len(c2_instances))
        c2_center[1] = (c2_y / len(c2_instances))

        c3_center[0] = (c3_x / len(c3_instances))
        c3_center[1] = (c3_y / len(c3_instances))
        
        new_centers = str(c1_center[0]) + "," + str(c1_center[1]) + "\t" + str(c2_center[0]) + "," + str(c2_center[1]) + "\t" + str(c3_center[0]) + "," + str(c3_center[1])

        if flag == True:
            output_centers.append(new_centers)
    
    for item in output_msw:
        print(item)
    output_centers = output_centers[:len(output_centers)-1]
    for item in output_centers:
        print(item)
    print("")    
