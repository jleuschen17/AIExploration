'''
Name(s): Joe Leuschen
UW netid(s): jleusche
'''
"""ternary_perceptron.py
Complete this python file as part of Part B.
You'll be filling in with code to implement:

a 3-way classifier
a 3-way weight updater

This program can be run from the given Python program
called run_3_class_4_feature_iris_data.py.
"""


def student_name():
    return "Joseph Leuschen"  # Replace with your own name.


class TernaryPerceptron:
    """
    Class representing the Ternary Perceptron
    ---
    It is an algorithm that can learn a ternary classifier
    """
    
    def __init__(self, W=None, alpha=1):
        """
        Initialize the Ternary Perceptron
        ---
        weights: Weight vector of the form W = [W0, W1, W2] where each Wi is a vector of
        the form [w_0, w_1, ..., w_{n-1}, bias_weight]
        alpha: Learning rate
        """
        if W is None:
            self.W = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        else:
            self.W = [w[:] for w in W]  # Use a deep copy of the argument weight
        self.alpha = alpha
    
    @staticmethod
    def argmax(lst):
        """
        Helper function for finding the arg max of elements in a list.
        It returns the index of the first occurrence of the maximum value.
        """
        idx, mval = -1, -1E20
        for i in range(len(lst)):
            if lst[i] > mval:
                mval = lst[i]
                idx = i
        return idx
    
    def classify(self, x_vector):
        """
        Method that classifies a given data point into one of 2 classes
        ---
        Inputs:
        x_vector = [x_0, x_1, ..., x_{n-1}]
        Note: y (correct class) is not part of the x_vector.
        
        Returns:
        y_hat: Predicted class
            0, 1, or 2,
            depending on which weight vector gives the highest
            dot product with the x_vector augmented with the 1
            for bias in position n.
            Break any ties by returning the first max element.
        """
        # ADD YOUR CODE HERE
        x_vector.append(1)
        dot_products = []
        for i in range(3):
            val = 0
            for j in range(len(x_vector)):
                val += self.W[i][j] * x_vector[j]
            dot_products.append(val)
        return self.argmax(dot_products)
    
    def train_with_one_example(self, x_vector, y):
        """
        Method that updates the model weights using a particular training example (x_vector,y)
        and returns whether the model weights were actually changed or not
        ---
        Inputs:
        x_vector: Feature vector, same as method classify
        y: Actual class of x_vector
            0, 1, or 2, depending on which class
            it belongs to
        Returns:
        weight_changed: True if there was a change in the weights
                        else False
        """
        # ADD YOUR CODE HERE
        classification = self.classify(x_vector)
        x_vector.pop()
        if classification == y:
            return False
        else:
            print("\n\n\n", self.W)
            if classification == 0:
                for i in range(len(x_vector)):
                    self.W[0][i] -= (self.alpha * x_vector[i])
                    self.W[y][i] += (self.alpha * x_vector[i])
                self.W[0][-1] -= self.alpha
                self.W[y][-1] += self.alpha
            elif classification == 1:
                for i in range(len(x_vector)):
                    self.W[1][i] -= (self.alpha * x_vector[i])
                    self.W[y][i] += (self.alpha * x_vector[i])
                self.W[1][-1] -= self.alpha
                self.W[y][-1] += self.alpha
            else:
                for i in range(len(x_vector)):
                    self.W[2][i] -= (self.alpha * x_vector[i])
                    self.W[y][i] += (self.alpha * x_vector[i])
                self.W[2][-1] -= self.alpha
                self.W[y][-1] += self.alpha
            return True
    
    def train_for_an_epoch(self, training_data):
        """
        Method that goes through the given training examples once, in the order supplied,
        passing each one to train_with_one_example.
        ---
        Input:
        training_data: Input training data
        [[x_vector_1, y_1], [x_vector_2, y_2], ...]
        where the x_vector is concatenated with the y value.

        Returns:
        changed_count: Return the number of weight updates.
        (If zero, then training has converged.)
        """
        # ADD YOUR CODE HERE
        changes = 0
        for i in training_data:
            changed = self.train_with_one_example(i[:len(i)-1], i[-1])
            if changed:
                changes += 1
        return changes


def sample_test():
    """
    May be useful while developing code
    Trains the ternary perceptron using a synthetic training set
    Prints the weights obtained after training
    """
    DATA = [
        [20, 25, 1, 1, 0],
        [-2, 7, 2, 1, 1],
        [1, 10, 1, 2, 1],
        [3, 2, 1, 1, 2],
        [5, -2, 1, 1, 2]]
    tp = TernaryPerceptron()
    print("Training Ternary Perceptron for 10 epochs.")
    for i in range(10):
        tp.train_for_an_epoch(DATA)
    print("Ternary Perceptron weights:")
    print(tp.W)
    print("Done.")


if __name__ == '__main__':
    sample_test()
