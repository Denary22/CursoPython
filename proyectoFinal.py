
from cProfile import label
from cgitb import text
from tkinter import *
from math import *

ventana = Tk()
#Personalizar ventana
ventana.title("Calculadora")
#Cambiar icono
ventana.iconphoto(False, PhotoImage(file='Imagenes/calcular.png'))
#Cambiar color
ventana.config(bg='#FFFFFF')
#Tamaño de la ventaba
ventana.geometry("370x300")
ventana.resizable(0,0)

ventana.attributes('-alpha',0.94)

color_letras1 = "black"
color_letras2 = "#8D8DAA"
color_fondo = "white"
color_fondo2 = "#E94560"
color_display = "#F9F9F9"

color_letras1_n = "white"
color_letras2_n = "#F05454"
color_fondo_n = "#222831"
color_fondo2_n = "#30475E"
color_display_n = "#222829"


#Ajustar elementos
Grid.rowconfigure(ventana,1,weight=1) 
Grid.rowconfigure(ventana,2,weight=1) 
Grid.rowconfigure(ventana,3,weight=1) 
Grid.rowconfigure(ventana,4,weight=1) 
Grid.rowconfigure(ventana,5,weight=1)
Grid.rowconfigure(ventana,6,weight=1)
Grid.rowconfigure(ventana,7,weight=1)  
Grid.columnconfigure(ventana,0,weight=1)
Grid.columnconfigure(ventana,1,weight=1)
Grid.columnconfigure(ventana,2,weight=1)
Grid.columnconfigure(ventana,3,weight=1)

#Display
display2 = Entry(ventana, font= ("Abeat", 14), bg=color_display, fg="gray", relief="flat" )
display2.grid(row=1,columnspan=8,sticky=NSEW)
display2.config(justify=RIGHT)
display = Entry(ventana, font= ("Century Gothic", 26, "bold"), bg=color_display, fg=color_letras1, relief="flat")
display.grid(row=2,columnspan=8,sticky=NSEW)
display.config(justify=RIGHT)

#indice
i = 0
diseño = True

#Funciones
def get_numbers(n):
    global i
    display.insert(i,n)
    i += 1

def get_operation(operator):
    global i
    operator_length = len(operator)
    display.insert(i, operator)
    i += operator_length

def clear_display():
    display.delete(0, END)
    display2.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()

def calcular():
    global i
    display2.delete(0, END)
    ecuacion = display.get()
    display2.insert(0,ecuacion+"  ")
    try:
        str(eval(ecuacion))
    except:
        display.delete(0, END)
        display.insert(0, "E R R O R ")
    resultado = str(eval(ecuacion))
    display.delete(0, END)
    display.insert(0, resultado+" ")
    longitud = len(resultado)
    i = longitud

