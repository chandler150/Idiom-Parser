import json
from collections import defaultdict

#from gensim.test.utils import datapath
#from gensim.models.word2vec import Text8Corpus, LineSentence
#from gensim.models.phrases import Phrases, ENGLISH_CONNECTOR_WORDS
from pprint import pprint
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import brown
import os
# Preset

#pprint(data)
#GOAL test recognition of these in Brown corpus

def get_idioms():
    with open("idiom_repository.json", "r") as read_file:
        data = json.load(read_file)

    #return data ## Trial to see
    idioms = []
    variations = []
    for i in range(len(data)):
        idioms.append(data[i]['idiom'])

        if len(data[i]['variations']) > 0:
            for s in data[i]['variations']:
                variations.append(s)

    for i in range(len(variations)):
        idioms.append(variations[i])

    with open('idioms.txt', 'w') as f:
        for x in idioms:
            f.write(str(x) + '\r')

    return idioms
def get_connector_words(idioms):

    dict = {}
    dict2 = {}
    count = 0
    for i in idioms:
        i = word_tokenize(i)
        if i[0] not in dict2:
            dict2[i[0]] = {'connector': [i[1:-1]], 'end': [[i[-1]]]}
        else:
            dict2[i[0]] = {'connector': dict2[i[0]].get('connector') + [i[1:-1]],
                          'end': dict2[i[0]].get('end') + [[i[-1]]]}

        '''main1 = word_tokenize(i['idiom'])
        dict[i['id']] = {'start': [main1[0]], 'connectors': main1[1:-1], 'end': [main1[-1]]}
        other1 = []
        if len(i['variations']) > 0:
            for k in range(len(i['variations'])):
                other1 = word_tokenize(i['variations'][k])
                if other1[0] not in dict[i['id']]['start']:
                    #breakpoint()
                    dict[i['id']]['start'] = dict.get(i['id']).get('start') + [other1[0]]
                    #breakpoint()
                for m in other1[1:-1]:
                    #breakpoint()
                    if m not in dict[i['id']]['connectors']:
                        #breakpoint()
                        dict.get(i['id']).get('connectors') + [m]
                if other1[-1] not in dict[i['id']]['end']:
                    dict.get(i['id']).get('end') + [other1[-1]]

'''

    # print(dict2)
    return dict2



'''
    connector_words = []
    not_connector_words = []
    start_words = []
    end_words = []
    dict = {}
    count = 0
    for i in idioms:
        tokens = word_tokenize(i)
        #print(tokens)
        dict[count] = {'start': tokens[0], 'connectors':tokens[1:-1], 'end': tokens[-1]}
        start_words.append(tokens[0])
        for i in (tokens[1:-1]):
            if i not in connector_words:
                connector_words.append(i)

        not_connector_words.append(tokens[0])
        not_connector_words.append(tokens[-1])
        count += 1
    #print(connector_words)
    #print(not_connector_words)
    #print('before',len(connector_words))
    #print(dict)
    for i in not_connector_words:
        if i in connector_words:
            connector_words.remove(i)
    #print('after',len(connector_words))
    return connector_words'''


def analyze_corpus(sentence, words):
    '''Returns a dictionary containing the found idioms within the input: sentence.
    Sentence should be inputted as a tokenized list, and is ideal as a Corpus'''
    dict = {}
    word_count = 0
    word_count_ret = 0
    for word in sentence:
        worda = word
        if word_count_ret <= word_count:
            word_count_ret, phrase = check_phrase(worda,word_count,words, sentence)
            if phrase is not None:
                dict[phrase] = dict.get(phrase,0) + 1
                phrase = None
        word_count += 1
    return dict

def check_sentence(sentence, words):
    '''Check sentence will accept a list of tokenized words as sentence, and output
    any idioms found as a delimited phrase with ('_') as the delimiter.
    Words is a dictionary of idioms in the form of
    {'first_word': {'connector': [[tokenized, words]], 'end': [[tokenized_word]] }} '''
    #print(sentence)
    start_token, in_between = None, []
    word_count = 0
    word_count_ret = 0
    for word in sentence:
        worda = word
        if word_count_ret <= word_count:
            word_count_ret, phrase = check_phrase(worda,word_count,words, sentence)
            if phrase is not None:
                yield phrase
                phrase = None
            else:
                yield word
        word_count += 1
    return
