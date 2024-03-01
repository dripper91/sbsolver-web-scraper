import sys

sys.setrecursionlimit(1000000)

vowels = ['a','e','i','o','u','y']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
c1 = consonants[:10]
c2 = consonants[10:]

vowelCombos, consCombos = [], []
vcSet, ccSet = set(), set()

def vowelDFS(vowels, curr):
    for v in vowels:
        newCurr = curr[:]
        newCurr += v
        if len(newCurr) == 3 and ''.join(sorted(list(newCurr))) not in vcSet:
            vcSet.add(''.join(sorted(list(newCurr))))
            vowelCombos.append(newCurr)
            return
        newVowels = vowels[:]
        newVowels.remove(v)
        vowelDFS(newVowels, newCurr)

def consDFS(consonants, curr):
    for c in consonants:
        newCurr = curr[:]
        newCurr += c
        if len(newCurr) == 4 and ''.join(sorted(list(newCurr))) not in ccSet:
            ccSet.add(''.join(sorted(list(newCurr))))
            consCombos.append(newCurr)
            return
        newConsonants = consonants[:]
        newConsonants.remove(c)
        consDFS(newConsonants, newCurr)

vowelDFS(vowels, "")
consDFS(c1, "")

print(vowelCombos)
print(len(vowelCombos))

print(consCombos)
print(len(consCombos))