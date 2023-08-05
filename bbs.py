from flask import Flask, request, render_template
from namechanger import changer
import codecs
app = Flask(__name__)

@app.route("/")
def bbs():
    message = "Hello world"
    file = codecs.open("articles.txt", "r", "utf-8")
    lines = file.readlines()
    file.close()
    return render_template("bbs.html", message = message, lines = lines)

@app.route("/result", methods=["POST"])
def result():
    message = "This is paiza"
    article = request.form["article"]
    name = request.form["name"]

    name = changer(name)

    file = codecs.open("articles.txt", "a", "utf-8")
    file.write(article + "," + name + "\n")
    file.close()

    return render_template("bbs_result.html", message = message, article = article, name = name)


if __name__ == '__main__':
    app.debug = True  #デバッグモードTrueにすると変更が即反映される
    app.run()
