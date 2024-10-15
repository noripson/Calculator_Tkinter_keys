from tkinter import *
# =====================Settings=============================
root = Tk()
root.title('Calculator')
root.geometry('330x460')
root.resizable(width=False, height=False)
# background color
color = 'gray26'
root.configure(bg=color)
# =====================Functions============================

# =====================Frames===============================
frame1 = Frame(root, width=500, height=80, bg=color)
frame1.pack(side=TOP)

frame2 = Frame(root, width=500, height=10, highlightbackground=color)
frame2.pack(side=TOP)

frame3 = Frame(root, width=500, height=10, highlightbackground=color)
frame3.pack(side=TOP)

frame4 = Frame(root, width=500, height=10, highlightbackground=color)
frame4.pack(side=TOP)

frame5 = Frame(root, width=500, height=10, highlightbackground=color)
frame5.pack(side=TOP)

frame6 = Frame(root, width=500, height=10, highlightbackground=color)
frame6.pack(side=TOP)
# ==================Labels & Entry==========================
result_display = Entry(frame1, font=('arial', 20, 'bold'), bd=10, justify='right').grid(columnspan=4)
# =====================Buttons==============================
button_number_7 = Button(frame3, width=8, height=5, text='7', bd=5)
button_number_7.pack(side=LEFT, pady=2, padx=2)

button_number_8 = Button(frame3, width=8, height=5, text='8', bd=5)
button_number_8.pack(side=LEFT, pady=2, padx=2)

button_number_9 = Button(frame3, width=8, height=5, text='9', bd=5)
button_number_9.pack(side=LEFT, pady=2, padx=2)

button_oprator_multiply = Button(frame3, width=8, height=5, text='x', bd=5)
button_oprator_multiply.pack(side=LEFT, pady=2, padx=2)
# ------------------------------------------------------------
button_number_4 = Button(frame4, width=8, height=5, text='4', bd=5)
button_number_4.pack(side=LEFT, pady=2, padx=2)

button_number_5 = Button(frame4, width=8, height=5, text='5', bd=5)
button_number_5.pack(side=LEFT, pady=2, padx=2)

button_number_6 = Button(frame4, width=8, height=5, text='6', bd=5)
button_number_6.pack(side=LEFT, pady=2, padx=2)

button_oprator_minus = Button(frame4, width=8, height=5, text='-', bd=5)
button_oprator_minus.pack(side=LEFT, pady=2, padx=2)
# -----------------------------------------------------------
button_number_1 = Button(frame5, width=8, height=5, text='1', bd=5)
button_number_1.pack(side=LEFT, pady=2, padx=2)

button_number_2 = Button(frame5, width=8, height=5, text='2', bd=5)
button_number_2.pack(side=LEFT, pady=2, padx=2)

button_number_3 = Button(frame5, width=8, height=5, text='3', bd=5)
button_number_3.pack(side=LEFT, pady=2, padx=2)

button_oprator_plus = Button(frame5, width=8, height=5, text='+', bd=5)
button_oprator_plus.pack(side=LEFT, pady=2, padx=2)
# ---------------------------------------------------------
button_oprator_remainder = Button(frame6, width=8, height=5, text='%', bd=5,)
button_oprator_remainder.pack(side=LEFT, pady=2, padx=2)

button_number_0 = Button(frame6, width=8, height=5, text='0', bd=5)
button_number_0.pack(side=LEFT, pady=2, padx=2)

button_clear = Button(frame6, width=8, height=5, text='=', bd=5)
button_clear.pack(side=LEFT, pady=2, padx=2)

button_oprator = Button(frame6, width=8, height=5, text='X', bd=5)
button_oprator.pack(side=LEFT, pady=2, padx=2)
# ==========================================================
root.mainloop()
