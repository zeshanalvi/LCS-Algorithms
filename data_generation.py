import random, string
import time

def generate_random_characters(n):
    random_characters = []
    for _ in range(n):
        random_character = random.choice(string.ascii_letters)  # Using ascii letters for random characters
        random_characters.append(random_character)
    return random_characters

def generate_sequences(characters, min_length, max_length, num_sequences):
    sequences = []
    for _ in range(num_sequences):
        length = random.randint(min_length, max_length)
        sequence = ''.join(random.choice(characters) for _ in range(length))
        sequences.append(sequence)
    return sequences


def prep(d,lenE,m,n,E):
    if(lenE!=len(E)):
        E = generate_random_characters(lenE)   # Convert set to list
    sequences = generate_sequences(E, m, n, d)
    #for seq in sequences:
        #print(seq)
    #print(type(sequences),type(sequences[0]))
    return sequences,E

