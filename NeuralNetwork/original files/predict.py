from keras.models import Sequential, model_from_json
from keras.layers import Dense
from keras.utils.np_utils import to_categorical
import numpy



data_set = numpy.loadtxt("featureVectorization.csv", delimiter=",")
data_size =len(data_set)

# Change those according to your needs
test_data_size = 1000
num_features = 3


#Train Set
inp_vec = data_set[0:(data_size - test_data_size + 1), 0:(num_features)]
output_vec = data_set[0:(data_size - test_data_size + 1), num_features]
output_vec_categorical = to_categorical(output_vec)



#Test Set
test_inp_vec = data_set[test_data_size:, 0:(num_features)]
test_output_vec = data_set[test_data_size:, num_features]
test_output_vec_categorical = to_categorical(test_output_vec)




ff = open('configs', 'r')
conf = ff.readline()
model2 = model_from_json(conf)

model2.load_weights('weights')

model2.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

scores = model2.evaluate(test_inp_vec, test_output_vec_categorical)
print("%s: %.2f%%" % (model2.metrics_names[1], scores[1]*100))
