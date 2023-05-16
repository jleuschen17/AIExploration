'''
Name(s): Joe Leuschen
UW netid(s): jleusche
'''


from binary_perceptron import BinaryPerceptron # Your implementation of binary perceptron
from plot_bp import PlotBinaryPerceptron
import csv  # For loading data.
from matplotlib import pyplot as plt
from remapper import remap

class PlotMultiBPOneVsOne(PlotBinaryPerceptron):

    def __init__(self, bp, plot_all=True, n_epochs=20, CLASSES=(0, 1)):
        self.CLASSES = CLASSES
        super().__init__(bp, plot_all, n_epochs)

    def read_data(self):
        data_as_strings = list(csv.reader(open('synthetic_data.csv'), delimiter=','))
        self.TRAINING_DATA = [[float(f1), float(f2), int(c)]
                              for [f1, f2, c] in data_as_strings]
        i = 0
        while i < len(self.TRAINING_DATA):
            if self.TRAINING_DATA[i][-1] == self.CLASSES[0]:
                self.TRAINING_DATA[i][-1] = 1
                i+=1
            elif self.TRAINING_DATA[i][-1] == self.CLASSES[1]:
                self.TRAINING_DATA[i][-1] = -1
                i+=1
            else:
                self.TRAINING_DATA.pop(i)


if __name__ == '__main__':
    binary_perceptron = BinaryPerceptron(alpha=0.5, weights=[0, 0, 0])
    pbp = PlotMultiBPOneVsOne(binary_perceptron)
    pbp.train()
    pbp.plot()
