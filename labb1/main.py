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

import numpy as np
import matplotlib.pyplot as plt
#import pdb; pdb.set_trace() # Debugging with venv

# Path to data
pichuPath = "data/pichu.txt"
pikachuPath = "data/pikachu.txt"
test_pointsPath = "data/test_points.txt"

# Read the Pichu.txt & Pikachu.txt data
def read_data(filename):
    with open(filename, 'r') as file:
        next(file)  # Skip the first line (header)
        points = [tuple(map(float, line.strip('()\n').split(','))) for line in file]
    return points

pichu_points = read_data(pichuPath)
pikachu_points = read_data(pikachuPath)

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

plot_points(pichu_points, pikachu_points)

# Read the test points for evaluation of the classifications algorithm's performance (used for testing the performance by using test_points.txt)
def read_test_points(filename):
    with open(filename, 'r') as file:
        test_points = [tuple(map(float, line.strip().split(','))) for line in file]
    return test_points

test_points = read_test_points(test_pointsPath)

# Classify the test points
def classify_test_point(test_point, pichu_points, pikachu_points):

    # Calculate distances to all Pichu and Pikachu points using 'Euclidean distance' formula
    pichu_distances = [np.sqrt((test_point[0] - p[0])**2 + (test_point[1] - p[1])**2) for p in pichu_points]
    pikachu_distances = [np.sqrt((test_point[0] - p[0])**2 + (test_point[1] - p[1])**2) for p in pikachu_points]
    
    # Find the minimum distance for each species
    min_pichu_distance = min(pichu_distances)
    min_pikachu_distance = min(pikachu_distances)
    
    # Check which species the nearest point belongs to
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