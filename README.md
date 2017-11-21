# Speaker-recognition
## Abstract
Speaker Sequence Segmentation is the first step in many audio-processing applications and aims to solve the problem ”who spoke when”. It therefore relies on efficient use of temporal information from extracted audio features. In this project, we have utilised the Linear Predictive Coefficients of the speech signal and it’s derived features to segment out the speech of individual speakers. We have employed both supervised and unsupervised learning methods to approach the problem.

## Introduction
### Introduction to Problem
The objective of this project is to segment speech sequences based on speaker transitions, where the number of speakers is not known beforehand.

### Motivation
The number of smart devices are increasing exponentially and so is the amount of data to process. Audio indexing which aims to organize content of multimedia using semantic information from audio data is broader class of problem for audio processing. Speech sequence segmentation aims to label the segments of audio/video data with corresponding speaker identities. Apart from audio indexing it has central application in speech research such as automatic speech recognition, rich transcription etc.

### Literature Review
The general unsupervised segmentation problem deals with the classification of a given utterance to a speaker participating in a multispeaker conversation. The exact definition of the problem is as follows. given a speech signal, recorded from a multi-speaker conversation, determine the number of speakers, determine the transition times between speakers and assign each speech segment to its speaker.

* Miro, Xavier Anguera, et al. ”Speaker diarization: A review of recent research.” Audio, Speech, and Language Processing, IEEE Transactions on 20.2 (2012): 356-370 discusses two approach, top-down and bottom-up approach. The top-down approach is initialized with very few clusters (usually one) whereas the bottom-up approach is initialized with many clusters (usually more clusters than expected speakers). In both cases the aim is to iteratively converge towards an optimum number of clusters. If the final number is higher than the optimum then the system is said to under-cluster.

* Qin Jin, Kornel Laskowski, Tanja Schultz, and Alex Waibel, ”Speaker Segmentation and Clustering In meetings” uses BIC ( Bayesian Information Criterion) to calculate the performance of different model. A negative value of BIC means that model provides a better fit to the data, that is there is a speaker change at point . Therefore, we continue merging segments until the value of BIC for the two closest segments is negative.

* Aadel Alatwi, Stephen So, Kuldip K. Paliwal “Perceptually Motivated Linear Prediction Cepstral Features for Network Speech Recognition” proposed a new method for modifying the power spectrum of input speech to obtain a set of perceptually motivated Linear Prediction (LP) parameters that provide noise-robustness to Automatic Speech Recognition (ASR) features

* Vladimir Fabregas et al, “Transformations of LPC and LSF Parameters to Speech Recognition Features” discusses features that can be obtained from the LPC parameters are the LPCC (LPC Cepstrum) and the MLPCC (Mel-Frequency LPCC).

### Proposed Approach
The problem requires that we split the input audio into multiple segments according to the speaker transitions. For this purpose, we need to characterise each individual’s voice by some features, using which we can detect if there is a speaker transition. For this purpose, we are using LPC and it’s derived features. The pre-processing of the audio clip involves detecting and discarding the parts of audio clip that don’t contain any voice, i.e. all speakers are silent. Further, we engage in feature extraction. The extracted features are used for the purpose of classification using two methods - supervised and unsupervised. The post-processing involves eliminating the sporadic values/samples detected over each of the larger time frame.

## Conclusion
### Summary
The overall aim of this project was to segment speech sequences based on speaker transitions, where the number of speakers is not known beforehand. We have achieved doing this firstly using the supervised approach wherein we had the data of the speakers involved in the conversation beforehand. Secondly, the unsupervised approach implemented rarely failed to detect the speaker transitions.

### Feature Extension
Further improvement can be done to improve robustness to noise and non-speech audio such as music. Furthermore, advance speaker diarization should be able to handle presence of overlapped speech on which the occurrence of overlapping speech almost regularly presents in natural conversation.

### Applications
One of the most important application will be in transcription of conversation. It can be used to localise the instances of speaker instances to pool data for model training which in turn improve transcription accuracy.
It can be used to crop the speech of a specific person of interest from a long audio clip.
