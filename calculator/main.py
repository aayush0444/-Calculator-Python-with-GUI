import tkinter as tk

# Calculator class using Tkinter
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("Smart Calculator")
        self.geometry("400x550")
        self.configure(bg="#222222")
        self.resizable(False, False)

        self.equation = ""

        # Input display setup
        self.display = tk.Entry(self, font=("Arial", 24), bd=0, bg="#1e1e1e",
                                fg="white", justify="right", relief="ridge")
        self.display.insert(0, "0")
        self.display.pack(padx=20, pady=20, ipady=15, fill="both")

        # Button layout function
        self.create_buttons()

        # Bind keyboard keys
        self.bind("<Key>", self.key_input)

    # Handle keyboard input
    def key_input(self, event):
        if event.char.isdigit() or event.char in "+-*/().":
            self.append_to_equation(event.char)
        elif event.keysym == "Return":
            self.calculate()
        elif event.keysym == "BackSpace":
            self.delete()
        elif event.char.lower() == 'c':
            self.clear()

    # Layout buttons row-wise
    def create_buttons(self):
        buttons = [
            ["C", "DEL", "(", ")"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "+/-", "+"],
            ["="]
        ]

        for row in buttons:
            row_frame = tk.Frame(self, bg="#222222")
            row_frame.pack(padx=10, pady=4, fill="both", expand=True)

            for btn_text in row:
                btn = tk.Button(row_frame, text=btn_text, font=("Arial", 20),
                                width=5, height=2, bg="#333333", fg="white",
                                activebackground="#555555",
                                command=lambda b=btn_text: self.handle_button(b))
                btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

    # What to do when a button is clicked
    def handle_button(self, btn):
        if btn == "=":
            self.calculate()
        elif btn == "C":
            self.clear()
        elif btn == "DEL":
            self.delete()
        elif btn == "+/-":
            self.toggle_sign()
        else:
            self.append_to_equation(btn)

    def append_to_equation(self, val):
        if self.display.get() == "0" or self.display.get() == "Error":
            self.display.delete(0, tk.END)
        self.display.insert(tk.END, val)

    def clear(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, "0")

    def delete(self):
        current = self.display.get()
        if len(current) > 1:
            self.display.delete(0, tk.END)
            self.display.insert(0, current[:-1])
        else:
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")

    def toggle_sign(self):
        try:
            current = self.display.get()
            if current.startswith("-"):
                self.display.delete(0)
            else:
                self.display.insert(0, "-")
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")

    def calculate(self):
        try:
            expression = self.display.get()
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

# Run the calculator
if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
