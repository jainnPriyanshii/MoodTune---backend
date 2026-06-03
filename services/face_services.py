from deepface import DeepFace

def analyze_face_emotion(image):
    result = DeepFace.analyze(
        image,
        actions=["emotion"],
        enforce_detection=False
    )

    emotions = result[0]["emotion"]
    dominant = result[0]["dominant_emotion"]

    return {
        "dominant": dominant,
        "emotions": emotions
    }