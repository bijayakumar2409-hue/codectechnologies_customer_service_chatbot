from flask import Flask, render_template, request

app = Flask(__name__)

# Simple chatbot responses
responses = {
    "hello": "Hello! Welcome to our customer service.",
    "hi": "Hi! How can I help you?",
    "price": "Please visit our pricing page for the latest plans.",
    "contact": "You can contact us at support@example.com.",
    "bye": "Thank you for visiting. Have a great day!"
}

@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""
    if request.method == "POST":
        user_message = request.form["message"].lower()
        reply = responses.get(user_message, "Sorry, I don't understand your question.")
    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
