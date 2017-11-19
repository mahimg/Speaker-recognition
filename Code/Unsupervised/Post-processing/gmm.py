import matplotlib.pyplot as plt

text_file = open("2.txt", "r")
# text_file = open("gmm_diffvalue.txt", "r")
# lines = text_file.readlines()
lines1 = text_file.read().split('\n')
count = 0
for s in range(0,len(lines1)):
    try:
        lines1[s] = int(lines1[s].strip())
    except ValueError:
        lines1[s] = 0

print (lines1)
print (len(lines1), count)
plt.scatter(list(range(0, len(lines1))), lines1)
plt.show()
text_file.close()