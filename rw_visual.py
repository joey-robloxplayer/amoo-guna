import matplotlib.pyplot as plt
from random_walk import RandomWalk




while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 9), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.cool, edgecolors= 'none', s=15)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='cyan', edgecolors='none', s= 100)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Make another walk? (yes/no)")
    if keep_running == 'no':
        break

