import numpy as np
import utils

class Adaline:
    def __init__(self, patternsLen, A, eta):
        self.W = utils.getNRandomNumbers(patternsLen + 1, 1)
        self.A = A
        self.eta = eta

    def activationFunction(self, X):
        return np.dot(X,self.W) * self.A

    def learning(self, X, d):
        salida_y = self.activationFunction(X)
        e = d - salida_y
        self.W = self.W + np.dot(self.eta * e * self.A, X)
        return self.activationFunction(X)