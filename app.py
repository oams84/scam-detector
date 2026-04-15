import json
import os
from flask import Flask, render_template, request, jsonify, redirect, url_for
from detector import analyze_message

app = Flask(__name__)

HISTORY_FILE = "data/history.json"


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)


def save_to_history(entry):
    history = load_history()
    history.append(entry)
    save_history(history)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    message = ""

    if request.method == "POST":
        message = request.form.get("message", "")
        result = analyze_message(message)

        entry = {
            "message": message,
            "verdict": result["verdict"],
            "risk_score": result["risk_score"],
            "reasons": result["reasons"]
        }
        save_to_history(entry)

    return render_template("index.html", result=result, message=message)


@app.route("/api/analyze", methods=["POST"])
def api_analyze():
    data = request.get_json(silent=True)

    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message' in JSON body."}), 400

    message = data["message"]
    result = analyze_message(message)

    entry = {
        "message": message,
        "verdict": result["verdict"],
        "risk_score": result["risk_score"],
        "reasons": result["reasons"]
    }
    save_to_history(entry)

    return jsonify(entry)


@app.route("/history", methods=["GET"])
def history():
    return render_template("history.html", history=load_history())


@app.route("/clear-history", methods=["POST"])
def clear_history():
    save_history([])
    return redirect(url_for("history"))


@app.route("/api/history", methods=["GET"])
def api_history():
    return jsonify(load_history())


if __name__ == "__main__":
    app.run(debug=True)
