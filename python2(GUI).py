# calculator(GUI)

import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.entry = tk.Entry(root, width=40, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for text in button_texts:
            button = tk.Button(self.root, text=text, padx=20, pady=20, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        clear_button = tk.Button(self.root, text="Clear", padx=20, pady=20, command=self.clear)
        clear_button.grid(row=row_val, column=0, columnspan=2)

        quit_button = tk.Button(self.root, text="Quit", padx=20, pady=20, command=self.root.quit)
        quit_button.grid(row=row_val, column=2, columnspan=2)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.entry.delete(0, tk.END)
        else:
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current + char)

    def clear(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
