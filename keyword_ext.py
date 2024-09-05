import spacy

def ext_noun(text):
    # Load spaCy model
    nlp = spacy.load("en_core_web_sm")

    # Process the text
    doc = nlp(text)

    # Keywords to prioritize (these can be adjusted based on your needs)
    priority_keywords = {"field", "button", "input", "link"}

    # List to store noun phrases with their priorities
    noun_phrases = []

    # Extract noun phrases without determiners
    for chunk in doc.noun_chunks:
        filtered_tokens = [token.text for token in chunk if token.pos_ != "DET"]
        noun_phrase = " ".join(filtered_tokens)
        
        # Calculate priority based on keyword presence
        priority = sum(1 for token in chunk if token.text.lower() in priority_keywords)
        
        noun_phrases.append((noun_phrase, priority))

    # Sort noun phrases by priority (higher priority first)
    noun_phrases.sort(key=lambda x: x[1], reverse=True)

    # Return the highest priority noun phrase, or the first one if priorities are equal
    return noun_phrases[0][0] if noun_phrases else None

# Test the function
# print(ext_noun('5.  Click on Register button'))
