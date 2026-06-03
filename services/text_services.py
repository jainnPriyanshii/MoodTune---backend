from transformers import pipeline
from label_mapper import NLP_TO_FACE

classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def analyze_text_emotion(text):

    
    result = classifier(text)
        

    emotions_list = result[0] if isinstance(result[0], list) else result

    dominant = max(emotions_list, key=lambda x: x['score'])
    emotions = {
        emotion["label"]: round(emotion["score"], 4)
        for emotion in emotions_list
    }

    mapped_dominant =  NLP_TO_FACE[dominant["label"]]

    return {
        "dominant": mapped_dominant,
        "emotions": emotions
    }