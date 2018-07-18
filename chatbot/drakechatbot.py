import random
import string

drakelyrics = ['godsplan.txt', 'backtoback.txt', 'hotlinebling.txt', 'inmyfeelings.txt']

i_words = []
my_words = []

remaining = []

greetings = ['hello', 'hi', 'hey!' ,'hey', 'yo']
goodbyes = ['bye', 'goodbye']
line_bank = []


def song_lyrics_parse():
    for song in drakelyrics:
        file = open('drakelyrics/clean_' + song, 'r')
        for line in file:
            if '[' in line:
                continue

            if line.strip('\n') in line_bank:
                continue
            line_l = line.translate(str.maketrans('','',string.punctuation))
            line_l = line_l.split()

            if len(line_l) > 0:
                response_found = False
                for l in line_l:
                    line_bank.append(line.strip('\n'))
                    if l.lower() in ['i', 'im']:
                        i_words.append(line.strip('\n'))
                        response_found = True
                        break
                    elif l.lower() in ['my', 'mine', 'me']:
                        my_words.append(line.strip('\n'))
                        response_found = True
                        break
                if response_found == False:
                    remaining.append(line.strip('\n'))
        #print('i_words: {}\n, my_words: {}\n, remaining: {}\n'.format(i_words, my_words,remaining))
    file.close()

def process_response(userinput):
    if userinput.strip() is '':
        return("Are you still there?")
    userinput_l = userinput.translate(str.maketrans('','',string.punctuation))
    userinput_l = userinput_l.split(' ')


    response_found = False
    for u in userinput_l:
        if u.lower() in greetings:
            response_found = True
            return(random.choice(greetings))

        elif u.lower() in goodbyes:
            response_found = True
            print("I just hope that you miss me a little when I'm gone.")
            quit()

        elif u.lower() in ['you', 'you\'re', 'u', 'Drake']:
            response_found = True
            return(random.choice(i_words))

        elif u.lower() in ['your', 'ur', 'yours']:
            response_found = True
            return(random.choice(my_words))

        else:
            continue

    if response_found is False:
        return(random.choice(remaining))

def main():

    song_lyrics_parse()

    print("Hey! I'm Drake.")

    while True:
        userinput = input(">> ")
        print(process_response(userinput))


if __name__ == '__main__':
    main()
