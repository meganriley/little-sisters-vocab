def add_prefix_un(word):
    return "un" + word



def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    new_words = []
    for word in vocab_words[1:len(vocab_words)]:
        print(prefix + word)
        new_words.append(prefix + word)
    return f'{prefix} :: '  + ' :: '.join(new_words)



def remove_suffix_ness(word):
    new_word = list(word[:-4])
    if new_word[-1] == 'i':
        new_word[-1] = 'y'
        print(new_word)
        
    shortened_word = ''.join(new_word)

    return shortened_word



def noun_to_verb(sentence, index):
    #gets rid of period punctuation
    no_periods = sentence.replace('.', '')
    #splits sentence into list
    verb_arr = no_periods.split()
    #'verbifies' word at index
    verb_arr[index] += "en"
    return verb_arr[index]
    
