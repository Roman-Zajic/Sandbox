import re
from wordfreq import zipf_frequency

def load_words():
  with open('words/words.txt') as word_file:
    valid_words = list(word_file.read().split())
    return valid_words

def freq(word):
  result = zipf_frequency(word, 'en')*10000000
  return int(result)


words = load_words()
words5 = []

for w in words:
  if len(w) == 5:
    words5.append(w)

# unique
words5 = list(set(words5))

mask = input('type word use # for missing letters: ').replace('#', '[a-z]')
print(mask)
matching = re.compile(mask)

matchinglist = list(filter(matching.match, words5))
print(matchinglist)
print(len(matchinglist))

exclude = input('type leters to exclude: ')

if len(exclude) > 0:
  excludelist =[]
  for l in exclude:
    for w in matchinglist:
      if l in w:
        excludelist.append(w)

  for i in excludelist:
    if i in matchinglist:
      matchinglist.remove(i)

print(matchinglist)
print(len(matchinglist))

include = input('type letters that shoud be included: ')

if len(include) > 0:
  includelist =[]
  for l in include:
    for w in matchinglist:
      if l in w:
        includelist.append(w)
else:
  includelist = excludelist

includelist.sort(key=freq)


print(includelist)
print(len(includelist))

