import spacy

def ext_noun(text):
    # Load spaCy model
    nlp = spacy.load("en_core_web_sm")

    # Sample text
    text = text
    # Process the text
    doc = nlp(text)

    # Extract noun phrases
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    return noun_phrases[0]

# print(ext_noun('Verify the first name field is editable'))