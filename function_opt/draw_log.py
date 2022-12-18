import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def read_log(log):
    avg_list = list()
    std_list = list()
    min_list = list()
    max_list = list()
    gen_list = list()
    for g in log:
        avg_list.append(g['avg'])
        std_list.append(g['std'])
        min_list.append(g['min'])
        max_list.append(g['max'])
        gen_list.append(g['gen'])
    return np.array(gen_list), np.array(avg_list), np.array(std_list), np.array(max_list), np.array(min_list)

def draw_log(log):
    gen_list, avg_list, std_list, max_list, min_list = read_log(log)
    plt.figure(figsize=(20, 10))
    plt.plot(gen_list, avg_list, label="avg")
    plt.plot(gen_list, min_list, label="min")
    plt.plot(gen_list, max_list, label="max")
    plt.legend()
    plt.tight_layout()
    plt.show()

def draw_queens_on_desk(desk):
    
    fig = plt.figure(figsize=(20,20))
    ax = fig.add_subplot(111)


    queen_number = len(desk)

    start_col_color = "black"
    cell_color = start_col_color

    def change_color(base_color):
            if base_color == "black":
                return "white"
            else:
                return "black"

    for col in range(queen_number):
        start_col_color = change_color(start_col_color)
        cell_color = start_col_color

        for row in range(queen_number):
            patch_obst = patches.Rectangle((col - 0.5, row - 0.5), 1, 1, edgecolor = cell_color, facecolor = cell_color, fill=True)
            ax.add_patch(patch_obst)
            cell_color = change_color(cell_color)
            




    for queen in desk:
        # Add queen point to desc
        patch_queen = patches.Circle(xy=(queen // queen_number, queen % queen_number), radius=0.15, facecolor="red", edgecolor="red", fill=True, visible=True)
        ax.add_patch(patch_queen)


    plt.grid()

    ax.set_yticks(np.arange(-0.5, queen_number+0.5, 1))
    ax.set_xticks(np.arange(-0.5, queen_number+0.5, 1))
    ax.set_yticklabels(np.arange(0, queen_number+0.5, 1))
    ax.set_xticklabels(np.arange(0, queen_number+0.5, 1))

    plt.draw()
    plt.show()

