'''
## Grundläggande algoritmen:
# 1. Läs in datan och spara i lämplig datastruktur (pichu.txt, pikachu.txt)
# 2. Plotta alla punkterna med olika färger i samma fönster
# 3. Läs in testpunkter (test_points.txt)
# 4. Beräkna avstånd mellan testpunkt och övriga punkter
# 5. Närmaste punkten tillhör Pichu? ...
#  ->  JA = Klassificera testpunkt som Pichu
#  ->  NEJ = Klassificera testpunkt som Pikachu

## The answer key for the given test data:
# Sample with (width, height): (25, 35) classified as Pikachu
# Sample with (width, height): (15, 14) classified as Pichu
# Sample with (width, height): (26, 30) classified as Pichu
# Sample with (width, height): (22, 45) classified as Pikachu
'''

import numpy as np
import matplotlib.pyplot as plt
import re
from paths import data_paths 
#import pdb; pdb.set_trace()# Debugging with venv

# Data path from paths.py imported as data_paths
pichu_data = data_paths['pichu']
pikachu_data = data_paths['pikachu']
test_points_data = data_paths['test_points']

# Read and format Pichu.txt & Pikachu.txt data
def read_and_format_data(filename):
        try:
            with open(filename, 'r') as file:
                next(file) # Skip header 
                lines = [re.sub(r'[()\s]', '', line) for line in file]
                points = [tuple(map(float, line.split(','))) for line in lines]
            return points
        except Exception as e:
            print("An error occurred while reading the data from file:", e)

# Usage of func
pichu_points = read_and_format_data(pichu_data)
pikachu_points = read_and_format_data(pikachu_data)

# Plot points of x,y-axis on a graph to add visualization
def plot_points(pichu_points, pikachu_points):
    pichu_x, pichu_y = zip(*pichu_points)
    pikachu_x, pikachu_y = zip(*pikachu_points)
    plt.scatter(pichu_x, pichu_y, color='blue', label='Pichu')
    plt.scatter(pikachu_x, pikachu_y, color='red', label='Pikachu')
    plt.xlabel('Width')
    plt.ylabel('Height')
    plt.legend()
    plt.show()

# Read the test points for evaluation of the classifications algorithm's performance (used for testing the performance by using test_points.txt)
def read_and_format_test_points(filename):
    formatted_points = []
    with open(filename, 'r') as file:
        for line in file:
            pairs = re.findall(r'[-+]?\d*\.\d+|[-+]?\d+', line)
            formatted_points.extend([(float(pairs[i]), float(pairs[i+1])) for i in range(0, len(pairs), 2)])
    return formatted_points

# Usage of func
test_points = read_and_format_test_points(test_points_data)

# Classify the test points
def classify_test_point(test_point, pichu_points, pikachu_points):

    # Calculate distances to all Pichu and Pikachu points using 'Euclidean distance' formula
    pichu_distances = [np.sqrt((test_point[0] - p[0])**2 + (test_point[1] - p[1])**2) for p in pichu_points]
    pikachu_distances = [np.sqrt((test_point[0] - p[0])**2 + (test_point[1] - p[1])**2) for p in pikachu_points]
    
    # Find the minimum distance for pichu and pikachu
    min_pichu_distance = min(pichu_distances)
    min_pikachu_distance = min(pikachu_distances)
    
    # Check which of pichu and pikachu the nearest point belongs to
    if min_pichu_distance < min_pikachu_distance:
        return "Pichu"
    else:
        return "Pikachu"

classifications = []
for test_point in test_points:
    classification = classify_test_point(test_point, pichu_points, pikachu_points)
    classifications.append(classification)

# Output results
for i, test_point in enumerate(test_points):
    print(f"Sample with (width, height): {test_point} classified as {classifications[i]}")

# Plot after console results output
plot_points(pichu_points, pikachu_points)