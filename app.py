from flask import Flask,request,render_template,redirect

from controller.person_controller import PersonController

app = Flask(__name__,template_folder="view", static_folder="view/assets")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/person", methods=["GET","POST", "PUT", "DELETE"])
def person():
    if request.method == "GET":
        return render_template("person.html",person_list = PersonController.find_all())

    elif request.method == "POST":
        name = request.form.get("name")
        family = request.form.get("family")
        status, message = PersonController.save(name,family)
        return render_template("person.html",person_list = PersonController.find_all())








app.run(host="192.168.39.100", port=80, debug=True)
