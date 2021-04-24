def goodie_dilemma(ls, n, k):

    mini = 2147483647

    for i in range((n - k) + 1):
          
        diff = ls[i + k - 1] - ls[i]

        if (diff<mini):

            mini = diff
            temp = ls[i:i+k:]


    return (temp)


def getKey(val):
	for key, value in goodies.items():
		if val == value:
			return key

	return -1




f = open("sample_input.txt", "r")
# f = open("sample_input1.txt", "r")
# f = open("sample_input2.txt", "r")

k = int(f.readline()[21])


f.readline()
f.readline()
f.readline()

goodies = {}

for x in (f.readlines()):

    if (x!=""):
        a,b = x.strip().split(": ")

        goodies[a] = int(b)

ls = list(goodies.values())

n = len(ls)

ls.sort()

# print(ls)

out = goodie_dilemma(ls,n,k)


w = open("sample_output.txt", "w")

w.write("The goodies selected for distribution are:\n")

w.write("\n")

for i in out:
    w.write(getKey(i) + ": " + str(i) + "\n")

w.write("\n")

w.write("And the difference between the chosen goodie with highest price and the lowest price is " + str(out[-1]-out[0]))