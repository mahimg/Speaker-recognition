from keras.layers import Input, Dense
from keras.models import Model, load_model
import scipy.io as spio
import numpy as np
from sklearn import cluster, mixture
np.set_printoptions(threshold='nan')
# this is the size of our encoded representations
encoding_dim = 200




mat = spio.loadmat('matlab2.mat', squeeze_me=True)

matrix = mat['nfp']

input = Input(shape=(63,))
# "encoded" is the encoded representation of the input
encoded = Dense(encoding_dim, activation='relu')(input)
# "decoded" is the lossy reconstruction of the input
decoded = Dense(63, activation='sigmoid')(encoded)


autoencoder1 = load_model('autoenc-200.h5')
#matrix = matrix.transpose()
encoder = Model(input, encoded)

# create a placeholder for an encoded (32-dimensional) input
encoded_input = Input(shape=(encoding_dim,))
# retrieve the last layer of the autoencoder model
decoder_layer = autoencoder1.layers[-1]
# create the decoder model
decoder = Model(encoded_input, decoder_layer(encoded_input))




encoded_value = encoder.predict(matrix)
decoded_value = decoder.predict(encoded_value)

a1 = decoded_value[1:1000]
a2 = decoded_value[1001:2000]
a3 = decoded_value[2001:3000]
a4 = decoded_value[3001:4000]
a5 = decoded_value[4001:5000]

b1 = decoded_value[20001:21000]
b2 = decoded_value[21001:22000]
b3 = decoded_value[22001:23000]
b4 = decoded_value[23001:24000]
b5 = decoded_value[24001:25000]

c1 = decoded_value[32001:33000]
c2 = decoded_value[33001:34000]
c3 = decoded_value[34001:35000]
c4 = decoded_value[35001:36000]
c5 = decoded_value[36001:37000]

d1 = decoded_value[50001:51000]
d2 = decoded_value[51001:52000]
d3 = decoded_value[52001:53000]
d4 = decoded_value[53001:54000]
d5 = decoded_value[54001:55000]

e1 = decoded_value[70001:71000]
e2 = decoded_value[71001:72000]
e3 = decoded_value[72001:73000]
e4 = decoded_value[73001:74000]
e5 = decoded_value[74001:75000]
#kmeans = cluster.KMeans(n_clusters=5, random_state=0, max_iter=2000).fit_predict(decoded_value)
#print("Kmeans Clustering:")
#print(kmeans)


###----GMM

GMM = mixture.GaussianMixture(n_components=5, random_state=None,reg_covar=0.18, max_iter=8000)

GMM.fit(a1)
GMM.bic(a1)
gmm = GMM.predict(a1)

