import numpy as np

from wordembeddingtest import WordEmbeddingTest


class WEAT(WordEmbeddingTest):
    def __init__(self, X, Y, A, B):
        self.X = X
        self.Y = Y
        self.A = A
        self.B = B

    # Calculate effect size
    def effect_size(self):
        x_s = np.array([self.s(x) for x in self.X])
        y_s = np.array([self.s(y) for y in self.Y])

        return (np.mean(x_s) - np.mean(y_s)) / np.std(np.concatenate((x_s, y_s)))

    # Calculate s(w, A, B)
    def s(self, w):
        a_cos = np.array([self._cos(w, a) for a in self.A])
        b_cos = np.array([self._cos(w, b) for b in self.B])

        return (np.mean(a_cos) - np.mean(b_cos))

    def tostr(self):
        return "WEAT"
