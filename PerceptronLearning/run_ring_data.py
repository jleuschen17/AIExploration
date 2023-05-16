'''
Name(s): Joe Leuschen
UW netid(s): jleusche
'''

from binary_perceptron import BinaryPerceptron # Your implementation of binary perceptron
from plot_bp import PlotBinaryPerceptron
import csv  # For loading data.
from matplotlib import pyplot as plt
from remapper import remap

class PlotRingBP(PlotBinaryPerceptron):

    def __init__(self, bp, plot_all=True, n_epochs=20, IS_REMAPPED=True):
        self.IS_REMAPPED = IS_REMAPPED
        super().__init__(bp, plot_all, n_epochs)

    def read_data(self):
        data_as_strings = list(csv.reader(open('ring-data.csv'), delimiter=','))
        self.TRAINING_DATA = [[float(f1), float(f2), int(c)] for [f1, f2, c] in data_as_strings]
        if self.IS_REMAPPED:
            for i in range(len(self.TRAINING_DATA)):
                x, y = remap(self.TRAINING_DATA[i][0], self.TRAINING_DATA[i][1])
                self.TRAINING_DATA[i][0] = x
                self.TRAINING_DATA[i][1] = y

    def plot(self):

        plt.title("Ring Data: Angle vs Radius")
        plt.xlabel("Angle")
        plt.ylabel("Radius")
        plt.legend(loc='best')
        plt.show()


if __name__ == '__main__':
    binary_perceptron = BinaryPerceptron(alpha=0.5)
    pbp = PlotRingBP(binary_perceptron)
    pbp.train()
    pbp.plot()

