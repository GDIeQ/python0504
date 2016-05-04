scores= [60,73,81,95,34]
n=5
i=0
total=0
total2=0
anw=0
while i < 5:
    total += scores[i]
    total2 += (scores[i]*scores[i])
    i += 1
avg = total/n
i = 0
while i< 5:
    anw += (scores[i] - avg)
    i += 1

print("total = "+str(total))
print("avg = "+str(avg))
print("total2 = "+str(total2))
print("anw = "+str(anw))
