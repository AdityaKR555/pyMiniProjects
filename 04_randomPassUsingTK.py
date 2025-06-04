import tkinter as tk
import random

# Function to generate password
def generate_password():
    try:
        length = int(entry.get())
        if length < 4 or length > 10:
            result_label.config(text="Length should be between 4 and 10")
            return
        
        options = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&"
        password = "".join(random.choice(options) for _ in range(length))
        result_label.config(text="Your Password is: " + password)

    except ValueError:
        result_label.config(text="Please enter a valid number")

# GUI setup
window = tk.Tk()
window.title("Password Generator")
window.geometry("350x200")

tk.Label(window, text="Enter password length (4–10):").pack(pady=10)
entry = tk.Entry(window)
entry.pack()

tk.Button(window, text="Generate Password", command=generate_password).pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()