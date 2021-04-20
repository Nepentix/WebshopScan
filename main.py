from flask import Flask, render_template, request, redirect
# import requests

app = Flask(__name__, template_folder="static")

@app.route("/",  methods=["GET","POST"])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        form_data = request.form
        site = form_data["url"]
        site = site.replace("http://","").replace("https://","").replace("www.","")
        return redirect(f"/result/{site}", code=302)

@app.route("/result/")
def result():
    return redirect("/", code=302)

@app.route("/result/<site>")
def scanning(site):
    return f"Result for {site}"

## This will run the file locally when executed directly.
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
