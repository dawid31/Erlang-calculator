import numpy as np
import matplotlib.pyplot as plt
from erlang import calculate_erlang_b


def plot_graph(start, end):
    values = []
    arguments = np.linspace(start, end, num=200) #creates 200 samples in given range
    for x in arguments:
        block_rate = calculate_erlang_b(traffic=x, lines=3)
        values.append(block_rate)

    plt.plot(arguments, values)
    
    #Plot legend
    plt.title("Współczynnik blokady w zależności od intensywności zgłoszeń")
    plt.ylabel("Współczynnik blokady")
    plt.xlabel("Intensywność zgłoszeń (w erlangach)")
    plt.show()
