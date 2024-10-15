from tkinter import *
# =====================Settings=============================
root = Tk()
root.title('Calculator')
root.geometry('320x400')
root.resizable(width=False, height=False)
# background color
color = 'gray26'
root.configure(bg=color)
operator = ""
text_input = StringVar()
# =====================Functions============================


def btn_click(numbers):
    global operator
    operator += str(numbers)
    text_input.set(operator)


def btn_clear_display():
    global operator
    operator = ""
    text_input.set("")


def btn_equal_input():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""


# ==================Labels & Entry==========================
result_display = Entry(root, font=('arial', 20, 'bold'), textvariable=text_input,
                       bd=10, justify='right').grid(columnspan=4)
# =====================Buttons==============================
button_number_7 = Button(root, padx=12, pady=12, text='7', bd=5, font=(
    'arial', 20, 'bold'), command=lambda: btn_click(7)).grid(row=1, column=0)

button_number_8 = Button(root, padx=12, pady=12, text='8', bd=5, font=(
    'arial', 20, 'bold'), command=lambda: btn_click(8)).grid(row=1, column=1)

button_number_9 = Button(root, padx=12, pady=12, text='9', bd=5, font=(
    'arial', 20, 'bold'), command=lambda: btn_click(9)).grid(row=1, column=2)

button_oprator_multiply = Button(root, padx=12, pady=12, text='x', bd=5,bg='gray40', font=(
    'arial', 20, 'bold'), command=lambda: btn_click('*')).grid(row=1, column=3)
# # ------------------------------------------------------------
button_number_4 = Button(root, padx=12, pady=12, text='4', bd=5, font=(
    'arial', 20, 'bold'), command=lambda: btn_click(4)).grid(row=2, column=0)

button_number_5 = Button(root, padx=12, pady=12, text='5', bd=5, font=(
    'arial', 20, 'bold'), command=lambda: btn_click(5)).grid(row=2, column=1)

button_number_6 = Button(root, padx=12, pady=12, text='6', bd=5, font=(
    'arial', 20, 'bold'), command=lambda: btn_click(6)).grid(row=2, column=2)

button_oprator_minus = Button(root, padx=15, pady=12,bg='gray40', text='-',
                              bd=5, font=('arial', 20, 'bold'), command=lambda: btn_click('-')).grid(row=2, column=3)
# # -----------------------------------------------------------
button_number_1 = Button(root, padx=12, pady=12, text='1', bd=5, font=(
    'arial', 20, 'bold'), command=lambda: btn_click(1)).grid(row=3, column=0)

button_number_2 = Button(root, padx=12, pady=12, text='2', bd=5, font=(
    'arial', 20, 'bold'), command=lambda: btn_click(2)).grid(row=3, column=1)

button_number_3 = Button(root, padx=12, pady=12, text='3', bd=5, font=(
    'arial', 20, 'bold'), command=lambda: btn_click(3)).grid(row=3, column=2)

button_oprator_plus = Button(root, padx=12, pady=12,bg='gray40', text='+',
                             bd=5, font=('arial', 20, 'bold'), command=lambda: btn_click('+')).grid(row=3, column=3)
# # # ---------------------------------------------------------
button_oprator_remainder = Button(root, padx=7, pady=12, text='%',bg='gray40', bd=5, font=(
    'arial', 20, 'bold'), command=lambda: btn_click('%')).grid(row=4, column=0)

button_number_0 = Button(root, padx=12, pady=12, text='0', bd=5, font=(
    'arial', 20, 'bold'), command=lambda: btn_click(0)).grid(row=4, column=1)

button_clear = Button(root, padx=9, pady=12, text='C', bd=5,bg='gray40', font=(
    'arial', 20, 'bold'), command=btn_clear_display).grid(row=4, column=2)

button_oprator = Button(root, padx=12, pady=12, text='=', bd=5,bg='gray40', font=(
    'arial', 20, 'bold'), command=btn_equal_input).grid(row=4, column=3)
# ==========================================================
root.mainloop()
