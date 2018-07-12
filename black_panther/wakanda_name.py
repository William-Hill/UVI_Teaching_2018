from fuzzywuzzy import fuzz
import re
import string
import collections
import gender_guesser.detector as gender
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

def anti_vowel(s):
    result = re.sub(r'[AEIOU]', '', s, flags=re.IGNORECASE)
    result = result.translate(None, string.punctuation)
    return result

def translate_name(your_name, similar_name):
    your_consonants = anti_vowel(your_name)
    similar_consonants = anti_vowel(similar_name)
    print "similar_consonants:", similar_consonants

    if len(your_consonants) > len(similar_consonants):
        length_difference = len(your_consonants) - len(similar_consonants)
        your_consonants = your_consonants[:-length_difference]
    elif len(your_consonants) < len(similar_consonants):
        length_difference = len(similar_consonants) - len(your_consonants)
        random.seed(length_difference)
        for _ in range(length_difference):
            print "random_choice:", random.choice(consonants)
            your_consonants = your_consonants + random.choice(consonants)

    print "your_consonants:", your_consonants

    translation_table = string.maketrans(similar_consonants, your_consonants)
    return similar_name.translate(translation_table)

def get_masculine_name(your_name):
    similar_name_score = 0
    most_similar_name = None

    for name in wakandan_masculine_names:
        score = fuzz.ratio(your_name, name)
        if score > similar_name_score:
            similar_name_score = score
            most_similar_name = name

    print "similar_name_score", similar_name_score
    print "most_similar_name", most_similar_name
    return most_similar_name

def get_feminine_name(your_name):
    similar_name_score = 0
    most_similar_name = None

    for name in wakandan_feminine_names:
        score = fuzz.ratio(your_name, name)
        if score > similar_name_score:
            similar_name_score = score
            most_similar_name = name

    print "similar_name_score", similar_name_score
    print "most_similar_name", most_similar_name

    return most_similar_name


name_string = ''.join(wakandan_masculine_names)
print "name_string:", name_string
consonant_string = name_string.translate(None, "".join(vowels + ["'"]))
print "consonant_string:", consonant_string
print collections.Counter(consonant_string).most_common(3)


your_name = raw_input("Enter your name: ").strip()
d = gender.Detector()
gender = d.get_gender(your_name)
if gender == "unknown":
    gender = raw_input("Is your name masculine or feminine? ")

if gender == "male":
    similar_name = get_masculine_name(your_name)
else:
    similar_name = get_feminine_name(your_name)

translate_name = translate_name(your_name, similar_name)
print "translated_name: ", translate_name
