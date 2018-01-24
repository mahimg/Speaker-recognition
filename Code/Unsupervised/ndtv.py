from keras.layers import Input, Dense
from keras.models import Model
import scipy.io as spio
import numpy as np
from sklearn import cluster, mixture

# this is the size of our encoded representations
encoding_dim = 50

# this is our input placeholder
input = Input(shape=(10,))
# "encoded" is the encoded representation of the input
encoded = Dense(50, activation='relu')(input)
decoded = Dense(10, activation='relu')(encoded)

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

mat = spio.loadmat('C:\\Users\\Souradip Pal\\Downloads\\ndtv1_vect.mat', squeeze_me=True)

matrix = mat['ndtv1_vect']
#matrix = matrix.transpose()



autoencoder.fit(matrix,matrix,epochs=200,batch_size=256,shuffle=True)

encoded_value = encoder.predict(matrix)
decoded_value = decoder.predict(encoded_value)


#means = cluster.KMeans(n_clusters=5, random_state=0, max_iter=2000).fit_predict(decoded_value2)
#print("Kmeans Clustering:")
#print(kmeans)

##--stack
autoencoder.fit(decoded_value, decoded_value,
                epochs=200,
                batch_size=256,
                shuffle=True)

encoded_value2 = encoder.predict(decoded_value)
decoded_value2 = decoder.predict(encoded_value2)


autoencoder.fit(decoded_value2, decoded_value2,
                epochs=200,
                batch_size=256,
                shuffle=True)

encoded_value3 = encoder.predict(decoded_value2)
decoded_value3 = decoder.predict(encoded_value3)

autoencoder.fit(decoded_value3, decoded_value3,
                epochs=200,
                batch_size=256,
                shuffle=True)

encoded_value4 = encoder.predict(decoded_value3)
decoded_value4 = decoder.predict(encoded_value4)

GMM = mixture.GaussianMixture(n_components=20, random_state=0,reg_covar=0.1, max_iter=500,tol=0.00000001,verbose=1,verbose_interval=5)



GMM.fit(decoded_value4)

gmm = GMM.predict(decoded_value4)

import matplotlib.pyplot as plt 

plt.scatter(list(range(1,36492)),gmm)
plt.show()