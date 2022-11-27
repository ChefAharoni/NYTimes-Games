import json

with open('dictionary.json') as json_f:
    data = json.load(json_f)

webster_dict = set(data.keys())  # Converts its keys as a set.

# This dictionary saves the definitions as keys.
