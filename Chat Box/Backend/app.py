from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", ""); # "" is the default value that will be returned if the key you are looking for doesn't exist.
        print("=============", user_message)
        response = client.models._generate_content(
            model ="gemini-2.5-flash",
            contents = user_message
        )
        print("RAW RESPONSE: ", response)
        print("TEXT RESPONSE: ", response.text)
        return jsonify({"reply": response.text})

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    

if __name__ == "__main__":
    app.run(debug=True)