# Newton's Method Visualizer

As the heading suggests, this is a python program that will take in a polynomial expression and an initial guess, use the Newton's method of approximation on it to solve for an approximate `x` in `f(x) = 0`, and show you the error from `y (=f(x))` to `0`.  

## User guide:

- Install python, then run
```shell
pip install sympy numpy matplotlib tkinter pandas
```
to ensure you have all the libraries required to run this code.  

- Then, navigate to the folder containing `NewtonsMethod.py` in your shell, and run `python NewtonsMethod.py`.  
- In the window that pops up, enter your equation in the form `7*x^3 - (2/3)*x^2 + 4`, hit the button to graph the plot.
- Then enter a number for an initial guess of `x` and hit "Next Guess".
- The next guess will be auto-updated and you can keep spamming "Next Guess" button until it stops changing.
- If the error just doesn't get close enough to zero even after a lot of tries, your polynomial probably doesn't have a zero.
- A polynomial (depending on its degree) can have multiple zeroes as well! You can keep trying with different initial guesses to see if it resolves to a different guess.

# Disclaimer
This is pretty bad code (lol) and I only wrote this to play around with tkinter (please don't use this to judge my coding capabilities lmao).