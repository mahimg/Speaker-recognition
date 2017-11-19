import matplotlib.pyplot as plt
import random
# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()
number_of_speakers = 5
text_file = open("random.txt", "r")
# text_file = open("gmm_diffvalue.txt", "r")
# lines = text_file.readlines()
lines1 = text_file.read().split('\n')
for s in range(0,len(lines1)):
    lines1[s] = lines1[s].strip()
print (lines1)
print (len(lines1))
text_file.close()
list1 = []
# list0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# print(list0)
print(len(list1))
grouping = int(len(lines1)/30)
for s in range(0,int(len(lines1)/grouping)):
    list1.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for m in range(s*grouping, (s+1)*grouping):
        try:
            print(int(s),int(lines1[int(m)]))
            list1[int(s)][int(lines1[int(m)])]  = list1[int(s)][int(lines1[int(m)])] + 1;
        except ValueError:
            pass
print(list1)

total_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for a in range(0, len(lines1)):
    try:
        total_count[int(lines1[int(a)])] = total_count[int(lines1[int(a)])] + 1;
    except ValueError:
        pass
for i in range(0, len(total_count)):
    total_count[i] = total_count[i]/(int(len(lines1)/grouping))
check_this = 1
# for check in range(0,20):
#     check_this = check
maxx = 1
minn = 999999999
list2 = []
for s in range(0,int(len(lines1)/grouping)):
    maxx = max(maxx, list1[int(s)][check_this])
    minn = min(minn, list1[int(s)][check_this])
    list2.append(list1[int(s)][check_this])
plt.plot(list2,  color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
plt.plot((0, int(len(lines1)/grouping)), (total_count[check_this], total_count[check_this]), 'k-', )
for i in [0,1,4,6,11,15]:
    x = int(len(lines1)/grouping)/15
    plt.plot((x*i, x*i), (minn, maxx), 'k--')
plt.ylabel('Density')
plt.xlabel('Time(Segments)')
# plt.title('Cluster ' + str(check+1))
# plt.savefig('fig' + str(check+1))
plt.show()
# To display all the clusters

# maxx = 1
# minn = 999999999
# for check in range(0, 20):
#
#     list2 = []
#     for s in range(0,int(len(lines1)/grouping)):
#         maxx = max(maxx, list1[int(s)][check]/total_count[check])
#         minn = min(minn, list1[int(s)][check]/total_count[check])
#         list2.append(list1[int(s)][check]/total_count[check])
#     plt.plot(list2,  color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
#     # plt.plot((0, int(len(lines1)/grouping)), (total_count[check], total_count[check]), 'k-')
# for i in range(0, number_of_speakers + 1):
#     x = int(len(lines1)/grouping)/number_of_speakers
#     plt.plot((x*i, x*i), (minn, maxx), 'k--')
# plt.show()

# To put bits for each segment
segments = int(len(lines1)/grouping)
listOfBits = ["" for i in range(0, len(list2))]
clusters = 20
# print(listOfBits)
total_count_average = total_count
for i in range(0, clusters):
    list2 = []
    for s in range(0, int(len(lines1) / grouping)):
        list2.append(list1[int(s)][i])
    for s in range(0, len(list2)):
        if list2[s] > total_count_average[i] :
            listOfBits[s] = listOfBits[s] + '1'
        else:
            listOfBits[s] = listOfBits[s] + '0'
print(listOfBits)

listOfChanges = [0 for i in range(0, len(list2))]
def findDiff(str1, str2):
    count = 0
    for i in range(0, len(str1)):
        if(str1[i] != str2[i]):
            count = count + 1
    return count
# for i in range(0, len(listOfBits) - 1):
#     listOfChanges[i] = findDiff(listOfBits[i], listOfBits[i + 1])
for i in range(3, len(listOfBits)):
    listOfChanges[i] = findDiff(listOfBits[i], listOfBits[i - 1]) + findDiff(listOfBits[i], listOfBits[i - 2]) + findDiff(listOfBits[i], listOfBits[i - 3])
print(listOfChanges)
listOfChanges[0]
plt.plot(listOfChanges,  color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
print(len(listOfChanges), grouping)
for i in range(0, 10 + 1):
    x = int(len(lines1)/grouping)/10
    plt.plot((x*i, x*i), (0, 20), 'k--')
plt.show()

speaker = 0
con = 1
final_ans = []

maxListOfChanges = 0
for i in range(0, len(listOfChanges)):
    maxListOfChanges = max(maxListOfChanges, listOfChanges[i])
cutoff = maxListOfChanges/3
for i in range(0, len(listOfChanges)):
    # if listOfChanges[i] > cutoff and listOfChanges[i - 1] < cutoff:
    #     speaker = speaker + 1
    minn = min(listOfChanges[i-1],listOfChanges[i-2],listOfChanges[i-3])
    if listOfChanges[i] - minn > cutoff and listOfChanges[i-1] - minn < cutoff:
        speaker = speaker + 1
    for j in range(0, grouping):
        final_ans.append(speaker)
plt.plot(final_ans, color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
file1 = open('3_1.txt','w')
for item in final_ans:
  file1.write("%s\n" % item)
file1.close()
# for i in [2000,6000,12000,20000,30000]:
#     plt.plot((i, i), (0, 5), '--', color='0.5')
plt.show()