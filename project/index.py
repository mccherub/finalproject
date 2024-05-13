from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class PayCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Pay Calculator")
        master.configure(bg='grey')  # Set background color to grey

        self.label_name = tk.Label(master, text="Name:", bg='grey', fg='white')
        self.label_name.grid(row=0, column=0)

        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1)

        self.label_grosspay = tk.Label(master, text="Gross Pay:", bg='grey', fg='white')
        self.label_grosspay.grid(row=1, column=0)

        self.entry_grosspay = tk.Entry(master)
        self.entry_grosspay.grid(row=1, column=1)

        self.tithe_var = tk.BooleanVar()
        self.tithe_var.set(False) # By default, tithe is not deducted

        self.tithe_checkbox = tk.Checkbutton(master, text="Deduct Tithe", variable=self.tithe_var, bg='grey', fg='white')
        self.tithe_checkbox.grid(row=2, columnspan=2)

        self.label_damaged_property = tk.Label(master, text="Damaged Property Deduction:", bg='grey', fg='white')
        self.label_damaged_property.grid(row=3, column=0)

        self.entry_damaged_property = tk.Entry(master)
        self.entry_damaged_property.grid(row=3, column=1)

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate, bg='brown', fg='white')
        self.calculate_button.grid(row=4, columnspan=2)

        self.delete_button = tk.Button(master, text="Delete", command=self.delete_item, bg='violet', fg='white')
        self.delete_button.grid(row=6, columnspan=2)

        # Create TreeView
        self.tree = ttk.Treeview(master, columns=('Net Pay', 'Total Tax', 'URA Tax', 'Tithe', 'Damaged Property Deduction'))
        self.tree.grid(row=5, columnspan=2)
        self.tree.heading('#0', text='Name')
        self.tree.heading('Net Pay', text='Net Pay')
        self.tree.heading('Total Tax', text='Total Tax')
        self.tree.heading('URA Tax', text='URA Tax')
        self.tree.heading('Tithe', text='Tithe')
        self.tree.heading('Damaged Property Deduction', text='Damaged Property Deduction')

    def calculate(self):
        name = self.entry_name.get()
        try:
            gross_pay = float(self.entry_grosspay.get())
            ura_tax = gross_pay * 0.05
            tithe = gross_pay * 0.1 if self.tithe_var.get() else 0
            damaged_property_deduction = float(self.entry_damaged_property.get()) if self.entry_damaged_property.get() else 0
            total_tax = ura_tax + tithe + damaged_property_deduction
            net_pay = gross_pay - total_tax

            self.tree.insert('', 'end', text=name, values=(f"Ugx {net_pay:.2f}", f"Ugx {total_tax:.2f}", f"Ugx {ura_tax:.2f}", f"Ugx {tithe:.2f}", f"Ugx {damaged_property_deduction:.2f}"))

        except ValueError:
            messagebox.showerror("Error", "Please enter valid gross pay or damaged property deduction.")

    def delete_item(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)

def main():
    root = tk.Tk()
    app = PayCalculator(root)
    root.resizable(1,1)
    root.mainloop()

if __name__ == "__main__":
    main()