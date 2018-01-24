from keras.layers import Input, Dense
from keras.models import Model
import scipy.io as spio
import numpy as np
# this is the size of our encoded representations
encoding_dim = 200

# this is our input placeholder
input = Input(shape=(63,))
# "encoded" is the encoded representation of the input
encoded = Dense(encoding_dim, activation='relu')(input)
# "decoded" is the lossy reconstruction of the input
decoded = Dense(63, activation='sigmoid')(encoded)

# this model maps an input to its reconstruction
autoencoder = Model(input, decoded)

encoder = Model(input, encoded)

# create a placeholder for an encoded (32-dimensional) input
encoded_input = Input(shape=(encoding_dim,))
# retrieve the last layer of the autoencoder model
decoder_layer = autoencoder.layers[-1]
# create the decoder model
decoder = Model(encoded_input, decoder_layer(encoded_input))
autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')

import scipy.io as spio

import numpy as np

np.set_printoptions(threshold='nan')

mat = spio.loadmat('feature_vector.mat', squeeze_me=True)

matrix = mat['new_vector']
matrix = matrix.transpose()



autoencoder.fit(matrix, matrix,
                epochs=50,
                batch_size=256,
                shuffle=True)

encoded_value = encoder.predict(matrix)
decoded_value = decoder.predict(encoded_value)

