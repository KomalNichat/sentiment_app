from flask import Flask, render_template, request

app = Flask(__name__)
history = []

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    score = None
    color = None
    emoji = None

    if request.method == "POST":
        text = request.form["text"]

        if "good" in text.lower():
            result = "Positive"
            score = 0.8
            color = "green"
            emoji = "😊"

        elif "bad" in text.lower():
            result = "Negative"
            score = -0.6
            color = "red"
            emoji = "😡"

        else:
            result = "Neutral"
            score = 0.0
            color = "gray"
            emoji = "😐"

        history.insert(0, {
            "text": text,
            "result": result,
            "score": score,
            "color": color,
            "emoji": emoji
        })

    return render_template("index.html", result=result, score=score, history=history)


if __name__ == "__main__":
    app.run(debug=True)
