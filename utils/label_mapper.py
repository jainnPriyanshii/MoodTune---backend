NLP_TO_FACE = {
    "joy": "happy",
    "sadness": "sad",
    "anger": "angry",
    "fear": "fear",
    "surprise": "surprise",
    "disgust": "disgust",
    "neutral": "neutral"
}

def normalize_nlp(emotions):
    return {
        NLP_TO_FACE[label]: score
        for label, score in emotions.items()
        if label in NLP_TO_FACE
    }