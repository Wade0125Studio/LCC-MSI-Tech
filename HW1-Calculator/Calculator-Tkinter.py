import tkinter as tk
from tkinter import ttk
from math import sqrt, sin, cos, tan, radians, exp

def clear_placeholder_1(event):
    if entry1.get() == "輸入第一個數":
        entry1.delete(0, tk.END)

def clear_placeholder_2(event):
    if entry2.get() == "輸入第二個數":
        entry2.delete(0, tk.END)

def calculate():
    num1 = entry1.get()
    num2 = entry2.get()
    operator = operator_var.get()

    if not num1:
        result = "請輸入第一個數"
    elif not num2 and operator not in ("sqrt", "cbrt", "exp", "sin", "cos", "tan"):
        result = "請輸入第二個數"
    else:
        num1 = float(num1)
        if operator in ("sqrt", "cbrt", "exp", "sin", "cos", "tan"):
            num2 = 0
        else:
            num2 = float(num2)
        if operator == "":
            result = "請選擇操作符"
        elif operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                result = "除數不能為零"
            else:
                result = num1 / num2
        elif operator == "**":
            result = num1 ** num2
        elif operator == "sqrt":
            result = sqrt(num1)
        elif operator == "cbrt":
            result = num1 ** (1/3)
        elif operator == "%":
            if num2 == 0:
                result = "除數不能為零"
            else:
                result = num1 % num2
        elif operator == "exp":
            result = exp(num1)
        elif operator == "sin":
            result = sin(radians(num1))
        elif operator == "cos":
            result = cos(radians(num1))
        elif operator == "tan":
            result = tan(radians(num1))
        else:
            result = "無效的操作符"

    result_label.config(text=f"結果: {result}")

def set_language():
    selected_language = language_var.get()
    if selected_language == "中文":
        title_label.config(text="Python科學計算機")
        title_hint.config(text="**若要計算根號,立方根,自然對數,正弦,餘弦,正切只需要再輸入在第一個數字的輸入欄**")
        entry1.delete(0, tk.END)
        entry1.insert(0, "輸入第一個數")
        entry2.delete(0, tk.END)
        entry2.insert(0, "輸入第二個數")
        operator_dropdown.set("請選擇運算方式")
        calculate_button.config(text="計算")
        result_label.config(text="計算結果: ")
    elif selected_language == "English":
        title_label.config(text="Python Scientific Calculator")
        title_hint.config(text="**To calculate square root, cube root, natural log, sine, cosine, tangent,\n only enter a value in the first input box**")
        entry1.delete(0, tk.END)
        entry1.insert(0, "Enter first number")
        entry2.delete(0, tk.END)
        entry2.insert(0, "Enter second number")
        operator_dropdown.set("Please select an operator")
        calculate_button.config(text="Calculate")
        result_label.config(text="Result: ")

root = tk.Tk()
root.title("Python Scientific Calculator")
root.iconbitmap('./calculator.ico') 
root.geometry("750x450")  # Increased height for the copyright statement
root.configure(bg="#000000")

# Language selection
language_var = tk.StringVar()
language_var.set("中文")  # Default language

language_frame = tk.Frame(root, bg="#2E3B4E")
language_frame.pack(pady=10)

chinese_radio = tk.Radiobutton(language_frame, text="中文", variable=language_var, value="中文", command=set_language)
english_radio = tk.Radiobutton(language_frame, text="English", variable=language_var, value="English", command=set_language)

chinese_radio.pack(side="left")
english_radio.pack(side="left")

# Add a title label
title_label = tk.Label(root, text="Python科學計算機", font=("Arial", 20), bg="#000000", fg="white")
title_label.pack(pady=10)

title_hint = tk.Label(root, text="**若要計算根號,立方根,自然對數,正弦,餘弦,正切只需要再輸入在第一個數字的輸入欄**", font=("Arial", 12), bg="#000000", fg="red")
title_hint.pack(pady=10)

entry1 = tk.Entry(root, width=18, font=("Arial", 12))
entry2 = tk.Entry(root, width=18, font=("Arial", 12))
entry1.insert(0, "輸入第一個數")

operator_var = tk.StringVar()
operator_dropdown = ttk.Combobox(root, textvariable=operator_var, values=[ "+", "-", "*", "/", "**", "sqrt", "cbrt", "%", "exp", "sin", "cos", "tan"], font=("Arial", 12), width=22)
operator_dropdown.set("請選擇運算方式")

entry2.insert(0, "輸入第二個數")
entry1.bind("<FocusIn>", clear_placeholder_1)
entry2.bind("<FocusIn>", clear_placeholder_2)

entry1.pack(padx=10, pady=10)
operator_dropdown.pack(padx=10, pady=10)
entry2.pack(padx=10, pady=10)

calculate_button = tk.Button(root, text="計算", command=calculate, font=("Arial", 14), bg="#4CAF50", fg="white")
calculate_button.pack(padx=10, pady=10)

result_label = tk.Label(root, text="計算結果: ", font=("Arial", 16), bg="#000000", fg="white")
result_label.pack(padx=10, pady=10)

# Add a copyright label at the bottom using pack
copyright_label = tk.Label(root, text="© CHANG-WEI-CHENG 2023", font=("Arial", 12), bg="#000000", fg="white")
copyright_label.pack(side="bottom")

root.bind('<Return>', lambda event=None: calculate())
root.mainloop()
