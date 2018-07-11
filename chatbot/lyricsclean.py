drakelyrics = ['godsplan.txt', 'backtoback.txt', 'hotlinebling.txt', 'inmyfeelings.txt']
#TODO: remove bad words if even a part of the word is found
badwords = ['nigga', 'shit', 'damn', 'fuck', 'ass', 'pussy', 'bitch', 'bitches', 'niggas']

for song in drakelyrics:
    f = open('drakelyrics/' + song, 'r')
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

if __name__ == '__main__':
    main()
