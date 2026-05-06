from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)
test_sentences = [
    
    "i am really sad and missing someone",
   
]

for sentence in test_sentences:
    result = classifier(sentence)
    

emotions_list = result[0] if isinstance(result[0], list) else result




dominant = max(emotions_list, key=lambda x: x['score'])
print(f"\nDominant emotion: {dominant['label']}")