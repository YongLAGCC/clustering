from collections import defaultdict
from math import inf, sqrt
import random
import pandas as pd


def point_avg(points):
    center_point = [0] * len(points[0])
    for curr_point in points:
        for j in range(len(curr_point)):
            center_point[j] += curr_point[j]
    for i in range(len(center_point)):
        center_point[i] = center_point[i] / len(points)

    return center_point
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    # raise NotImplementedError()


def update_centers(data_set, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    centers = []
    assignment_dict = defaultdict(list)
    for i in range(len(assignments)):
        if assignments[i] not in assignment_dict:
            assignment_dict[assignments[i]] = [data_set[i]]
        else:
            assignment_dict[assignments[i]] += [data_set[i]]
    for j in assignment_dict:
        centers.append(point_avg(assignment_dict[j]))

    return centers


def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments

def distance(a, b):
    squared_distance = 0
    for i in range(len(a)):
        squared_distance += (a[i] - b[i]) ** 2
    return sqrt(squared_distance)

    """
    Returns the Euclidean distance between a and b
    """
    # raise NotImplementedError()


def generate_k(data_set, k):

    return random.sample(population=data_set, k=k)
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    # raise NotImplementedError()


def get_list_from_dataset_file(dataset_file):
    dataset = pd.read_csv(dataset_file, names=['col1', 'col2'])
    data = dataset.values.tolist()
    return data



def cost_function(clustering):

    if clustering is None or len(clustering) ==0:
        raise Exception("missding input")
    ret = 0
    for ( k, v) in clustering.items():
        centroid = point_avg(v)
        for point in v:
            ret += distance(centroid, point) **2
    return ret
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



