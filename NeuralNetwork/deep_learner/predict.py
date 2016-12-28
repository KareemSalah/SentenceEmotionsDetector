from keras.models import model_from_json


class Classifier:
    def __init__(self):

    def load_model(self):
        f = open('configs', 'r')
        conf = f.readline()
        f.close()
        model = model_from_json(conf)
        model.load_weights('weights')
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def start(self, vectors):
        self.load_model

        predictions = []
        counters = [0, 0, 0]
        for result in model.predict(vectors):
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
