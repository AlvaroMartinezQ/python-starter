text = """Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy
emphasizes code readability with its notable use of significant indentation. Its language constructs and
object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[30]
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (
particularly, procedural), object-oriented and functional programming. Python is often described as a "baatteries
included" language due to its comprehensive standard library.[31] Guido van Rossum began working on Python in the
late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.[32] Python
2.0 was released in 2000 and introduced new features, such as list comprehensions and a garbage collection system
using reference counting and was discontinued with version 2.7.18 in 2020.[33] Python 3.0 was released in 2008 and
was a major revision of the language that is not completely backward-compatible and much Python 2 code does not run
unmodified on Python 3. Python consistently ranks as one of the most popular programming languages """

stop_words = frozenset(
   ["a", "about", "after", "all", "also", "always", "am", "an", "and", "any", "are", "at", "be", "been", "being",
    "but", "by", "came", "can", "cant", "come", "could", "did", "didnt", "do", "does", "doesnt", "doing", "dont",
    "else", "for", "from", "get", "give", "goes", "going", "had", "happen", "has", "have", "having", "how", "i", "if",
    "ill", "im", "in", "into", "is", "isnt", "it", "its", "ive", "just", "keep", "let", "like", "made", "make", "many",
    "may", "me", "mean", "more", "most", "much", "no", "not", "now", "of", "only", "or", "our", "really", "say", "see",
    "some", "something", "take", "tell", "than", "that", "the", "their", "them", "then", "there", "they", "thing",
    "this", "to", "try", "up", "us", "use", "used", "uses", "very", "want", "was", "way", "we", "what", "when",
    "where", "which", "who", "why", "will", "with", "without", "wont", "you", "your", "youre"])

characters = ",.;-()"
traslations = "      "
traslation_table = text.maketrans(characters, traslations)
filtered_text = text.translate(traslation_table)

all_words = filtered_text.split()
different_words = {word for word in all_words if word not in stop_words}

# print(f"Found {len(different_words)} different words: ")
# print("\n".join(different_words))

ocurrences = dict()
sw_freq = dict()

for word in all_words:
    if word not in stop_words:
        ocurrences[word] = ocurrences.get(word, 0) + 1
    else:
        sw_freq[word] = sw_freq.get(word, 0) + (1./len(all_words))

print(ocurrences)
print(sw_freq)
