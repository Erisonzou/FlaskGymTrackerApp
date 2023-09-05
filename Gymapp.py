from flask import Flask, render_template, url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Gym.db'
db = SQLAlchemy(app)

class Todo(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    Workout = db.Column(db.String(200), nullable = False)
    Excercise = db.Column(db.String(200), nullable = False)
    completed = db.Column(db.Integer, default = 0)
    Weights = db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r' %self.id
    
@app.route('/',methods=['POST','GET'])

def index():
    if request.method == 'POST':

        new_excercise = request.form['Excercise']
        new_Workout = request.form['Workout']
        new_Weights = request.form['Weights']
        new_task = Todo(Workout = new_Workout, Excercise = new_excercise, Weights = new_Weights)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "there was an issue adding task"
        
    else:
        TodayWorkout = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html',tasks = TodayWorkout)


if __name__ == "__main__":
    app.run(debug=True)