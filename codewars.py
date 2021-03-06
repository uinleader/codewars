romanNumbers = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

vowels = ['a', 'e', 'i', 'o', 'u']

scoreLetter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# https://www.codewars.com/kata/5648b12ce68d9daa6b000099
def BusStops(bus_stops):
    bus = []
    bus_stops = bus_stops.split()
    for entry in bus_stops:
        bus.append(entry.split(','))
    # Good Luck!
    peopleNum = 0;
    print(bus)
    for stop in bus:
        peopleNum = peopleNum + int(stop[0]) - int(stop[1])
    return peopleNum

# https://www.codewars.com/kata/5467e4d82edf8bbf40000155
def descending_order(num):
    arr = []
    result = ''
    for n in str(num):
        arr += n
    SArr = sorted(arr, reverse=True)
    for entry in SArr:
        result += entry
    return result

# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
def intFilter(l):
    j = l.split()
    result = []
    'return a new list with the strings filtered out'
    for n in j:
        try:
            k = int(n)
            result.append(k)
        except:
            pass
    return result

# https://www.codewars.com/kata/5262119038c0985a5b00029f
def primeCheck(num):
    num = int(num)
    if num < 2:
        return False
    a = 1
    while num % a == 0:
        a += 1
    b = a**(num-1)-1
    if b % num == 0:
        return 'Prime Number'
    else:
        return 'Not Prime Number'

# https://www.codewars.com/kata/51b6249c4612257ac0000005
def romanNum(roman):
    arr = []
    result = 0
    for letter in roman:
        arr.append(romanNumbers.get(letter))
    for idx, num in enumerate(arr):
        nID = idx + 1
        if nID < arr.__len__() and num < arr[nID]:
            result -= num
        else:
            result += num
    return result

# https://www.codewars.com/kata/520b9d2ad5c005041100000f
def pigLatin(text):
    result = ''
    wString = text.split()
    for word in wString:
        if word.isalpha():
            L_word = word[1:] + word[0] + 'ay'
            result += L_word + ' '
        else:
            result += word + ' '
    result = result[:-1]
    return result

# https://www.codewars.com/kata/54ff3102c1bad923760001f3
def vowelsCount(input_str):
    num_vowels = 0
    # your code here
    for letter in input_str:
        if letter in vowels:
            num_vowels += 1
    return num_vowels

# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/
def high(string):
    words = string.split()
    scores = {}
    for word in words:
        score = 0
        for letter in word:
            score += scoreLetter.index(letter)+1;
        scores[word] = score
    sortedScores = sorted(scores.values(), reverse=True)
    for word, score in scores.items():
        if score == sortedScores[0]:
            return word




