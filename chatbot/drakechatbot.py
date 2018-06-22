import random
#import pdb; pdb.set_trace()

i_words = []
my_words = []
remaining = []
greetings = ['hello', 'hi', 'hey!' ,'hey']


def song_lyrics_parse():
    f = open('drakelyrics/godsplan.txt', 'r')

    for line in f:
        if '[' in line:
            continue
        line_l = line.split()
        if len(line_l) > 0:
            for l in line_l:
                if l.lower() in ['i', 'i\'m']:
                    i_words.append(line.strip('\n'))
                    break
                elif l.lower() in ['my', 'mine', 'me']:
                    my_words.append(line.strip('\n'))
                    break
                else:
                    remaining.append(line.strip('\n'))
                    break
        #print('i_words: {}\n, my_words: {}\n, remaining: {}\n'.format(i_words, my_words, remaining))

def main():

    song_lyrics_parse()

    print("Hey! I'm Drake.")

    while True:
        userinput = input(">> ")
        userinput_l = userinput.split(' ')
        for u in userinput_l:
            if u.lower() in greetings:
                print(random.choice(greetings))
                break

            elif u.lower() in ['you', 'your']:
                print(random.choice(i_words))
                break

            elif u.lower() in ['you\'re', 'youre']:
                print(random.choice(my_words))
                break

            else:
                print(random.choice(remaining))
                break


if __name__ == '__main__':
    main()
