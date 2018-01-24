import scipy.io as spio
from sklearn import cluster, datasets, mixture
import numpy as np

np.set_printoptions(threshold='nan')

mat = spio.loadmat('enc_vector.mat', squeeze_me=True)
print(type(mat))
clusters = 5

array = mat['new_vector']
array = array.transpose()
print(type(array))
print(np.shape(mat))
print(array[1])

'''GMM = mixture.GaussianMixture(n_components=clusters, random_state=None,reg_covar=0.18, max_iter=8000)
GMM.fit(array)
gmm = GMM.predict(array)

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
'''