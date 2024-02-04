def reverse(sentence):
    words = sentence.split()
    rev_words = words[::-1]
    rev_sentence=' '.join(rev_words)
    return rev_sentence
sentence = input()
rev_sentence = reverse(sentence)
print (rev_sentence)
    