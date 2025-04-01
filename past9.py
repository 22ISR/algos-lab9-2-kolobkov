import tkinter as tk
root = tk.Tk()
root.geometry("800x500")
root.title("Моя программа")

label = tk.Label(root, text="Калькулятор", font=("Arial", 18))
label.pack(padx=20, pady=20)
textbox = tk.Entry(root, font=("Arial", 16))
textbox.pack(padx=20, pady=20)
buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)

btn1 = tk.Button(buttonFrame, text="1", font=("Arial", 18))
btn1.grid(row=0, column=0, sticky="we")
buttonFrame.pack(fill="x")

btn1 = tk.Button(buttonFrame, text="2", font=("Arial", 18))
btn1.grid(row=0, column=1, sticky="we")
buttonFrame.pack(fill="x")

btn1 = tk.Button(buttonFrame, text="3", font=("Arial", 18))
btn1.grid(row=0, column=2, sticky="we")
buttonFrame.pack(fill="x")

btn1 = tk.Button(buttonFrame, text="-", font=("Arial", 18))
btn1.grid(row=0, column=3, sticky="we")
buttonFrame.pack(fill="x")


btn1 = tk.Button(buttonFrame, text="4", font=("Arial", 18))
btn1.grid(row=1, column=0, sticky="we")
buttonFrame.pack(fill="x")

btn1 = tk.Button(buttonFrame, text="5", font=("Arial", 18))
btn1.grid(row=1, column=1, sticky="we")
buttonFrame.pack(fill="x")

btn1 = tk.Button(buttonFrame, text="6", font=("Arial", 18))
btn1.grid(row=1, column=2, sticky="we")
buttonFrame.pack(fill="x")

btn1 = tk.Button(buttonFrame, text="+", font=("Arial", 18))
btn1.grid(row=1, column=3, sticky="we")
buttonFrame.pack(fill="x")


btn1 = tk.Button(buttonFrame, text="7", font=("Arial", 18))
btn1.grid(row=2, column=0, sticky="we")
buttonFrame.pack(fill="x")

btn1 = tk.Button(buttonFrame, text="8", font=("Arial", 18))
btn1.grid(row=2, column=1, sticky="we")
buttonFrame.pack(fill="x")

btn1 = tk.Button(buttonFrame, text="9", font=("Arial", 18))
btn1.grid(row=2, column=2, sticky="we")
buttonFrame.pack(fill="x")

btn1 = tk.Button(buttonFrame, text="*", font=("Arial", 18))
btn1.grid(row=2, column=3, sticky="we")
buttonFrame.pack(fill="x")


btn1 = tk.Button(buttonFrame, text="Clear", font=("Arial", 18))
btn1.grid(row=3, column=0, sticky="we")
buttonFrame.pack(fill="x")

btn1 = tk.Button(buttonFrame, text="0", font=("Arial", 18))
btn1.grid(row=3, column=1, sticky="we")
buttonFrame.pack(fill="x")

btn1 = tk.Button(buttonFrame, text="=", font=("Arial", 18))
btn1.grid(row=3, column=2, sticky="we")
buttonFrame.pack(fill="x")

btn1 = tk.Button(buttonFrame, text="/", font=("Arial", 18))
btn1.grid(row=3, column=3, sticky="we")
buttonFrame.pack(fill="x")

root.mainloop()
