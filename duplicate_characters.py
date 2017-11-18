// this programs finds the duplicate characters in a string
dict = {}
def find_duplicate(word):
    if len(word) != 0:
        for alpha in word:
            if alpha not in dict:
                dict[alpha] = 1
            else:
                dict[alpha] += 1
        return dict
    else:
        print "invalid input"

print find_duplicate("java").items()
print find_duplicate("").items()
