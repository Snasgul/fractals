import matplotlib.pyplot as plt
import time

lines = [[0, 0], [0, 1]]
    
def rotate_by_90(x, y, origin_x, origin_y):
    return [origin_x - (y - origin_y), origin_y + x - origin_x]

def iterate():
    temp = [[]]
    lines.reverse()
    origin_x = lines[0][0]
    origin_y = lines[0][1]
    for point in lines:
        if point != lines[0]:
            temp.append(rotate_by_90(point[0], point[1], origin_x, origin_y))
    del temp[0]
    lines.reverse()
    lines.extend(temp)

for i in range(15):
    iterate()
    x_points = []
    y_points = []
    for i in range(len(lines)):
        x_points.append(lines[i][0])
        y_points.append(lines[i][1])

    size = max((max(x_points) - min(x_points)), (max(y_points) - min(y_points)))
    print(size)
    #plt.axes((min(x_points), min(y_points), size, size))
    
    plt.plot(x_points, y_points, '-')
    plt.show(block=True)
    time.sleep(1)