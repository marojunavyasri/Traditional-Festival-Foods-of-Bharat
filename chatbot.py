import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyBB509aq-gH3is4zQ2i-8-GQRgvCJsKJTY")

def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Run chatbot in terminal
if __name__ == "__main__":
        print("Chatbot is running! Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot stopped.")
            break
        print("Bot:", get_gemini_response(user_input))
