'''
Name(s): Joe Leuschen
UW netid(s): jleusche
'''

# Your implementation of binary perceptron
from plot_tp import PlotTernaryPerceptron
import csv  # For loading data.
from matplotlib import pyplot as plt
from remapper import remap
from ternary_perceptron import TernaryPerceptron


class PlotMultiTP(PlotTernaryPerceptron):

    def __init__(self, bp, n_epochs=20):
        super().__init__(bp, n_epochs)

    def read_data(self):
        data_as_strings = list(csv.reader(open('synthetic_data.csv'), delimiter=','))
        self.TRAINING_DATA = [[float(f1), float(f2), int(c)]
                              for [f1, f2, c] in data_as_strings]

    def plot(self):
        plt.title("Synthetic data plot")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend(loc='best')
        plt.show()

if __name__ == '__main__':
    ternary_perceptron = TernaryPerceptron
    pbp = PlotMultiTP(ternary_perceptron)
    pbp.train()
    pbp.plot()