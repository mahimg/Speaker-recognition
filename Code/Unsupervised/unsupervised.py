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

mat = spio.loadmat('fvect.mat', squeeze_me=True)

matrix = mat['fvect']
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






###----GMM





GMM = mixture.GaussianMixture(n_components=20, random_state=None,reg_covar=0.1, max_iter=800000)
GMM = mixture.GaussianMixture(n_components=20, random_state=0,reg_covar=0.1, max_iter=500,tol=0.00000001,verbose=1,verbose_interval=5)



GMM.fit(cat)

gmm = GMM.predict(cat)
GMM.bic(decoded_value4)
count1 = np.bincount(gmm[0:15396])
print((np.argmax(count1)))
count2 = np.bincount(gmm[15397:30793])
print((np.argmax(count2)))
count3 = np.bincount(gmm[30794:46190])
print((np.argmax(count3)))
count4 = np.bincount(gmm[46191:61587])
print((np.argmax(count4)))
count5 = np.bincount(gmm[61588:76984])
print((np.argmax(count5)))

	print(np.shape(gmm))
print("Gaussian Mixture:")
print(gmm)


#----------
a1=decoded_value4[1:2550]
a2=decoded_value4[12750:(12750+7650)]
a3=decoded_value4[25499:(25499+5100)]
a4=decoded_value4[38248:(38248+12750)]
a5=decoded_value4[50997:(50997+10200)]

a1=decoded_value4[1:6374]
a2=decoded_value4[12750:(12750+6374)]
a3=decoded_value4[25499:(25499+6374)]
a4=decoded_value4[38248:(38248+6374)]
a5=decoded_value4[50997:(50997+6374)]







a6=decoded_value4[6373:12749]
a7=decoded_value4[(12750+6373):25498]
a8=decoded_value4[(25499+6373):38247]
a9=decoded_value4[(38248+6373):50996]
a10=decoded_value4[(50997+6373):63745]

cat=np.concatenate((a1,a2,a3,a4,a5), axis=0)


import matplotlib.pyplot as plt 

plt.scatter(list(range(1,38250)),gmm)
plt.show()


np.savetxt('4.txt',gmm,fmt='%7.0f')





#### shuffle test

a1=decoded_value4[0:2000]
a2=decoded_value4[12749:12749+4000]
a3=decoded_value4[12749*2:12749*2+6000]
a4=decoded_value4[12749*3:12749*3+8000]
a5=decoded_value4[12749*4:12749*4+10000]


b1=decoded_value4[6375:6375+6374]
b2=decoded_value4[12749+6374:12749+6374+6374]
b3=decoded_value4[12749*2+6374:12749*2+6374+6374]
b4=decoded_value4[12749*3+6374:12749*3+6374+6374]
b5=decoded_value4[12749*4+6374:12749*4+6374+6374]


cat=np.concatenate((a1,a2,a3,a4,a5), axis=0)