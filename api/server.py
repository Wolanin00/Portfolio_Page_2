from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cv")
def open_cv_page():
    return send_file(path_or_file='static/file/Szewczyk_Mateusz_CV.pdf', as_attachment=False)


@app.route("/download_cv")
def download_cv():
    return send_file(path_or_file='static/file/Szewczyk_Mateusz_CV.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