def cambiar_diseño():
    global diseño
    diseño=not(diseño)
    if diseño:
        display.config(bg="#F9F9F9", fg=color_letras1)
        display2.config(bg="#F9F9F9")
        boton_c.config(bg=color_fondo, fg=color_fondo2)
        boton_p.config(bg=color_fondo, fg=color_fondo2)
        btn_eli.config(bg=color_fondo, fg=color_fondo2)
        btn_bo.config(bg=color_fondo, fg=color_fondo2)
        btn7.config(bg=color_fondo, fg=color_letras1)
        btn8.config(bg=color_fondo, fg=color_letras1)
        btn9.config(bg=color_fondo, fg=color_letras1)
        btn4.config(bg=color_fondo, fg=color_letras1)
        btn5.config(bg=color_fondo, fg=color_letras1)
        btn6.config(bg=color_fondo, fg=color_letras1)
        btn3.config(bg=color_fondo, fg=color_letras1)
        btn2.config(bg=color_fondo, fg=color_letras1)
        btn1.config(bg=color_fondo, fg=color_letras1)
        btn_pu.config(bg=color_fondo, fg=color_letras1)
        btn0.config(bg=color_fondo, fg=color_letras1)
        btn_ig.config(bg=color_fondo2)
        btn_sum.config(bg=color_fondo, fg=color_letras2)
        btn_re.config(bg=color_fondo, fg=color_letras2)
        btn_mul.config(bg=color_fondo, fg=color_letras2)
        btn_div.config(bg=color_fondo, fg=color_letras2)
        btnd.config(bg="#F9F9F9", fg="#F9F9F9", activebackground="#F9F9F9")
        btn_cuadrado.config(bg=color_fondo, fg=color_letras2)
        btn_raiz.config(bg=color_fondo, fg=color_letras2)
        btn_modulo.config(bg=color_fondo, fg=color_letras2)
        btn_exp.config(bg=color_fondo, fg=color_letras2)
        btn_sen.config(bg=color_fondo, fg=color_letras2)
        btn_cos.config(bg=color_fondo, fg=color_letras2)
        btn_tan.config(bg=color_fondo, fg=color_letras2)
        btn_log.config(bg=color_fondo, fg=color_letras2)

    else:
        display2.config(bg=color_display_n)
        display.config(bg=color_display_n, fg=color_letras1_n)
        boton_c.config(bg=color_fondo_n, fg=color_fondo2_n)
        boton_p.config(bg=color_fondo_n, fg=color_fondo2_n)
        btn_eli.config(bg=color_fondo_n, fg=color_fondo2_n)
        btn_bo.config(bg=color_fondo_n, fg=color_fondo2_n)
        btn7.config(bg=color_fondo_n, fg=color_letras1_n)
        btn8.config(bg=color_fondo_n, fg=color_letras1_n)
        btn9.config(bg=color_fondo_n, fg=color_letras1_n)
        btn4.config(bg=color_fondo_n, fg=color_letras1_n)
        btn5.config(bg=color_fondo_n, fg=color_letras1_n)
        btn6.config(bg=color_fondo_n, fg=color_letras1_n)
        btn3.config(bg=color_fondo_n, fg=color_letras1_n)
        btn2.config(bg=color_fondo_n, fg=color_letras1_n)
        btn1.config(bg=color_fondo_n, fg=color_letras1_n)
        btn_pu.config(bg=color_fondo_n, fg=color_letras1_n)
        btn0.config(bg=color_fondo_n, fg=color_letras1_n)
        btn_ig.config(bg=color_fondo2_n)
        btn_sum.config(bg=color_fondo_n, fg=color_letras2_n)
        btn_re.config(bg=color_fondo_n, fg=color_letras2_n)
        btn_mul.config(bg=color_fondo_n, fg=color_letras2_n)
        btn_div.config(bg=color_fondo_n, fg=color_letras2_n)
        btnd.config(bg=color_display_n, fg=color_display_n, activebackground=color_display_n)
        btn_cuadrado.config(bg=color_fondo_n, fg=color_letras2_n)
        btn_raiz.config(bg=color_fondo_n, fg=color_letras2_n)
        btn_modulo.config(bg=color_fondo_n, fg=color_letras2_n)
        btn_exp.config(bg=color_fondo_n, fg=color_letras2_n)
        btn_sen.config(bg=color_fondo_n, fg=color_letras2_n)
        btn_cos.config(bg=color_fondo_n, fg=color_letras2_n)
        btn_tan.config(bg=color_fondo_n, fg=color_letras2_n)
        btn_log.config(bg=color_fondo_n, fg=color_letras2_n)


#Botones
boton_c = Button(ventana,text="(", font= ("Century Gothic", 18), bg=color_fondo, fg=color_fondo2, relief="flat", command=lambda:get_operation("("))
boton_c.grid(row=4, column=6, sticky=NSEW)
boton_p = Button(ventana,text=")", font= ("Century Gothic", 18), bg=color_fondo, fg=color_fondo2, relief="flat", command=lambda:get_operation(")"))
boton_p.grid(row=4, column=7, sticky=NSEW)
btn_eli = Button(ventana,text="⌫", font= ("Century Gothic", 18), bg=color_fondo, fg=color_fondo2, relief="flat", command=lambda:undo())
btn_eli.grid(row=3, column=6 , columnspan=2, sticky=NSEW)
btn_bo = Button(ventana,text="AC", font= ("Century Gothic", 18), bg=color_fondo, fg=color_fondo2, relief="flat", command=lambda:clear_display())
btn_bo.grid(row=6, column=4, sticky=NSEW)

