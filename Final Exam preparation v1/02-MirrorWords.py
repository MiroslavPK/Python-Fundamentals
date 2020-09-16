import re

text = input()
pattern = r'([@|#])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1'

matches = re.findall(pattern, text)
mirror_words = []

for match in matches:
    if match[1] == match[2][::-1]:
        mirror_words.append(f'{match[1]} <=> {match[2]}')

if len(matches) == 0:

    print('No word pairs found!')

else:

    print(f'{len(matches)} word pairs found!')

if len(mirror_words) == 0:

    print('No mirror words!')
else:

    print('The mirror words are:')
    print(', '.join(mirror_words))
