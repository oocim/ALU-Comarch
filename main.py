import tkinter as tk
from tkinter import ttk

class ALU:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def bitwise_and(self, a, b): return a & b
    def bitwise_or(self, a, b): return a | b
    def bitwise_not(self, a): return ~a
    def bitwise_xor(self, a, b): return a ^ b
    def bitwise_xnor(self, a, b): return ~(a ^ b) & 0xFFFFFFFF
    def bitwise_nand(self, a, b): return ~(a & b) & 0xFFFFFFFF

class ALUSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Modern ALU Simulator with Gate Visualization")
        self.geometry("800x500")
        self.resizable(False, False)

        self.alu = ALU()

        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.configure("TLabel", font=("Segoe UI", 11))
        self.style.configure("Bold.TLabel", font=("Segoe UI", 11, "bold"))
        self.style.configure("Header.TLabel", font=("Segoe UI", 14, "bold"))

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self, padding=20)
        main_frame.pack(fill="both", expand=True)

        # Left side - Input and Operation Controls
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side="left", fill="y")

        ttk.Label(left_frame, text="ALU Simulator", style="Header.TLabel").pack(pady=(0, 10))

        ttk.Label(left_frame, text="Operand A:", style="Bold.TLabel").pack(anchor="w")
        self.entry_a = ttk.Entry(left_frame)
        self.entry_a.pack(fill="x", pady=5)
        self.entry_a.bind("<KeyRelease>", lambda e: self.auto_calculate())

        self.label_b = ttk.Label(left_frame, text="Operand B (ignored for NOT):", style="Bold.TLabel")
        self.label_b.pack(anchor="w")
        self.entry_b = ttk.Entry(left_frame)
        self.entry_b.pack(fill="x", pady=5)
        self.entry_b.bind("<KeyRelease>", lambda e: self.auto_calculate())

        ttk.Label(left_frame, text="Operation:", style="Bold.TLabel").pack(anchor="w", pady=(10, 0))
        self.operation = ttk.Combobox(left_frame, values=[
            "ADD", "SUBTRACT", "AND", "OR", "XOR", "XNOR", "NAND", "NOT"
        ], state="readonly")
        self.operation.pack(fill="x", pady=5)
        self.operation.bind("<<ComboboxSelected>>", self.on_operation_change)

        ttk.Label(left_frame, text="Results", style="Header.TLabel").pack(pady=(15, 5))
        self.result_label = ttk.Label(left_frame, text="Result: ", style="Bold.TLabel")
        self.result_label.pack(anchor="w")
        self.binary_label = ttk.Label(left_frame, text="Binary: ")
        self.binary_label.pack(anchor="w")
        self.hex_label = ttk.Label(left_frame, text="Hex: ")
        self.hex_label.pack(anchor="w")

        # Right side - Gate Animation & Truth Table
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side="right", fill="both", expand=True)

        ttk.Label(right_frame, text="Gate Animation", style="Header.TLabel").pack(pady=(15, 5))
        self.canvas = tk.Canvas(right_frame, width=300, height=150, bg="white", highlightbackground="gray")
        self.canvas.pack(pady=5)

        ttk.Label(right_frame, text="Live Truth Table", style="Header.TLabel").pack(pady=(15, 5))
        self.truth_table_text = tk.Text(right_frame, height=8, width=40, font=("Courier New", 11), bd=1, relief="solid")
        self.truth_table_text.pack()
        self.truth_table_text.config(state="disabled")

        self.update_truth_table()
        self.auto_calculate()

    def on_operation_change(self, event=None):
        op = self.operation.get()
        if op == "NOT":
            self.entry_b.state(["disabled"])
            self.label_b.config(text="Operand B (disabled for NOT):")
        else:
            self.entry_b.state(["!disabled"])
            self.label_b.config(text="Operand B:")
        self.update_truth_table()
        self.auto_calculate()

    def auto_calculate(self):
        if self.operation.get():
            self.calculate()

    def calculate(self):
        op = self.operation.get()
        try:
            a = int(self.entry_a.get()) if self.entry_a.get() else 0
            b = int(self.entry_b.get()) if self.entry_b.get() and op != "NOT" else 0

            if op == "ADD":
                result = self.alu.add(a, b)
            elif op == "SUBTRACT":
                result = self.alu.subtract(a, b)
            elif op == "AND":
                result = self.alu.bitwise_and(a, b)
            elif op == "OR":
                result = self.alu.bitwise_or(a, b)
            elif op == "XOR":
                result = self.alu.bitwise_xor(a, b)
            elif op == "XNOR":
                result = self.alu.bitwise_xnor(a, b)
            elif op == "NAND":
                result = self.alu.bitwise_nand(a, b)
            elif op == "NOT":
                result = self.alu.bitwise_not(a)
            else:
                raise ValueError("Invalid operation")

            self.result_label.config(text=f"Result: {result}")
            self.binary_label.config(text=f"Binary: {bin(result)}")
            self.hex_label.config(text=f"Hex: {hex(result)}")
            self.update_truth_table()
            self.draw_gate()

        except ValueError:
            self.result_label.config(text="Result: Invalid Input")
            self.binary_label.config(text="Binary: -")
            self.hex_label.config(text="Hex: -")

    def update_truth_table(self):
        op = self.operation.get()
        output = ""

        if op in ["AND", "OR", "XOR", "XNOR", "NAND"]:
            output += " A   B   OUT\n"
            output += "------------\n"
            for a in [0, 1]:
                for b in [0, 1]:
                    if op == "AND":
                        out = a & b
                    elif op == "OR":
                        out = a | b
                    elif op == "XOR":
                        out = a ^ b
                    elif op == "XNOR":
                        out = ~(a ^ b) & 1
                    elif op == "NAND":
                        out = ~(a & b) & 1
                    output += f" {a}   {b}    {out}\n"
        elif op == "NOT":
            output += " A   OUT\n"
            output += "--------\n"
            for a in [0, 1]:
                out = ~a & 1
                output += f" {a}    {out}\n"
        else:
            output = "Select a logic operation."

        self.truth_table_text.config(state="normal")
        self.truth_table_text.delete("1.0", tk.END)
        self.truth_table_text.insert(tk.END, output)
        self.truth_table_text.config(state="disabled")

    def draw_gate(self):
        self.canvas.delete("all")
        op = self.operation.get()

        # draw inputs and outputs
        self.canvas.create_line(20, 50, 80, 50, width=2)  # Input A
        if op != "NOT":
            self.canvas.create_line(20, 100, 80, 100, width=2)  # Input B
        self.canvas.create_line(220, 75, 280, 75, width=2)  # Output

        # gate shape
        if op == "AND":
            self.canvas.create_rectangle(80, 40, 180, 110, outline="black", width=2)
            self.canvas.create_arc(130, 40, 230, 110, start=270, extent=180, style="arc", width=2)
            self.canvas.create_text(155, 75, text="AND", font=("Segoe UI", 10, "bold"))
        elif op == "OR":
            self.canvas.create_arc(60, 30, 200, 120, start=270, extent=180, style="arc", width=2)
            self.canvas.create_text(155, 75, text="OR", font=("Segoe UI", 10, "bold"))
        elif op == "XOR":
            self.canvas.create_arc(65, 30, 205, 120, start=270, extent=180, style="arc", width=2)
            self.canvas.create_arc(60, 30, 200, 120, start=270, extent=180, style="arc", width=2)
            self.canvas.create_text(155, 75, text="XOR", font=("Segoe UI", 10, "bold"))
        elif op == "XNOR":
            self.canvas.create_arc(65, 30, 205, 120, start=270, extent=180, style="arc", width=2)
            self.canvas.create_arc(60, 30, 200, 120, start=270, extent=180, style="arc", width=2)
            self.canvas.create_text(155, 75, text="XNOR", font=("Segoe UI", 10, "bold"))
        elif op == "NAND":
            self.canvas.create_rectangle(80, 40, 180, 110, outline="black", width=2)
            self.canvas.create_arc(130, 40, 230, 110, start=270, extent=180, style="arc", width=2)
            self.canvas.create_oval(180, 65, 195, 80, outline="black", fill="white", width=2)
            self.canvas.create_text(155, 75, text="NAND", font=("Segoe UI", 10, "bold"))
        elif op == "NOT":
            self.canvas.create_polygon(80, 40, 80, 110, 160, 75, fill="", outline="black", width=2)
            self.canvas.create_oval(160, 65, 170, 85, outline="black", fill="white", width=2)
            self.canvas.create_text(120, 75, text="NOT", font=("Segoe UI", 10, "bold"))
        elif op == "ADD":
            self.canvas.create_rectangle(80, 50, 180, 100, outline="black", width=2)
            self.canvas.create_text(130, 75, text="+", font=("Segoe UI", 16, "bold"))
        elif op == "SUBTRACT":
            self.canvas.create_rectangle(80, 50, 180, 100, outline="black", width=2)
            self.canvas.create_text(130, 75, text="-", font=("Segoe UI", 16, "bold"))

if __name__ == "__main__":
    app = ALUSimulator()
    app.mainloop()
