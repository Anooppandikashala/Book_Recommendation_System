# -*- coding: utf-8 -*-
"""
basic_sentiment_analysis
~~~~~~~~~~~~~~~~~~~~~~~~

This module contains the code and examples described in 
http://fjavieralba.com/basic-sentiment-analysis-with-python.html

"""
from pprint import pprint
import nltk
import yaml
import sys
import os
import re

class Splitter(object):

    def __init__(self):
        self.nltk_splitter = nltk.data.load('/home/anoop/nltk_data/tokenizers/punkt/english.pickle')
        self.nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()

    def split(self, text):
        """
        input format: a paragraph of text
        output format: a list of lists of words.
            e.g.: [['this', 'is', 'a', 'sentence'], ['this', 'is', 'another', 'one']]
        """
        sentences = self.nltk_splitter.tokenize(text)
        tokenized_sentences = [self.nltk_tokenizer.tokenize(sent) for sent in sentences]
        return tokenized_sentences


class POSTagger(object):

    def __init__(self):
        pass
        
    def pos_tag(self, sentences):
        """
        input format: list of lists of words
            e.g.: [['this', 'is', 'a', 'sentence'], ['this', 'is', 'another', 'one']]
        output format: list of lists of tagged tokens. Each tagged tokens has a
        form, a lemma, and a list of tags
            e.g: [[('this', 'this', ['DT']), ('is', 'be', ['VB']), ('a', 'a', ['DT']), ('sentence', 'sentence', ['NN'])],
                    [('this', 'this', ['DT']), ('is', 'be', ['VB']), ('another', 'another', ['DT']), ('one', 'one', ['CARD'])]]
        """

        pos = [nltk.pos_tag(sentence) for sentence in sentences]
        #adapt format
        pos = [[(word, word, [postag]) for (word, postag) in sentence] for sentence in pos]
        return pos

class DictionaryTagger(object):

    def __init__(self, dictionary_paths):
        files = [open(path, 'r') for path in dictionary_paths]
        dictionaries = [yaml.load(dict_file) for dict_file in files]
        map(lambda x: x.close(), files)
        self.dictionary = {}
        self.max_key_size = 0
        for curr_dict in dictionaries:
            for key in curr_dict:
                if key in self.dictionary:
                    self.dictionary[key].extend(curr_dict[key])
                else:
                    self.dictionary[key] = curr_dict[key]
                    self.max_key_size = max(self.max_key_size, len(key))

    def tag(self, postagged_sentences):
        return [self.tag_sentence(sentence) for sentence in postagged_sentences]

    def tag_sentence(self, sentence, tag_with_lemmas=False):
        """
        the result is only one tagging of all the possible ones.
        The resulting tagging is determined by these two priority rules:
            - longest matches have higher priority
            - search is made from left to right
        """
        tag_sentence = []
        N = len(sentence)
        if self.max_key_size == 0:
            self.max_key_size = N
        i = 0
        while (i < N):
            j = min(i + self.max_key_size, N) #avoid overflow
            tagged = False
            while (j > i):
                expression_form = ' '.join([word[0] for word in sentence[i:j]]).lower()
                expression_lemma = ' '.join([word[1] for word in sentence[i:j]]).lower()
                if tag_with_lemmas:
                    literal = expression_lemma
                else:
                    literal = expression_form
                if literal in self.dictionary:
                    #self.logger.debug("found: %s" % literal)
                    is_single_token = j - i == 1
                    original_position = i
                    i = j
                    taggings = [tag for tag in self.dictionary[literal]]
                    tagged_expression = (expression_form, expression_lemma, taggings)
                    if is_single_token: #if the tagged literal is a single token, conserve its previous taggings:
                        original_token_tagging = sentence[original_position][2]
                        tagged_expression[2].extend(original_token_tagging)
                    tag_sentence.append(tagged_expression)
                    tagged = True
                else:
                    j = j - 1
            if not tagged:
                tag_sentence.append(sentence[i])
                i += 1
        return tag_sentence

def value_of(sentiment):
    if sentiment == 'positive': return 1
    if sentiment == 'negative': return -1
    return 0

def sentence_score(sentence_tokens, previous_token, acum_score):    
    if not sentence_tokens:
        return acum_score
    else:
        current_token = sentence_tokens[0]
        tags = current_token[2]
        token_score = sum([value_of(tag) for tag in tags])
        if previous_token is not None:
            previous_tags = previous_token[2]
            if 'inc' in previous_tags:
                token_score *= 2.0
            elif 'dec' in previous_tags:
                token_score /= 2.0
            elif 'inv' in previous_tags:
                token_score *= -1.0
        return sentence_score(sentence_tokens[1:], current_token, acum_score + token_score)

def sentiment_score(review):
    return sum([sentence_score(sentence, None, 0.0) for sentence in review])

