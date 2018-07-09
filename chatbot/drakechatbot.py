import random
import string
#import pdb; pdb.set_trace()
drakelyrics = ['godsplan.txt', 'backtoback.txt', 'hotlinebling.txt']

i_words = []
my_words = []
remaining = []
greetings = ['hello', 'hi', 'hey!' ,'hey', 'yo']
line_bank = []
bad_responses = ['', ' ', None]
#TODO: use tensorflow to create a model to map words to each other

def song_lyrics_parse():
    #TODO: read in list of multiple songs: for l in drakelyrics
    for song in drakelyrics:
        f = open('drakelyrics/' + song, 'r')
        #TODO: strip duplicate/repetitive lines
        #TODO: strip punctuation
        #TODO: make it more "random"
        #TODO: limit responses for empty lines
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
def main():

    song_lyrics_parse()

    print("Hey! I'm Drake.")

    while True:
        userinput = input(">> ")
        if userinput in bad_responses:
            print("Are you still there?")
            continue
        userinput_l = userinput.translate(str.maketrans('','',string.punctuation))
        userinput_l = userinput_l.split(' ')
        for u in userinput_l:
            if u.lower() in greetings:
                print(random.choice(greetings))
                break

            elif u.lower() in ['you', 'your', 'u']:
                print(random.choice(i_words))
                break

            elif u.lower() in ['you\'re', 'youre', 'ur']:
                print(random.choice(my_words))
                break

            else:
                continue
        #TODO: how do we make it so that once we get to the end of the user input string, we print a random choice?
        #print(random.choice(remaining))
        #break


if __name__ == '__main__':
    main()
