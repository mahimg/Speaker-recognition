file = open('supervised_random.txt', 'r')
lines = file.read().split('\n')
file.close()
print(lines)
print(len(lines))
print(lines[0], lines[1])
audio_length = 1*3600 + 3*60 + 45
file1 = open('supervised_random.srt', 'w')
prev = 0
count = 1
for i in range(0, len(lines) - 1):
    if lines[i].strip() != lines[i+1].strip() :
        print(lines[i].strip())
        file1.write("%d" % count)
        file1.write("\n")
        HH = prev/(60*60)
        MM = (prev % 3600) / 60
        SS = (prev % 60)
        file1.write("%02d:%02d:%02d,000 --> " % (HH, MM, SS))
        now = (audio_length*i)/len(lines)
        HH = now / (60 * 60)
        MM = (now % 3600) / 60
        SS = (now % 60)
        file1.write("%02d:%02d:%02d,000\n" % (HH, MM, SS))
        prev = now
        file1.write("Speaker %d\n\n" % count)

        count = count + 1
file1.close()

