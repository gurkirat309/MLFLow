import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def plot_graph(data, title="Graph Title", xlabel="X-axis", ylabel="Y-axis"):
    """
    Plots a simple line graph using the provided data.

    Parameters:
    - data: A list or numpy array of y-values. The x-values will be generated automatically.
    - title: Title of the graph.
    - xlabel: Label for the x-axis.
    - ylabel: Label for the y-axis.
    """
    x_values = np.arange(len(data))
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=x_values, y=data)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()  
