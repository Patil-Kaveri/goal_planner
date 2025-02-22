from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Storage for goals
goals = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        goal = request.form['goal']
        goals.append({"text": goal, "completed": False})
        return redirect(url_for('home'))
    return render_template('index.html', goals=goals)

@app.route('/delete/<int:goal_index>')
def delete_goal(goal_index):
    if 0 <= goal_index < len(goals):
        del goals[goal_index]
    return redirect(url_for('home'))

@app.route('/edit/<int:goal_index>', methods=['GET', 'POST'])
def edit_goal(goal_index):
    if request.method == 'POST':
        new_goal = request.form['goal']
        goals[goal_index]["text"] = new_goal
        return redirect(url_for('home'))
    return render_template('edit.html', goal=goals[goal_index]["text"], index=goal_index)

@app.route('/complete/<int:goal_index>')
def complete_goal(goal_index):
    if 0 <= goal_index < len(goals):
        goals[goal_index]["completed"] = True
    return redirect(url_for('home'))

@app.route('/completed')
def completed_goals():
    completed = [goal["text"] for goal in goals if goal["completed"]]
    return render_template('completed.html', completed_goals=completed)

@app.route('/clear')
def clear_goals():
    goals.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
