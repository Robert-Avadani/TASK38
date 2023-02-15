import spacy

# In the first example we are comparing all these 3 words with each other
# and print the similarity result based on that predetermined spacy language model.
# We notice the first two are more close to each other because they are animals
# and the fruit's similarity is the most lower than all of 3.
print(f"Comparing the words cat, monkey, banana.\n")
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# In this example we compare the words one by one and we notice
# the differences as there could be other similarities between
# specific words like monkeys and bananas since monkeys like
# bananas so they are associated with that
print("\nComparing the words cat, apple, monkey, banana in more detail.\n")
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# Here we are comparing whole sentences and depending on the context itself
# and which model we use the similarities will vary
print("\nComparing sentences:\n")
sentence_to_compare = "Why is my cat on the car"
print(f"Comparing the sentence \'{sentence_to_compare}\' to a list of other sentences.")
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


# After running the example file with both models we notice that the similarities vary
# and it's normal as the en_core_web_sm is a smaller model than the en_core_web_md and
# based on the information taken from the source the en_core_web_sm includes vocabulary,
# syntax, and named entity recognition, while en_core_web_md includes those plus word
# vectors and syntax-sensitive tensor-based sentence representation which in turn will
# provide us a different result based on which one is used.I believe the smaller one is
# mostly used to recognise the context of words in a specific sentence while the medium
# one should be used for more complex comparisons in general and more accuracy in general.