def check_phrase(worda,word_count,words, sentence):
    phrase = []
    inc = 0
    start_token = None
    in_between = []
    #if worda == 'that':
    #    breakpoint()
    if worda in words:
        start_token = worda
        #print("start_token",start_token)
        inc += 1
    if start_token:
        #print("next words", sentence[word_count+inc:])
        for i in sentence[word_count+inc:]:
            next_word = i                                   #Checks Words beyond Start token
            #print('next word: ', next_word)
            for i in words[start_token]['connector']:       #Checks all variations of connector words
                #print('connectors: ', i)
                #if next_word == 'fail':
                    #breakpoint()
                if next_word in i:                          # in a potential phrase
                    #print("YES IT IS")
                    in_between.append(next_word)            #Adds word of potential phrase to list
                    #print('in_between: ', in_between)
                    inc += 1                                #Removes word from next runthrough
                    flag1 = 0
                    break
                if next_word not in i:
                    flag1 = 1                               #next_word was not a connector
                    break
            for i in words[start_token]['end']:
                if next_word in i:                          #End of phrase
                    if len(in_between) == len(words[start_token]['connector'][words[start_token]['end'].index([next_word])]):
                        #Verifies the length of in_between words saved is the same as it should be for the
                        #idiom it thinks it is, this could maybe be more specific
                        phrase = score_candidate(start_token, next_word, in_between)
                        #print('phrase: ', phrase)
                        inc += 1
                        flag2 = 0
                        return word_count+inc, phrase            #yield the delimited phrase & new count
                    else:
                        #Mixup where it finds end word but didn't find in between words
                        #double check these flags, but I think so,
                        flag2 = 1
                        flag1 = 1
                        break
                else:
                    flag2 =1                              #next_word was not an end_word
                    break
            if (flag1+flag2) > 1:                         #neither a connector or end word
                start_token = None
                flag1 = 0
                flag2 = 0
                break
    else:
        return word_count+inc, None
    return word_count+inc,None

'''
        #print('The test word is:',word)
        #print('The Start Token is:',start_token)
        #breakpoint()
        if start_token is None:
            if word in words:
                print('state=2')
                #Start of a potential phrase
                start_token = word
        if start_token:
            try:
                if word in words[start_token]['end']:
                    print('state=3')
                    #means word is an end to the start token I.e. a full phrase
                    phrase = score_candidate(start_token, word, in_between)
                    #print(phrase)
                    yield phrase
                    start_token, in_between = None, []
            except:
                print('state=4')
                continue
        if start_token:
            #print('The potential connector words are:', words[start_token]['connector'])
            for i in words[start_token]['connector']:
                if word in i:
                    # We're inside a potential phrase: add the connector word and keep growing the phrase.
                            #print(word)
                    print('state=5')
                    in_between.append(word)
                    #print('The inbetween is:', in_between)
                elif word not in i:
                    print('state=6')
                    for i in in_between:
                        print('state=7')
                        yield i
                    yield word
                    #start_token, in_between = None, []

                #yield word
        else:
            print('state=8')
            #breakpoint()
            #Not in a phrase
            #print('end',word)

            yield word
            #start_token, in_between = None, []
            #else:
                # Not inside a phrase: emit the connector word and move on.
                #yield word, None
'''
'''
#OLD CODE FROM GENSIM
    start_token, in_between = None, []
    for word in sentence:
        if word not in self.connector_words:
            # The current word is a normal token, not a connector word, which means it's a potential
            # beginning (or end) of a phrase.
            if start_token:
                # We're inside a potential phrase, of which this word is the end.
                phrase, score = self.score_candidate(start_token, word, in_between)
                if score is not None:
                    # Phrase detected!
                    yield phrase, score
                    start_token, in_between = None, []
                else:
                    # Not a phrase after all. Dissolve the candidate's constituent tokens as individual words.
                    yield start_token, None
                    for w in in_between:
                        yield w, None
                    start_token, in_between = word, []  # new potential phrase starts here
            else:
                # Not inside a phrase yet; start a new phrase candidate here.
                start_token, in_between = word, []
        else:  # We're a connector word.
            if start_token:
                # We're inside a potential phrase: add the connector word and keep growing the phrase.
                in_between.append(word)
            else:
                # Not inside a phrase: emit the connector word and move on.
                yield word, None
    # Emit any non-phrase tokens at the end.
    if start_token:
        yield start_token, None
        for w in in_between:
            yield w, None

'''


def score_candidate(word_a, word_b, in_between):
    '''Based on Gensim's Multi-Word-Expression (MWE) Finder,
    this simple code joins previously found MWE's into a single token'''
    phrase = '_'.join([word_a] + in_between + [word_b])
    return phrase

