
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
sentence = "Python is a great programming language"
embedding = model.encode(sentence)

print(embedding)  # → a vector of 384 dimensions
