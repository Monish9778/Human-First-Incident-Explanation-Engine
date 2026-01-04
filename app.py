from flask import Flask, render_template, request

app = Flask(__name__)


def explain_error(error_message: str) -> dict:
    """
    Takes an error message as input
    Returns a human-friendly explanation
    """
    error = error_message.lower()

    if "timeout" in error:
        return {
            "type": "Network Error",
            "what": "The system could not connect within the expected time.",
            "why": "The server may be slow, down, or unreachable.",
            "fix": "Check the server status or your network connection."
        }

    if "access denied" in error or "permission denied" in error:
        return {
            "type": "Authentication Error",
            "what": "The system rejected the login attempt.",
            "why": "Incorrect username/password or insufficient permissions.",
            "fix": "Verify credentials and access rights."
        }

    if "not found" in error:
        return {
            "type": "Resource Not Found",
            "what": "The requested file or resource could not be located.",
            "why": "The path or resource name is incorrect.",
            "fix": "Check the file path or resource identifier."
        }

    return {
        "type": "Unknown Error",
        "what": "The system encountered an unknown issue.",
        "why": "The error does not match known patterns.",
        "fix": "Review logs or contact technical support."
    }


@app.route("/", methods=["GET", "POST"])
def index():
    explanation = None

    if request.method == "POST":
        error_message = request.form.get("error_message")
        explanation = explain_error(error_message)

    return render_template("index.html", explanation=explanation)


if __name__ == "__main__":
    app.run(debug=True)
