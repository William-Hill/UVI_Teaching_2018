import fileinput
import string

drakelyrics = ['godsplan.txt', 'backtoback.txt', 'hotlinebling.txt','inmyfeelings.txt']

badwords_dict = {
    'nigga' : 'brotha',
    'niggas' : 'brothas',
    'shit'  : 'stuff',
    'damn' : 'dang',
    'fuck' : 'mess',
    'fuckin' : 'messin',
    'ass' : 'butt',
    'pussy' : 'CENSORED',
    'bitch' : 'chick',
    'bitches' : 'chicks'
}

def main():
    for song in drakelyrics:
        f = open('drakelyrics/' + song, 'r+')
        n = open('drakelyrics/clean_' + song, 'w+')
        for line in f:
            if '[' in line:
                continue
            line_l = line.split()
            if len(line_l) > 0:
                for i in range(len(line_l)):
                    #TODO: how to preserve punctuation?
                    stripped_word = line_l[i].translate(str.maketrans('','',string.punctuation))
                    stripped_word = stripped_word.lower()
                    if stripped_word in badwords_dict.keys():
                        word_new = badwords_dict[stripped_word]
                        ###This is failing
                        line_l[i] = stripped_word.replace(stripped_word, word_new)
            line_n = ' '.join(line_l)
            n.write(line_n)
            n.write('\n')
    f.close()
    n.close()

if __name__ == '__main__':
    main()
