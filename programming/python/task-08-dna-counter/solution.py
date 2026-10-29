#варіант2

import tkinter as tk
from tkinter import scrolledtext


class A(tk.Tk): 
    def __init__(self):
        super().__init__()
        
        self.title("Counter")
        self.text = scrolledtext.ScrolledText(self, width=50, height=10, font=("Courier", 12))
        self.text.pack(padx=30, pady=10)

        button_space = tk.Frame(self)
        button_space.pack(pady=5)

        self.count = tk.Button(button_space, text="Count", width=10, command=self.count_letters)
        self.count.pack(side=tk.LEFT, padx=5)

        self.clear = tk.Button(button_space, text="Clear", width=10, command=self.clear_text)
        self.clear.pack(side=tk.LEFT, padx=5)

        self.goodbye = tk.Button(button_space, text="Goodbye", width=10, command=self.destroy)
        self.goodbye.pack(side=tk.LEFT, padx=5)

        self.result_label = tk.Label(self, text="", font=("Courier", 12))
        self.result_label.pack(pady=5)


    def count_letters(self):
        text = self.text.get("1.0", tk.END).upper()
        a_count = text.count("A")
        t_count = text.count("T")
        c_count = text.count("C")
        g_count = text.count("G")
        self.result_label.config(
            text=f"Num As: {a_count}  Num Ts: {t_count}  "
                 f"Num Cs: {c_count}  Num Gs: {g_count}"
        )

    def clear_text(self):
        self.text.delete("1.0", tk.END)
        self.result_label.config(text="")


if __name__ == "__main__":
    app = A()
    app.mainloop()

