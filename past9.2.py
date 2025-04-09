import tkinter as tk
import math
root = tk.Tk()
root.geometry("800x500")
root.title("Калькулятор")

def on_button_click(value):
    if value == "=":
        try:
            result = eval(textbox.get("1.0", tk.END))
            print(result)
            textbox.delete("1.0", tk.END) 
            textbox.insert(tk.END, result)
        except ZeroDivisionError:
            print("Error")
            textbox.delete("1.0", tk.END) 
            textbox.insert(tk.END, "Error")
        except Exception as e:
            textbox.delete("1.0", tk.END) 
            textbox.insert(tk.END, "Error")
    elif value == "√":
        koren = eval(textbox.get("1.0", tk.END))
        sqrt_math = math.sqrt(koren)
        textbox.delete("1.0", tk.END) 
        textbox.insert(tk.END, sqrt_math)
    elif value == "clear":
        textbox.delete("1.0", tk.END)
    else:
        textbox.insert(tk.END, value)


label = tk.Label(root, text="Калькулятор", font=("Arial", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack(padx=10, pady=10)

buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)

buttonFrame.pack(fill="x")
btnsqrt = tk.Button(buttonFrame, text="√", font=("Arial", 18), command=lambda v="√": on_button_click(v))
btnsqrt.grid(row=0, column=3, sticky="we")

btnright = tk.Button(buttonFrame, text=")", font=("Arial", 18), command=lambda v=")": on_button_click(v))
btnright.grid(row=0, column=2, sticky="we")

btnleft = tk.Button(buttonFrame, text="(", font=("Arial", 18), command=lambda v="(": on_button_click(v))
btnleft.grid(row=0, column=1, sticky="we")

btnpoint = tk.Button(buttonFrame, text=".", font=("Arial", 18), command=lambda v=".": on_button_click(v))
btnpoint.grid(row=0, column=0, sticky="we")

btn1 = tk.Button(buttonFrame, text="1", font=("Arial", 18), command=lambda v="1": on_button_click(v))
btn1.grid(row=1, column=0, sticky="we")

btn2 = tk.Button(buttonFrame, text="2", font=("Arial", 18), command=lambda v="2": on_button_click(v))
btn2.grid(row=1, column=1, sticky="we")

btn3 = tk.Button(buttonFrame, text="3", font=("Arial", 18), command=lambda v="3": on_button_click(v))
btn3.grid(row=1, column=2, sticky="we")

btnminus = tk.Button(buttonFrame, text="-", font=("Arial", 18), command=lambda v="-": on_button_click(v))
btnminus.grid(row=1, column=3, sticky="we")

btn4 = tk.Button(buttonFrame, text="4", font=("Arial", 18), command=lambda v="4": on_button_click(v))
btn4.grid(row=2, column=0, sticky="we")

btn5 = tk.Button(buttonFrame, text="5", font=("Arial", 18), command=lambda v="5": on_button_click(v))
btn5.grid(row=2, column=1, sticky="we")

btn6 = tk.Button(buttonFrame, text="6", font=("Arial", 18), command=lambda v="6": on_button_click(v))   
btn6.grid(row=2, column=2, sticky="we")

btnplus = tk.Button(buttonFrame, text="+", font=("Arial", 18), command=lambda v="+": on_button_click(v))  
btnplus.grid(row=2, column=3, sticky="we")

btn7 = tk.Button(buttonFrame, text="7", font=("Arial", 18), command=lambda v="7": on_button_click(v))
btn7.grid(row=3, column=0, sticky="we")

btn8 = tk.Button(buttonFrame, text="8", font=("Arial", 18), command=lambda v="8": on_button_click(v))
btn8.grid(row=3, column=1, sticky="we")

btn9 = tk.Button(buttonFrame, text="9", font=("Arial", 18), command=lambda v="9": on_button_click(v) )
btn9.grid(row=3, column=2, sticky="we")

btnymn = tk.Button(buttonFrame, text="*", font=("Arial", 18), command=lambda v="*": on_button_click(v))
btnymn.grid(row=3, column=3, sticky="we")

btnclear = tk.Button(buttonFrame, text="Clear", font=("Arial", 18), command=lambda v="clear": on_button_click(v))
btnclear.grid(row=4, column=0, sticky="we")

btn0 = tk.Button(buttonFrame, text="0", font=("Arial", 18), command=lambda v="0": on_button_click(v))
btn0.grid(row=4, column=1, sticky="we")

btnrovn = tk.Button(buttonFrame, text="=", font=("Arial", 18), command=lambda v="=": on_button_click(v))
btnrovn.grid(row=4, column=2, sticky="we")

btndel = tk.Button(buttonFrame, text="/", font=("Arial", 18), command=lambda v="/": on_button_click(v))
btndel.grid(row=4, column=3, sticky="we")


root.mainloop()
