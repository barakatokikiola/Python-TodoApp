from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

# Index route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        if task_content:
            tasks.append(task_content)  # Add new task
        return redirect(url_for('index'))
    return render_template('index.html', tasks=tasks)

# Delete task route
@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

# Edit task route
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    if 0 <= task_id < len(tasks):
        if request.method == 'POST':
            new_content = request.form['content']
            tasks[task_id] = new_content
            return redirect(url_for('index'))
        return render_template('edit.html', task=tasks[task_id], task_id=task_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
