import numpy as np
import matplotlib.pyplot as plt
import math
import time

print(math.log(2756856/688856, 2))

def mandelbrot(x_start, x_stop, y_start, y_stop, resolution):
    try:
        #t = time.localtime()
        min_dist = min(x_stop - x_start, y_stop - y_start)
        x_cor = np.linspace(x_start, x_stop, int((x_stop - x_start) * resolution / min_dist))
        y_cor = np.linspace(y_start, y_stop, int((y_stop - y_start) * resolution / min_dist))
        x_len = len(x_cor)
        y_len = len(y_cor)
        iterations = 90 / min_dist
        iterations = 150
        output = np.zeros((x_len,y_len))

        size = 0

        for i in np.arange(x_len):

            for j in np.arange(y_len):
                c = complex(x_cor[i],y_cor[j])
                z = complex(0, 0)
                count = 0

                for k in np.arange(iterations):
                    z = (z * z) + c
                    count = count + 1
                    if (abs(z) > 4):
                        break
                    if(count == 90):
                        size += 1
                output[i,j] = count
            print((i/x_len)*100,"% completed")
        #print(time.localtime - t)
        
    finally:
        print(output)
        #plt.figure(dpi=3000)
        plt.imshow(output.T, cmap = "Blues")
        plt.axis("off")
        plt.show()
        plt.savefig("mandelbrot6.png")
        return size

#mandelbrot(-2, 1, -1.5, 1.5, 4000)
#2756856
mandelbrot(-2, 1, -1.5, 1.5, 2000)
#688856
#mandelbrot(-2, 1, -1.5, 1.5, 1000)
#171964
#mandelbrot(-2, 1, -1.5, 1.5, 500)
#42918
#mandelbrot(-1.5, 0.5, -1, 1, 1000)
#mandelbrot(-1.5, -0.5, 0, 1, 1000)