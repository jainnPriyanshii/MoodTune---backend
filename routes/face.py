import cv2 

from deepface import DeepFace

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        break
    try:
        results = DeepFace.analyze(frame,actions=['emotion'],enforce_detection=False)

        for face in results:

            x,y,w,h = face['region']['x'],face['region']['y'],face['region']['w'],face['region']['h']
            emotion = face['dominant_emotion']

            cv2.rectangle(frame,(x,y),(x+w,y+h),(250,0,0),2)

            cv2.putText(frame,emotion,(x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)


    except:
        cv2.putText(frame,'NO Face Detected',(50,50),
                        cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)


    cv2.imshow("face detection",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()