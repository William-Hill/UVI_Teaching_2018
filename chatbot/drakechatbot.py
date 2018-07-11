import random
import string

#TODO: add a goodbye
drakelyrics = ['godsplan.txt', 'backtoback.txt', 'hotlinebling.txt', 'inmyfeelings.txt']

i_words = []
my_words = []
remaining = []
greetings = ['hello', 'hi', 'hey!' ,'hey', 'yo']
line_bank = []
bad_responses = ['', ' ', None]
#TODO: use tensorflow to create a model to map words to each other

def song_lyrics_parse():
    for song in drakelyrics:
        f = open('drakelyrics/' + song, 'r')
        #TODO: make it more "random"
        for line in f:
            if '[' in line:
                continue
            if line.strip('\n') in line_bank:
                continue
            line_l = line.translate(str.maketrans('','',string.punctuation))
            line_l = line_l.split()
            if len(line_l) > 0:
                for l in line_l:
                    line_bank.append(line.strip('\n'))
                    if l.lower() in ['i', 'im']:
                        i_words.append(line.strip('\n'))
                        break
                    elif l.lower() in ['my', 'mine', 'me']:
                        my_words.append(line.strip('\n'))
                        break
                    else:
                        remaining.append(line.strip('\n'))
                        break
        #print('i_words: {}\n, my_words: {}\n, remaining: {}\n'.format(i_words, my_words, remaining))
    f.close()

def process_response(userinput, response_found = False):
    pass

def main():

    song_lyrics_parse()

    print("Hey! I'm Drake.")

    while True:
        response_found = False
        userinput = input(">> ")
        if userinput in bad_responses:
            print("Are you still there?")
            continue
        userinput_l = userinput.translate(str.maketrans('','',string.punctuation))
        userinput_l = userinput_l.split(' ')
        for u in userinput_l:
            if u.lower() in greetings:
                response_found = True
                print(random.choice(greetings))
                break

            elif u.lower() in ['you', 'your', 'u']:
                response_found = True
                print(random.choice(i_words))
                break

            elif u.lower() in ['you\'re', 'youre', 'ur']:
                response_found = True
                print(random.choice(my_words))
                break

            else:
                continue
        if response_found is False:
            print(random.choice(remaining))


if __name__ == '__main__':
    main()
