from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__) 
CORS(app)  # Allow frontend to communicate with backend

# Configure Gemini AI API key
genai.configure(api_key="AIzaSyBB509aq-gH3is4zQ2i-8-GQRgvCJsKJTY")

def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    response = get_gemini_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
