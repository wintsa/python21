'''
def f(x: int) -> int:
    return x + 1

a = [1.0]
print(f(a[0]))


def a():
    print("a")

def b():
    print("b")

c = a

c()

for c in [a, b]:
    c()

c = lambda x,y: x*x

for i in 11, 2, 3:
    print((lambda x,y: i*x)(i,0))



l = [2, 3, 5, 6, 9, 1, 2, 6]  # list
s = {2, 3, 5, 6, 9, 1, 2, 6}  # set
t = (2, 3, 5, 6, 9, 1, 2, 6)  # tuple

text = "Два молодых человека, студент и офицер, друзья с детства, были одних лет и оба красивы, но не похожи друг на друга."

print(text[5:10])


for a in s:
    print(a)

print(l[0])
print(t[0])
print(list(s)[0])

print(t, s, set(l), sep=",\n", end=";\n")



'''

d = {1: "one", 2: "two", 3: "three"}
d2 = {"1": "one", "2": "two", "3": "three", 4: "four"}


# print(d2[1])

def get(self, key, default=None):
    """
    Return the value for key if key is in the dictionary, else default.
    If default is not given, it defaults to None, so that this method
    never raises a KeyError.
    """
    try:
        return self[key]
    except KeyError:
        return default


'''
try:
    a = int(input())
except Exception:
    print("incorrect number")
'''

print(get(d2, 1, "null"))

text = "молодых человека, студент и офицер, друзья с детства, были одних лет и оба красивы, но не похожи друг на друга." \
       "Борис был высокий белокурый юноша с правильными тонкими чертами спокойного и красивого лица. Николай был" \
       "невысокий курчавый молодой человек с открытым выражением лица. На верхней губе его уже показывались черные" \
       "волосики, и во всем лице выражались стремительность и восторженность. Николай покраснел, как только вошел в" \
       "гостиную. Видно было, что он искал и не находил, что сказать; Борис, напротив, тотчас же нашелся и рассказал" \
       "спокойно, шутливо, как эту Мими, куклу, он знал еще молодою "

text = text.lower()

abc = dict()


for a in text:
    n = abc.get(a, 0)
    abc[a] = n + 1

l = list(abc.items())

charsorted = sorted(l, key=lambda x: x[0])
charsorted = sorted(charsorted, key=lambda x: x[1], reverse=True)

for tup in charsorted:
    #    number = abc[char]
    (char, number) = tup
    print(char + ": " + str(number))
