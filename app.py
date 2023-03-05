from flask import Flask,jsonify,request

app = Flask(__name__)

data = [
    {
    "id" : 1,
    "contact" : "99885835857",
    "name" : "Raju",
    "done" : False
    },
    {
    "id" : 2,
    "contact" : "9234235857",
    "name" : "rahul",
    "done" : False
    }
]

@app.route("/addData", methods = ["POST"])
def giveTasks():
    if not request.json:
        return jsonify({
            "status" : "Error",
            "message" : "Data Not Available"
        },400)
    contact = {
        "id":data[-1]["id"]+1,
        "name" : request.json["name"],
        "contact" : request.json.get("contact",""),
        "done" : False
        }
    data.append(contact)
    return jsonify({
        "status" : "success",
        "message" : "id added successfuly"
    })

if(__name__ == "__main__"):
    app.run(debug = True)