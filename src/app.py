from flask import Flask, render_template, request, redirect, url_for
from syntax_checker import check_syntax
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def upload_page():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]

    if file.filename == "":
        return "No selected file"

    if not file.filename.endswith(".py"):
        return "Invalid file type. Please upload a .py file."

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
        
    syntax_result = check_syntax(code)

    if syntax_result["error"]:
        error_message = f"{syntax_result['error_type']} at line {syntax_result['line']}: {syntax_result['msg']}"
    else:
        error_message = "None"

    return render_template(
        "analysis_result.html",
        lines=len(code.splitlines()),
        functions=0,
        classes=0,
        imports=0,
        error=error_message
    )

@app.route("/results")
def results_page():
    return render_template(
        "results.html",
        lines=42,
        functions=3,
        classes=1,
        imports=2,
        error="None"
    )

if __name__ == "__main__":
    app.run(debug=True)
