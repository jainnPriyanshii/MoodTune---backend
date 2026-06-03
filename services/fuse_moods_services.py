def fuse_moods(face_result,text_result):
    emotions = ['happy','sad', 'angry', 'fear', 'surprise', 'disgust', 'neutral']

    fused_score = {}

    for emotion in emotions :

        face_score = face_result["emotions"].get(emotion, 0)
        text_score = text_result["emotions"].get(emotion, 0)

        fused_score[emotion]=(face_score * 0.6) + (text_score * 0.4)

    dominant_emotion = max(fused_score, key= fused_score.get)


    return {
        "dominant":dominant_emotion,
        "emotions": fused_score
        
    }