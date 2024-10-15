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
# resultlabel = Label(frame1, width=290, height=76, text=50000)
# resultlabel.pack(side=LEFT)
# =====================Buttons==============================
button_number_7= Button(frame3, width=10, height=5, text='7')
button_number_7.pack(side=LEFT,pady=2,padx=2)

button_number_8= Button(frame3, width=10, height=5, text='8')
button_number_8.pack(side=LEFT,pady=2,padx=2)

button_number_9= Button(frame3, width=10, height=5, text='9')
button_number_9.pack(side=LEFT,pady=2,padx=2)

button_oprator_multiply= Button(frame3, width=10, height=5, text='x')
button_oprator_multiply.pack(side=LEFT,pady=2,padx=2)
# ------------------------------------------------------------
button_number_4= Button(frame4, width=10, height=5, text='4')
button_number_4.pack(side=LEFT,pady=2,padx=2)

button_number_5= Button(frame4, width=10, height=5, text='5')
button_number_5.pack(side=LEFT,pady=2,padx=2)

button_number_6= Button(frame4, width=10, height=5, text='6')
button_number_6.pack(side=LEFT,pady=2,padx=2)

button_oprator_minus= Button(frame4, width=10, height=5, text='-')
button_oprator_minus.pack(side=LEFT,pady=2,padx=2)
# -----------------------------------------------------------
button_number_1= Button(frame5, width=10, height=5, text='1')
button_number_1.pack(side=LEFT,pady=2,padx=2)

button_number_2= Button(frame5, width=10, height=5, text='2')
button_number_2.pack(side=LEFT,pady=2,padx=2)

button_number_3= Button(frame5, width=10, height=5, text='3')
button_number_3.pack(side=LEFT,pady=2,padx=2)

button_oprator_plus= Button(frame5, width=10, height=5, text='+')
button_oprator_plus.pack(side=LEFT,pady=2,padx=2)
# ---------------------------------------------------------
button_oprator_remainder= Button(frame6, width=10, height=5, text='%')
button_oprator_remainder.pack(side=LEFT,pady=2,padx=2)

button_number_0= Button(frame6, width=10, height=5, text='0')
button_number_0.pack(side=LEFT,pady=2,padx=2)

button_clear= Button(frame6, width=10, height=5, text='=')
button_clear.pack(side=LEFT,pady=2,padx=2)

button_oprator_result= Button(frame6, width=10, height=5, text='X')
button_oprator_result.pack(side=LEFT,pady=2,padx=2)
# ==========================================================
root.mainloop()
