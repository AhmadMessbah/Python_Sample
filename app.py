from flask import Flask,request,render_template,redirect,jsonify

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

    elif request.method == "DELETE":
        id = int(request.args.get("id"))
        PersonController.remove(id)
        return render_template("person.html",person_list = PersonController.find_all())


@app.route("/api")
def api():
    return f"{jsonify(PersonController.find_all()[1])}"


app.run(host="192.168.39.100", port=80, debug=True)
