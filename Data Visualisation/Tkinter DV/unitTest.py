import unittest
from unittest.mock import patch, MagicMock
from app import Application
import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

class TestApplication(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = Application(master=self.root)

    def test_1_create_widgets(self):
        print("Test 1: Create Widgets")
        self.assertIsNotNone(self.app.bar_chart_button)
        self.assertIsNotNone(self.app.line_graph_button)
        self.assertIsNotNone(self.app.scatter_plot_button)
        self.assertIsNotNone(self.app.heat_map_button)
        self.assertIsNotNone(self.app.three_d_graph_button)
        self.assertIsNotNone(self.app.exit_button)
        print("Passed")

    @patch('matplotlib.pyplot.show')
    def test_2_generate_bar_chart(self, mock_plt_show):
        print("Test 2: Generate Bar Chart")
        self.app.generate_bar_chart()
        mock_plt_show.assert_called_once()
        print("Passed")

    @patch('matplotlib.pyplot.show')
    def test_3_generate_line_graph(self, mock_plt_show):
        print("Test 3: Generate Line Graph")
        self.app.generate_line_graph()
        mock_plt_show.assert_called_once()
        print("Passed")

    @patch('matplotlib.pyplot.show')
    def test_4_generate_scatter_plot(self, mock_plt_show):
        print("Test 4: Generate Scatter Plot")
        self.app.generate_scatter_plot()
        mock_plt_show.assert_called_once()
        print("Passed")

    @patch('matplotlib.pyplot.show')
    def test_5_generate_heat_map(self, mock_plt_show):
        print("Test 5: Generate Heat Map")
        self.app.generate_heat_map()
        mock_plt_show.assert_called_once()
        print("Passed")

    @patch('matplotlib.pyplot.show')
    def test_6_generate_three_d_graph(self, mock_plt_show):
        print("Test 6: Generate 3D Graph")
        self.app.generate_three_d_graph()
        mock_plt_show.assert_called_once()
        print("Passed")

    @patch('tkinter.messagebox.askyesno')
    @patch('tkinter.Tk.destroy')
    def test_7_exit_app_yes(self, mock_destroy, mock_askyesno):
        print("Test 7: Exit App")
        mock_askyesno.return_value = True
        self.app.exit_app()
        mock_destroy.assert_called_once()
        print("Passed")

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(unittest.makeSuite(TestApplication))
    if result.wasSuccessful():
        print(f"{result.testsRun}/{result.testsRun} Tests Passed.")
    else:
        print(f"{result.testsRun - len(result.failures)}/{result.testsRun} Tests Passed.")