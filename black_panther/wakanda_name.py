from fuzzywuzzy import fuzz
import re
import string
import collections
import gender_guesser.detector
import random

vowels = ['o', 'i', 'y', 'e', 'a','u']
consonants =['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm' ,'n' ,'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
wakandan_masculine_names = ["T'Challa", "T'Chaka", "W'Kabi", "N'Jobu", "N'Jadaka", "M'Baku", "Zuri", "Azzuri",
"T'Shan", "S'Yan", "N'Kano", "Q'Ran", "B'Tumba", "N'Baza", "T'Chanda", "N'Gamo", "N'Iix", "N'Tomo",
"W'Tambi", "D'Vanu", "T'Swana", "T'Kora", "N'Baku", "B'Gali", "G'Mal", "N'Gami", "D'arun",
"B'Ntro", "K'Shan", "K'Tyah", "M'Daka", "M'Wabu", "M'Gari", "M'Demwe", "N'Kono", "N'Baaka", "N'Yaga"]

wakandan_feminine_names = ["Okoye", "Nakia", "Shuri", "Ramonda", "Ayo", "Aneka", "Dalia", "Lulu", "Nailah",
"Nareema", "Onyeka", "Teela", "Asira", "Folami", "Mbali", "Zola", "Yami", "Zari", "Jahniss", "Amara",
"Nehanda", "Andebah", "Okusana", "Chandra", "Zawadi", "Onome", "Abena", "Asha"]

#algorithm
'''
Take user Input
use gender module to determine gender
use fuzzywuzzy to find closest known Wakandan name; match the name length
run name through vowel cipher
run name through consonant cipher
'''

def anti_vowel(name):
    '''Strips away vowels from a name'''
    result = re.sub(r'[AEIOU]', '', name, flags=re.IGNORECASE)
    table = str.maketrans({key: None for key in string.punctuation})
    result = result.translate(table)
    return result

def translate_name(your_name, similar_name):
    your_consonants = anti_vowel(your_name)
    similar_consonants = anti_vowel(similar_name)

    if len(your_consonants) > len(similar_consonants):
        length_difference = len(your_consonants) - len(similar_consonants)
        your_consonants = your_consonants[:-length_difference]
    elif len(your_consonants) < len(similar_consonants):
        length_difference = len(similar_consonants) - len(your_consonants)
        random.seed(length_difference)
        for _ in range(length_difference):
            your_consonants = your_consonants + random.choice(consonants)


    translation_table = str.maketrans(similar_consonants, your_consonants)
    return similar_name.translate(translation_table)

def get_masculine_name(your_name):
    pass

def get_feminine_name(your_name):
    pass

def main():
    pass

if __name__ == '__main__':
    main()
