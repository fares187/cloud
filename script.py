import nltk

nltk.download('punkt')
nltk.download('stopwords')

stop_words = nltk.corpus.stopwords.words('english')

with open("random_paragraphs.txt", "r") as file:
    text = file.read()

text = text.lower()
text = ''.join([char for char in text if char.isalnum() or char.isspace()])
tokens = nltk.word_tokenize(text)

filtered_words = [word for word in tokens if word not in stop_words]

word_counts = nltk.FreqDist(filtered_words)

print("Word Frequency Count:")
for word, count in word_counts.items():
    print(f"{word}: {count}")