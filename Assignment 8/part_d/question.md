# Question

Implement a MapReduce program that computes the inverted index for the given input, i.e.
for every word in the input it should output a list of (byte) offsets. The offset should
be the byte offset of the row that contains the word. However, typical stop words should
not be part of the index. Stop words are frequently occurring words like `and` that do
not have a substantial relevance. You can find a list of typical English stop words in
the given file(`big.txt`)
