from flask import Flask, request, jsonify, render_template,session



print("================================================")
print("================================================")
print("================== Client Server ===============")
print("================================================")
print("================================================")


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("sessions.html")



if __name__ == '__main__':
    app.run(debug= True )