if __name__ == "__main__":
    #'''text = "What can I say about this place. The staff of the restaurant is nice and the eggplant is not bad. Apart from that, very uninspired food, lack of atmosphere and too expensive. I am a staunch vegetarian and was sorely dissapointed with the veggie options on the menu. Will be the last time I visit, I recommend others to avoid."'''
    #negative
    #text = "THis book was horrible.  If it was possible to rate it lower than one star i would have.  I am an avid reader and picked this book up after my mom had gotten it from a friend.  I read half of it, suffering from a headache the entire time, and then got to the part about the relationship the 13 year old boy had with a 33 year old man and i lit this book on fire.  One less copy in the world...don't waste your money."
    #positive
    #''' text = "Dr.Oz is an accomplished heart surgeon in the field of cardiac transplantation. He describes how he combines complementary medicine (e.g. hypnosis, reflexology, yoga, message, acupuncture. Etc) with orthodox Western medicine. There is an excellent forward by Dr Dean Ornish, and an interesting epilogue containing an overview of the complementary medicine techniques. The bulk of the book contains stories of patients Dr. Oz treated using this revolutionary way. I am a cardiologist, and I have a great interest in combining western medicine with complementary medicine, which is the reason I bought this book. However this book was a bit boring to read and was also a bit of a disappointment. Nevertheless, those interested in this new medicine, which I think will be the medicine of the new millennium, will want to read this book"'''
    
    #'''text ="It is a good book and i like this book verymuch"
    
    text ="this is an easy-to-read, very difficult book. sharma does not shy away from the ugliest, most difficult subjects but writes about them so fluidly that you find yourself going along at a steady clip, jaw dropping wider and wider. much like the subjects of abuse in this book, the reader at times can feel like he's in an abusive relationship he just can't pull away from. that's not meant to demean or minimize actual abuse victims suffer. it's only meant to highlight how deftly sharma captures abuse of all kind (institutional, familial, cultural, structural) and grabs your attention with it.$despite this book's horrific subject manner, there was a bit of genius in the writing. while the reader is inside the head of the main character, who, to put it nicely, is a vile man, the reader both loathes and somehow can feel some pity for him, once all of his sins catch up with him. while reading this, you know everything he has done is reprehensible but, because you are reading it from his perspective, you almost feel sorry for him when he gets what he pretty much deserves. getting the reader to feel this way is pretty remarkable. the author was able to keep this balance because he allowed us inside ram's daughter's head as well (and allowing us to get out of ram's head made it a bit easier to read). it is interesting to read the political and cultural piece to this as well. sadly, it was interesting in a psychological aspect because it shows the reader why some families stay together, despite abuse this despicable and the result it can have on keeping the victim a victim and how that plays out with the next generation. the end tied it all together as well. it was a difficult book to read and phantom. if it weren't so well written, i am not sure if i could have finished. it is not for the weak of heart.$this is not an easy book to review;nor is it easy to read. the main character, an overweight alcoholic, political crook and child molester, tells most of the story from his point of view. although he is mostly a vile man, there are some times you forget yourself and feel some sympathy towards him.he molests his oldest daughter, anita, when she was 12. twenty years later, anita is a widow with a young daughter of her own. she is forced to take her daughter and move in with her father, who she has grown to hate deeply.  she is increasingly paranoid that he may attempt to molest her daughter. amidst this story are stories of political corruption and intrigue that her father is involved in. i enjoy indian fiction, and although this novel is a little crazy at times, i love sharma's writing. his characters are so well drawn that i can practically picture them.$the write-up on the back of the edition that i read describes sharma's protagonist as a bit of a dostoevskyian anti-hero. this makes sense: sharma gives us a corrupt, alcoholic, child-molesting bureaucrat as the vehicle through which most of the story is told. and-call me old fashioned-this makes the story just that much harder to get through; any time you have a protagonist so wretched, so miserable, so abhorrent that you are viscerally—even physically—angered by them. well, good luck finishing; you are unlikely to enjoy the story."#
    #text="this is a well done fantasy book with some nice little life lessons. this is just the start and introduction to this world. the story will appeal to younger children, probably in the 1st to 3rd grade age range. it's a great book for children who are ready to move on to chapter books, but not quite ready for middle grade level reads."
    

    splitter = Splitter()
    postagger = POSTagger()
    dicttagger = DictionaryTagger([ 'dicts/positive1.yml', 'dicts/negative1.yml', 
                                    'dicts/inc.yml', 'dicts/dec.yml', 'dicts/inv.yml'])

    splitted_sentences = splitter.split(text)
    pprint(splitted_sentences)

    pos_tagged_sentences = postagger.pos_tag(splitted_sentences)
    pprint(pos_tagged_sentences)

    dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)
    pprint(dict_tagged_sentences)

    print("analyzing sentiment...")
    score = sentiment_score(dict_tagged_sentences)
    print(score)


