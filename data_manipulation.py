import pandas as pd
from collections import defaultdict

med_data = pd.read_csv('static/dataset/allMeds.csv')

med_full_names = med_data['name']
med_name = []

medicines = []


for i in med_full_names:
    i = i.lower()
    words = i.split()
    medicines.append(words[0])

# print(medicines)

vec = defaultdict(list)
for word in medicines:
    vec[word[0]].append(word)

# ch = 'a'
# for i in range(26):
#   print(f"for {ch}: {len(vec[ch])}) ...example: {vec[ch][0]}")
#   ch = chr(ord(ch) + 1)
