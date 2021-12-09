import random

# Random number from 1 to 100
print(random.randrange(1, 100))


# Winner picker:
names = ['Mike', 'Alice', 'Jhon', 'Vasyl']
print(random.choice(names))


# Music collection shuffle:
tracks = ['1.mp3', '2.mp3', '4.wav']
random.shuffle(tracks)
print(tracks)

