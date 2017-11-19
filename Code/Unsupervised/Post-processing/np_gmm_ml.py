import matplotlib.pyplot as plt
import random
from sklearn.cluster import KMeans
import numpy as np
import itertools
import operator

def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]
# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()
number_of_speakers = 5
text_file = open("random.txt", "r")
# text_file = open("gmm_diffvalue.txt", "r")
# lines = text_file.readlines()
lines1 = text_file.read().split('\n')
for s in range(0,len(lines1)):
    try:
        lines1[s] = int(lines1[s].strip())
    except:
        lines1[s] = lines1[s-1]
        pass
print (lines1)
print (len(lines1))
text_file.close()
lines1 = np.array(lines1)
list1 = []
# list0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# print(list0)
print(len(list1))
grouping = int(len(lines1)/40)
for s in range(0,int(len(lines1)/grouping)):
    list1.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for m in range(s*grouping, (s+1)*grouping):
        try:
            print(int(s),int(lines1[int(m)]))
            list1[int(s)][int(lines1[int(m)])]  = list1[int(s)][int(lines1[int(m)])] + 1;
        except ValueError:
            pass
print(list1)

kmeans = KMeans(n_clusters=5, random_state=100).fit(list1)
print(kmeans.labels_)
listAns = [0 for i in range(0,len(kmeans.labels_))]
for i in range(2,len(listAns)-2):
    listAns[i] = most_common([kmeans.labels_[i-2],kmeans.labels_[i-1],kmeans.labels_[i],kmeans.labels_[i+1],kmeans.labels_[i+2]])
listAns[0] = most_common([kmeans.labels_[2],kmeans.labels_[1],kmeans.labels_[0]])
listAns[1] = most_common([kmeans.labels_[2],kmeans.labels_[1],kmeans.labels_[0]])
listAns[len(listAns)-1] = most_common([kmeans.labels_[len(listAns)-1-2],kmeans.labels_[len(listAns)-1-1],kmeans.labels_[len(listAns)-1]])
listAns[len(listAns)-2] = most_common([kmeans.labels_[len(listAns)-1-2],kmeans.labels_[len(listAns)-1-1],kmeans.labels_[len(listAns)-1]])
print(listAns)
for i in range(0,11):
    x = int(len(lines1) / grouping) / 10
    plt.plot((x * i - 0.25, x * i -0.25), (0, 5), 'k--')
plt.plot(listAns, color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
file1 = open('3_1.txt','w')
for item in listAns:
  file1.write("%s\n" % item)
file1.close()
plt.show()