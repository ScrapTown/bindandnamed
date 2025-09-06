from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"

db = SQLAlchemy(app)

class ToDo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    task = db.Column(db.String(200),nullable=False)

with app.app_context():
    db.create_all()

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task").strip()
        if task:
            task = ToDo(task = task)
            db.session.add(task)
            db.session.commit()
        return redirect("/")
    tasks = ToDo.query.all()
    return render_template("index.html",tasks=tasks)

@app.route("/delete/<int:id>",methods=["POST"])
def delete(id):
    task = ToDo.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)