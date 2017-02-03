str1 = "My name is"
str2 = "thomas"

bob = str1 + str2

print bob


for letter in str2:

    print "Current letter:",letter


print len(str2)

index =0
while index < len(str2):

    letters = str2[index]
    print index,":",letters
    index = index +1


word = "bananas"
count =0
count2=0
i=0
for letter1 in word[i]:
    if letter1=='a':
        count=count +1

        print letter1, count
    if 'a' in word:
        print "found it"



print letter1, count
print word[0:3]
