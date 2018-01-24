import numpy as np
import sklearn as skl
import librosa
from pydub import AudioSegment
from pydub.utils import make_chunks
import os
import sox
import subprocess
from sklearn.cluster import KMeans

myaudio = AudioSegment.from_file("brian.wav" , "wav")
chunk_length_ms = 30 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

#Export all of the individual chunks as wav files

for i, chunk in enumerate(chunks):
    chunk_name = "chunk{0}.wav".format(i)
    #print "exporting", chunk_name
    chunk.export(chunk_name, format="wav")

wav_files = os.listdir(".")
mfcc=np.zeros(20000).reshape(10000,2)
y=np.array([])
for i,file in enumerate(wav_files):
    #if file.endswith("chunks{0}.wav".format(i)):              --main .wav file
    y, sr=librosa.load(file)
    print(sr)
    mfcc[i+1]=librosa.feature.mfcc(y=y, sr=sr, n_mfcc=10)
print(mfcc.shape)
#kmeans = KMeans(n_clusters=5, random_state=0).fit_predict(mfcc)
#print(kmeans.labels_)


