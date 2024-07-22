import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import seaborn as sns

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True)
        self.create_widgets()

    def create_widgets(self):
        button_options = {"side": "top", "pady": 50, "padx": 50}

        self.bar_chart_button = tk.Button(self, text="Bar Chart", command=self.generate_bar_chart)
        self.bar_chart_button.pack(button_options)

        self.line_graph_button = tk.Button(self, text="Line Graph", command=self.generate_line_graph)
        self.line_graph_button.pack(button_options)

        self.scatter_plot_button = tk.Button(self, text="Scatter Plot", command=self.generate_scatter_plot)
        self.scatter_plot_button.pack(button_options)

        self.heat_map_button = tk.Button(self, text="Heat Map", command=self.generate_heat_map)
        self.heat_map_button.pack(button_options)

        self.three_d_graph_button = tk.Button(self, text="3D Graph", command=self.generate_three_d_graph)
        self.three_d_graph_button.pack(button_options)

        self.exit_button = tk.Button(self, text="Exit", command=self.exit_app)
        self.exit_button.pack(button_options)

    def generate_bar_chart(self):
        data = pd.DataFrame(np.random.randint(0, 100, size=(10, 1)), columns=list('A'))
        data.plot(kind='bar')
        plt.show()

    def generate_line_graph(self):
        data = pd.DataFrame(np.random.randint(0, 100, size=(10, 1)), columns=list('A'))
        data.plot(kind='line')
        plt.show()

    def generate_scatter_plot(self):
        data = pd.DataFrame(np.random.randint(0, 100, size=(10, 2)), columns=list('AB'))
        data.plot(kind='scatter', x='A', y='B')
        plt.show()

    def generate_heat_map(self):
        data = pd.DataFrame(np.random.randint(0, 100, size=(10, 10)))
        sns.heatmap(data, annot=True, cmap="YlGnBu")
        plt.show()

    def generate_three_d_graph(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x = np.random.randint(0, 100, size=(10))
        y = np.random.randint(0, 100, size=(10))
        z = np.random.randint(0, 100, size=(10))
        ax.scatter(x, y, z)
        plt.show()

    def exit_app(self):
        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            self.master.destroy()

root = tk.Tk()
root.title("Data Visualization")
root.state('zoomed')  
app = Application(master=root)
app.mainloop()