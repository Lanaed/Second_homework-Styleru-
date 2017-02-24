import matplotlib.pyplot as plt
import json
import random

def plt_histogram(sorted_base, x, y):
    color_list = json.load(open('color.json'))
    for i in range(len(y)):
        plt.bar(x[i], y[i], label=sorted_base[i][0], color=random.choice(color_list))
    plt.title('Average payments')
    plt.ylabel('Payment')
    plt.xlabel('Languages')
    plt.legend(ncol=4)
    plt.axis([1, len(y) + 1, 0, 130000])
    plt.show()

