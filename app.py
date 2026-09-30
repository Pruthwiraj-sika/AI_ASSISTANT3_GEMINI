from flask import Flask,render_template,jsonify,url_for,redirect,request

import os
from dotenv import load_dotenv
from google import genai

app = Flask(__name__)
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API Key nahi mili! Apni .env file check kar.")
client = genai.Client(api_key=api_key)

@app.route("/")
def home():
    return render_template("text.html")
@app.route("/chat",methods=["POST"])
def chat():
    user_message = request.form.get("prompt")

    try:
        response = client.models.generate_content(
            model = "gemini-3.6-flash",
            contents = user_message
        )
        return jsonify({"reply":response.text})

    except Exception as e:
        return jsonify({"reply": f"Error aa gaya he {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)