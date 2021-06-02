from matplotlib import pyplot as plt

# example elbow joint angles
angles = [90, 86, 84, 80, 78, 75, 73, 70, 68, 66, 63, 61, 59, 57, 54, 53, 48, 40, 34, 33, 35, 37, 40, 44, 47, 50, 53, 55, 58, 60, 63, 65, 68, 70, 73, 75, 77, 80, 84, 88, 90]

seconds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,  27, 28,  29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]

plt.plot(seconds, angles)

plt.title("elbow angles over time")
plt.xlabel('seconds')
plt.ylabel('degrees')

plt.show()


# Plots a line segment between two points
def plot_line(p1, p2):
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'ro-')

# Plots a body_25 given an array of points
def plot_body(data):
    connections = [(8,9,11), (11,22,23), (11,24,24), (8,12,14), (14,19,20), (14,21,21), (0,1,4), (1,5,7), (1,8,8), (0,15,15), (15,17,17), (0,16,16), (16,18,18)]
    for i in range(len(connections)):
        subline = connections[i]
        plot_line((data[subline[0]][0], data[subline[0]][1]), (data[subline[1]][0], data[subline[1]][1]))
        for j in range(subline[1], subline[2]):
            plot_line((data[j][0], data[j][1]), (data[j+1][0], data[j+1][1]))
    plt.gca().invert_yaxis()

# Plots a hand given an array of points
def plot_hand(data):
    connections = [(0,17,20), (0,13,16), (0,9,12), (0,5,8), (0,1,4)]
    for i in range(len(connections)):
        subline = connections[i]
        plot_line((data[subline[0]][0], data[subline[0]][1]), (data[subline[1]][0], data[subline[1]][1]))
        for j in range(subline[1], subline[2]):
            plot_line((data[j][0], data[j][1]), (data[j+1][0], data[j+1][1]))
    plt.gca().invert_yaxis()
