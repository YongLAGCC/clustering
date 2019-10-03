from collections import defaultdict
from math import inf
import random
import csv


def point_avg(points):
    center_point = [0] * len(points[0])
    for curr_point in points:
        for j in range(len(curr_point)):
            center_point[j]+=curr_point[j]
    for i in range(len(center_point)):
        center_point[i] = center_point[i]/len(points)
    return center_point


"""
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
        
        
        # raise NotImplementedError()


def update_centers(data_set, assignments):
    clustering = defaultdict(list)
    for assign, point in zip(assignments,  data_set):
        clustering[assign].append(point)
    
    
    centers = []
    for k in clustering.keys():
        centers.append(point_avg(clustering[k]))
    return centers

"""
    Accepts a dataset and a list of assignments; the indexes
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
        # raise NotImplementedError()


def assign_points(data_points, centers):
    """
        """
    assignments = []
    for p in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(p, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    d = 0
    for (i, j) in zip(a, b):
        d +=(i - j)**2
    return 0.5 ** d



def generate_k(data_set, k):
    return random.sample(data_set, k)
    
    """
        Given `data_set`, which is an array of arrays,
        return a random set of k points from the data_set
        """
    raise NotImplementedError()


def get_list_from_dataset_file(dataset_file):
    dataset=[]
    with open(dataset_file) as file:
        csv_reader=csv.reader(file)
        for r in csv_reader:
            new_points = []
            for n in range(0,len(r)):
                row = int(r[n])
                new_points.append(row)
                dataset.append(new_points)
    return dataset
# raise NotImplementedError()


def cost_function(clustering):
    
    c = 0;
    for k in clustering.keys():
        points = clustering[k]
        center = point_avg( points)
        for p in points:
            c +=distance(center,p )**2
        return c;
# raise NotImplementedError()


def k_means(dataset_file, k):
    dataset = get_list_from_dataset_file(dataset_file)
    k_points = generate_k(dataset, k)
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering
