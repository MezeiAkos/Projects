import tkinter as tk

window = tk.Tk()
window.title("Change return")


def do_shit():
    n = float(number.get())
    two_hundreds = int(n / 200)
    n -= (two_hundreds * 200)
    tk.Label(text="200: " + str(two_hundreds)).pack()

    one_hundreds = int(n / 100)
    n -= one_hundreds * 100
    tk.Label(text="100: " + str(one_hundreds)).pack()

    fifties = int(n / 50)
    n -= fifties * 50
    tk.Label(text="50: " + str(fifties)).pack()

    twenties = int(n / 20)
    n -= twenties * 20
    tk.Label(text="20: " + str(twenties)).pack()

    tens = int(n / 10)
    n -= tens * 10
    tk.Label(text="10: " + str(tens)).pack()

    fives = int(n / 5)
    n -= fives * 5
    tk.Label(text="5: " + str(fives)).pack()

    ones = int(n)
    n -= int(n)
    tk.Label(text="1: " + str(ones)).pack()

    fiftybani = int(n / 0.5)
    n -= fiftybani * 0.5
    tk.Label(text="0.50: " + str(fiftybani)).pack()

    tenbani = int(n / 0.1)
    n -= tenbani * 0.1
    tk.Label(text="0.10: " + str(tenbani)).pack()

    fivebani = int(n / 0.05)
    n -= fivebani * 0.05
    tk.Label(text="0.05: " + str(fivebani)).pack()

    onebani = int(n / 0.01)
    tk.Label(text="0.01: " + str(onebani)).pack()


greeting = tk.Label(text="Enter amount: ")
greeting.pack()

number = tk.Entry(width=35)
number.pack()
button = tk.Button(text="Calculate change", command=do_shit)
button.pack()
window.mainloop()