btn7 = Button(ventana,text="7" , font= ("Abeat", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(7))
btn7.grid(row=3, column=2, sticky=NSEW)
btn8 = Button(ventana,text="8", font= ("Abeat", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(8))
btn8.grid(row=3, column=3, sticky=NSEW)
btn9 = Button(ventana,text="9", font= ("Abeat", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(9))
btn9.grid(row=3, column=4, sticky=NSEW)

btn4 = Button(ventana,text="4", font= ("Abeat", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(4))
btn4.grid(row=4, column=2, sticky=NSEW)
btn5 = Button(ventana,text="5", font= ("Abeat", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(5))
btn5.grid(row=4, column=3, sticky=NSEW)
btn6 = Button(ventana,text="6", font= ("Abeat", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(6))
btn6.grid(row=4, column=4, sticky=NSEW)

btn1 = Button(ventana,text="1", font= ("Abeat", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(1))
btn1.grid(row=5, column=2, sticky=NSEW)
btn2 = Button(ventana,text="2", font= ("Abeat", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(2))
btn2.grid(row=5, column=3, sticky=NSEW)
btn3 = Button(ventana,text="3", font= ("Abeat", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(3))
btn3.grid(row=5, column=4, sticky=NSEW)

btn_pu = Button(ventana,text=".", font= ("Futura", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_operation("."))
btn_pu.grid(row=6, column=2, sticky=NSEW)
btn0 = Button(ventana,text="0", font= ("Abeat", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(0))
btn0.grid(row=6, column=3, sticky=NSEW)
btn_ig = Button(ventana,text="=", font= ("Abeat", 20, "bold"), bg=color_fondo2, fg="white", relief="flat", command=lambda:calcular())
btn_ig.grid(row=5, column=6, rowspan=2, columnspan=2, sticky=NSEW) #5,6

btn_div = Button(ventana,text="÷", font= ("Abeat", 20, "bold"), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:get_operation("/"))
btn_div.grid(row=3, column=5, sticky=NSEW)
btn_mul = Button(ventana,text="×", font= ("Abeat", 20, "bold"), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:get_operation("*"))
btn_mul.grid(row=4, column=5, sticky=NSEW)
btn_re = Button(ventana,text="-", font= ("Abeat", 20, "bold"), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:get_operation("-"))
btn_re.grid(row=5, column=5, sticky=NSEW)
btn_sum = Button(ventana,text="+", font= ("Abeat", 20, "bold"), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:get_operation("+"))
btn_sum.grid(row=6, column=5, sticky=NSEW)

btn_cuadrado = Button(ventana,text="x²", font= ("Abeat", 16), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:get_operation("**2"))
btn_cuadrado.grid(row=3, column=0, sticky=NSEW)
btn_raiz = Button(ventana,text="√", font= ("Abeat", 16), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:get_operation("sqrt("))
btn_raiz.grid(row=3, column=1, sticky=NSEW)
btn_modulo = Button(ventana,text="mod", font= ("Abeat", 16), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:get_operation("%"))
btn_modulo.grid(row=4, column=0, sticky=NSEW)
btn_exp = Button(ventana,text="exp", font= ("Abeat", 16), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:get_operation("**"))
btn_exp.grid(row=4, column=1, sticky=NSEW)
btn_sen = Button(ventana,text="sen", font= ("Abeat", 16), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:get_operation("sin("))
btn_sen.grid(row=5, column=0, sticky=NSEW)
btn_cos = Button(ventana,text="cos", font= ("Abeat", 16), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:get_operation("cos("))
btn_cos.grid(row=5, column=1, sticky=NSEW)
btn_tan = Button(ventana,text="tan", font= ("Abeat", 16), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:get_operation("tan("))
btn_tan.grid(row=6, column=0, sticky=NSEW)
btn_log = Button(ventana,text="ln", font= ("Abeat", 16), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:get_operation("log("))
btn_log.grid(row=6, column=1, sticky=NSEW)


photo = PhotoImage(file = "Imagenes/dia-noche.png")  
btnd = Button(ventana, text=" .                                                                                                          ." ,image = photo, activebackground=color_display, bg=color_display, fg=color_display, relief="flat", compound=LEFT, command=lambda:cambiar_diseño())
btnd.grid(row=0,columnspan=8, sticky=NSEW)



ventana.mainloop()