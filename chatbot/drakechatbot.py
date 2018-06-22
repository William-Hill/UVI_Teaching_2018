import random
i_words = []
my_words = []
remaining = []
greetings = ['hello', 'hi', 'hey!' ,'hey',]


def song_lyrics_parse():
    f = open('drakelyrics/godsplan.txt', 'r')

    for line in f:
        line_l = line.split()
        if '[' in line_l:
            break
        for l in line_l:
            if l.lower() in ['i', 'i\'m']:
                i_words.append(line.strip('/n'))
                break
            elif l.lower() in ['my', 'mine']:
                my_words.append(line.strip('/n'))
                break
            else:
                remaining.append(line.strip('/n'))
                break

def main():

    song_lyrics_parse()

    print("Hey! I'm Drake.")

    while True:
        userinput = input(">> ")
        userinput_l = userinput.split(' ')
        for u in userinput_l:
            if u.lower() in greetings:
                print(random.choice(greetings))

            elif u.lower() in ['you', 'your']:
                print(random.choice(i_words))

            elif u.lower() in ['you\'re', 'youre']:
                print(random.choice(my_words))

            else:
                print(random.choice(remaining))


if __name__ == '__main__':
    main()
