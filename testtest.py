import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_md")

def check_similarity(text1, text2):
    # Process the texts with spaCy
    doc1 = nlp(text1)
    doc2 = nlp(text2)

    # Calculate the similarity
    similarity = doc1.similarity(doc2)

    return similarity

# Example texts
text1 = "the Last Name field"
text2 = 'Last Name lastName   text '

# Check similarity
similarity_score = check_similarity(text1, text2)

print(f"Similarity Score: {similarity_score:.4f}")
