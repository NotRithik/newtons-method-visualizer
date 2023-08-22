import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
import sympy as sp

# Create the main application window
root = tk.Tk()
root.title("Function Grapher")

def evaluate_expression(expr, x):
    return eval(expr.replace("^", "**").replace("x", "(" + str(x) + ")"))

def diff_expression(expr):
    expression_sym = sp.sympify(expr.replace("^", "**"))
    return str(sp.diff(expression_sym, sp.Symbol("x")))

# Function to update the graph
def plot_graph(steps=0):
    step_count.set(steps)
    x = np.arange(-10, 10.1, 0.1)
    y = [evaluate_expression(function_input_entry.get(), val) for val in x]

    ax.clear()
    ax.plot(x, y, color="red")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Graph of y = ' + function_input_entry.get())
    canvas.draw()

# Function to perform the next step
def next_step():
    x = np.arange(-10, 10.1, 0.1)
    differential = diff_expression(function_input_entry.get())
    m = evaluate_expression(differential, float(guess_input_entry.get()))
    c = evaluate_expression(function_input_entry.get(), float(guess_input_entry.get())) - (m * float(guess_input_entry.get()))

    next_guess = float(guess_input_entry.get()) - (evaluate_expression(function_input_entry.get(), float(guess_input_entry.get())) / evaluate_expression(differential, float(guess_input_entry.get())))

    y = [(m * val) + c for val in x]

    plot_graph(steps = step_count.get() + 1)

    ax.plot(x, y, color="green")
    canvas.draw()

    error.set(abs(evaluate_expression(function_input_entry.get(), float(guess_input_entry.get()))))
    current_guess.set(guess_input_entry.get())

    guess_input_entry.delete(0, tk.END)
    guess_input_entry.insert(0, str(next_guess))

# Create a frame for the input section
input_frame = ttk.Frame(root, padding=10)
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Label and Entry widgets
function_input_label = ttk.Label(input_frame, text="Input function:")
function_input_label.grid(row=0, column=0, sticky="w")
function_input_entry = ttk.Entry(input_frame)
function_input_entry.grid(row=0, column=1, padx=(0, 10), sticky="ew")

# Graph Button
graph_button = ttk.Button(input_frame, text="Graph Function", command=plot_graph)
graph_button.grid(row=0, column=2, padx=10)

# Guesses
guess_input_label = ttk.Label(input_frame, text="Next Guess:")
guess_input_label.grid(row=0, column=3, sticky="w")
guess_input_entry = ttk.Entry(input_frame)
guess_input_entry.grid(row=0, column=4, padx=(0, 10), sticky="ew")

# Next Step Button
next_step_button = ttk.Button(input_frame, text="Next Step", command=next_step)
next_step_button.grid(row=0, column=5, padx=10)

steps_label = ttk.Label(input_frame, text="Steps Taken:")
steps_label.grid(row=1, column=0, sticky="w")
step_count = tk.IntVar()
step_count.set(0)
steps_counter = ttk.Label(input_frame, textvariable=step_count)
steps_counter.grid(row=1, column=1, padx=(0, 10), sticky="ew")

# Error indicator
error_label = ttk.Label(input_frame, text="Error:")
error_label.grid(row=1, column=3, sticky="w")
error = tk.IntVar()
error_indicator = ttk.Label(input_frame, textvariable=error)
error_indicator.grid(row=1, column=4, padx=(0, 10), sticky="ew")

# Current guess
current_guess_label = ttk.Label(input_frame, text="Current Guess:")
current_guess_label.grid(row=1, column=5, sticky="w")
current_guess = tk.IntVar()
current_guess_indicator = ttk.Label(input_frame, textvariable=current_guess)
current_guess_indicator.grid(row=1, column=6, padx=(0, 10), sticky="ew")

# Create a frame for the graph
graph_frame = ttk.Frame(root, padding=10)
graph_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

# Create a Matplotlib figure and axis
fig, ax = plt.subplots()
ax.plot([], [])  # Placeholder for initial plot
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Graph of y = 0')

# Create a Tkinter canvas for embedding the Matplotlib figure
canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.get_tk_widget().pack()

# Update the layout
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)

# Start the Tkinter event loop
root.mainloop()
