from keras.models import *
import numpy as np


class Classifier:
    def __init__(self):
        self.model = None

    def load_model(self):
        f = open('configs', 'r')
        conf = f.readline()
        f.close()
        self.model = model_from_json(conf)
        self.model.load_weights('weights')
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return self.model

    def start(self, vectors):
        print self.model
        print 'ttttttttssssssstttttttttttttt'
        # if not self.model:
        self.load_model()
        print '99999999999999999999999999999999999'
        print(np.array(vectors))
        print '99999999999999999999999999999999999'
        predictions = []
        counters = [0, 0, 0]
        for result in self.model.predict(np.array(vectors)):
            if result[0] > result[1] and result[0] > result[2]:
                predictions.append(0)
                counters[0] += 1
            elif result[1] > result[0] and result[1] > result[2]:
                predictions.append(1)
                counters[1] += 1
            else:
                predictions.append(2)
                counters[2] += 1
        total = len(predictions)

        results = dict()
        results['predictions'] = predictions
        results['counters'] = counters
        results['total'] = total
        return results