def gensim(idioms,connections):
    '''Depreciated'''
    # Create training corpus. Must be a sequence of sentences (e.g. an iterable or a generator).
    #test
    #sentences = Text8Corpus(datapath('testcorpus.txt'))
    #print(sentences)
    #trial
    sentences = LineSentence(datapath('/Users/chandlerjones/Documents/School/Grad/CSC 582/Coding/Project/idioms.txt'))
    #Actual
    #sentences = idioms
    #print(sentences)
    #NEW TEST
    #sentences = [["to", "hell", "and", "back"]]
    # Each sentence must be a list of string tokens:
    first_sentence = next(iter(sentences))
    #print(first_sentence)
    #print(first_sentence[:10])
    #['computer', 'human', 'interface', 'computer', 'response', 'survey', 'system', 'time', 'user', 'interface']
    # Train a toy phrase model on our training corpus.
    phrase_model = Phrases(sentences, min_count=1, threshold=-1,scoring='npmi',connector_words=connections)#connector_words=ENGLISH_CONNECTOR_WORDS)
    #Test connector words = all words which are not the start and finish of all strings
    #print(phrase_model.vocab)
    #print(phrase_model.find_phrases(sentences))
    #hi = phrase_model.analyze_sentence(["hi I love human interfaces"])
    #print(hi)
    # Apply the trained phrases model to a new, unseen sentence.
    new_sentence = ['I', 'can\'t', 'hear', 'you', 'over', 'the','sound','of', 'kicked', 'the', 'bucket']

    #****************************THE IMPORTANT PART**********************************************

    #First Iteration
    neato = phrase_model[new_sentence]
    print(phrase_model[new_sentence])
    hi = phrase_model.export_phrases()
    print(hi)
    for x in phrase_model.export_phrases():
        print(x, " , {}".format(phrase_model.export_phrases()[x]))
    #Second Iteration
    triphrase = Phrases([phrase_model[new_sentence]], min_count=1, threshold=1,scoring='npmi')
    print(triphrase.vocab)
    print(triphrase[phrase_model[new_sentence]])
    bye = triphrase.export_phrases()
    print(bye)
    #Third Iteration
    quadphase = Phrases([triphrase[phrase_model[new_sentence]]], min_count=1, threshold=-1, scoring='npmi')
    print(quadphase[triphrase[phrase_model[new_sentence]]])

    seeya = quadphase.export_phrases()
    print(seeya)

    #How many iterations are necessary?
    #How can I automate this to autosolve necessary iterations?
            #Recursive Function?

    #****************END OF IMPORTANT SECTION***************************************************************

    #['trees_graph', 'minors']
    # The toy model considered "trees graph" a single phrase => joined the two
    # tokens into a single "phrase" token, using our selected `_` delimiter.
    # Apply the trained model to each sentence of a corpus, using the same [] syntax:
    for sent in phrase_model[sentences]:
        #print("hi,",sent)
        pass
    # Update the model with two new sentences on the fly.
    #print(phrase_model.vocab)
    #phrase_model.add_vocab([["This", "is", "the", "end!"]])
    #print(phrase_model.vocab)
    # Export the trained model = use less RAM, faster processing. Model updates no longer possible.
    frozen_model = phrase_model.freeze()
    # Apply the frozen model; same results as before:
    frozen_model[new_sentence]
    #['trees_graph', 'minors']
    # Save / load models.
    frozen_model.save("/tmp/my_phrase_model.pkl")
    model_reloaded = Phrases.load("/tmp/my_phrase_model.pkl")
    model_reloaded[['trees', 'graph', 'minors']]  # apply the reloaded model to a sentence
    #['trees_graph', 'minors']
    #for phrase, score in phrases.find_phrases(sentences).items():
    #    print(phrase, score)

def check_brown(connector_words):
    from nltk.corpus import brown
    dict = {}
    #print(brown.sents()[103])
    print("Compiling Idioms in Brown ...")
    for sentence in brown.sents():
        #breakpoint()
        counter = analyze_corpus(sentence,connector_words)
        dict.update(counter)
    return dict

def check_coca(COCA,connector_words):
    dict = {}

    print("Compiling Idioms in Coca ...")
    for sentence in COCA:
        sentence = word_tokenize(sentence)
        counter = analyze_corpus(sentence, connector_words)
        dict.update(counter)
    return dict

def Sum(dict):
   sum_ = 0
   for i in dict.values():
      sum_ = sum_ + i
   return sum_

def get_coca():             #start,end
    #with open("/home/cjones87/COCA/text_unzipped/w_spok_2012.txt", "r") as read_file:
    with open("w_spok_2012.txt", "r") as read_file:
        data = read_file.read()
        coca = sent_tokenize(data)
        print("there are {} sentences in this one.".format(len(coca)))
        print("Checking COCA for idioms")
    return coca

def main():


    idioms = get_idioms()
    connector_words = get_connector_words(idioms)
    '''
    #Demo Step 1:
    for key, value in sorted(connector_words.items()):
        print(key, ' : ', value)
    '''
    '''
    #Demo Step 2:
    sentence = ['These', 'words', 'fail', 'me', 'they', 'are', 'my', 'Achilles', 'heel']
    hi = check_sentence(sentence, connector_words)
    newsent = []
    for i in hi:
       newsent.append(i)
    print('Test Sentence: ', sentence)
    print('Test Compile: ', newsent)
    counter = analyze_corpus(sentence,connector_words)
    print('Test Counter: ', counter)
    '''
    #'''
    #Demo Step 3:
    brownoutput = check_brown(connector_words)
    NumIdioms = Sum(brownoutput)
    for key, value in sorted(brownoutput.items(), key=lambda x: x[1]):
        print("{} : {}".format(key, value))

    print("There are {} idioms in this section of the Brown Corpus" .format(NumIdioms))
    #'''
    '''
    cocainput = get_coca()

    cocaoutput = check_coca(cocainput,connector_words)
    print(cocaoutput)
    NewNum = Sum(cocaoutput)
    print("There are {} idioms in this section of the COCA Corpus".format(NewNum))
    '''
if __name__ == '__main__':
    main()