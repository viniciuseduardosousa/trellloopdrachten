import random

original = "hallo"
originalrandom = ''.join(random.sample(original, len(original)))
print(originalrandom)