from flask import Flask, jsonify, request
from face_services import analyze_face_emotion
from text_services import analyze_text_emotion
from fuse_moods_services import fuse_moods
from image_decoder import image_decoder

app = Flask(__name__)

@app.route('/')

def index():
    return "Hello , ALL good"


@app.route("/analyze-face",methods=['POST'])

def analyze_face():
    try:
        data = request.get_json()

        image_b64 = data.get("image")
        



        if not image_b64:
            return jsonify({
                "success": False,
                "error": "No image provided"
            }), 400
        image=image_decoder(image_b64)
        
    

        result = analyze_face_emotion(image)

        return jsonify({
            "success": True,
            "dominant": result["dominant"],
            "emotions": result["emotions"]
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/analyze-text", methods=["POST"])
def analyze_text():
    try:
        data = request.get_json()

        text = data["text"]

        if not text:
            return jsonify({
             "success": False,
            "error": "Text is required"
            }), 400

        result = analyze_text_emotion(text)

        return jsonify(result)
    
    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/get-mood",methods=["POST"])

def get_mood():
    try:
        data = request.get_json()
        image_b64 = data.get("image")
        image = image_decoder(image_b64)
        text = data.get("text", "")
        face_result = analyze_face_emotion(image)
        text_result = analyze_text_emotion(text)

        result = fuse_moods(face_result,text_result)

        return jsonify(result)


    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)