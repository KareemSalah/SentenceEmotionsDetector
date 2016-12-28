from keras.models import Sequential, model_from_json
from keras.layers import Dense
from keras.utils.np_utils import to_categorical
import numpy


class Trainer:
    def __init__(self):
        pass

    def start(self):
        data_set = numpy.loadtxt("featureVectorization.csv", delimiter=",")
        data_size = len(data_set)

        # Change those according to your needs
        test_data_size = 1000
        num_features = 3

        # Train Set
        inp_vec = data_set[0:(data_size - test_data_size + 1), 0:num_features]
        output_vec = data_set[0:(data_size - test_data_size + 1), num_features]
        output_vec_categorical = to_categorical(output_vec)

        # Test Set
        test_inp_vec = data_set[test_data_size:, 0:num_features]
        test_output_vec = data_set[test_data_size:, num_features]
        test_output_vec_categorical = to_categorical(test_output_vec)

        # ====================== Model Configuration =========================
        # Stacking 3 layers, so choosing a sequential model
        model = Sequential()
        # The first layer has 3 inputs and has 3 outputs
        inp_layer = Dense(3, input_dim=3, init='uniform', activation='relu')
        # The second hidden layer has 3 outputs as well
        hid_layer = Dense(3, init='uniform', activation='relu')
        # The final output layer has 3 outputs between [0, 1], that's why a sigmoid activation function was used
        out_layer = Dense(3, init='uniform', activation='sigmoid')

        # Adding the layer to the model
        model.add(inp_layer)
        model.add(hid_layer)
        model.add(out_layer)

        # Compile model with loss function for multi-class classification, with the adam algorithm for optimizing
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        model_configs = model.to_json()

        # ===================== Training The Model ===========================
        model.fit(inp_vec, output_vec_categorical, nb_epoch=10, batch_size=10)
        model_weights = model.get_weights()

        # ===================== Saving model configs and weights =============
        fc = open('configs', 'w')
        fc.write(model_configs)
        model.save_weights('weights')

        # ===================== Evaluating Model =============================
        scores = model.evaluate(test_inp_vec, test_output_vec_categorical)
        print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
        return scores[1]*100.0
