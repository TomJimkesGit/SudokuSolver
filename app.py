from flask import Flask, render_template, request
from sudoku_solver.src.brute_force_solver import BruteForceSolver

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_grid', methods=['POST'])
def submit_grid():

    lines = []
    for i in range(0,9):
        lines.append("")
        for j in range(0,9):
            sq = request.form[f"{i}-{j}"]
            sq = '0' if sq == "" else sq
            lines[i] += sq

    solver = BruteForceSolver()
    solver.read_from_lines(lines)
    if solver.solve():
        return render_template('solved_puzzle.html', puzzle=solver.get_puzzle())
    return render_template('index.html') 

@app.route('/submit_text', methods=['POST'])
def submit_text():
    puzzle_text = request.form['text_input']
    lines = puzzle_text.split('\r\n')
    solver = BruteForceSolver()
    solver.read_from_lines(lines)
    if solver.solve():
        return render_template('solved_puzzle.html', puzzle=solver.get_puzzle())
    return render_template('index.html') 