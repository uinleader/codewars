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


def descending_order(num):
    arr = []
    result = ''
    for n in str(num):
        arr += n

    SArr = sorted(arr, reverse=True)

    for entry in SArr:
        result += entry

    return result


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


def primeCheck(num):
    num = int(num)
    if num < 2:
        return False
    a = 1
    while num % a == 0:
        a += 1
    if (a ** (num - 1) - 1) % num == 0:
        return 'Prime Number'
    else:
        return 'Not Prime Number'


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


def vowelsCount(input_str):
    num_vowels = 0
    # your code here
    for letter in input_str:
        if letter in vowels:
            num_vowels += 1

    return num_vowels
