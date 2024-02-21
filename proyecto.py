
from cProfile import label
from cgitb import text
from tkinter import *
from math import *

ventana = Tk()
#Personalizar ventana
ventana.title("Calculadora")
#Cambiar icono
#ventana.iconphoto(False, PhotoImage(file='..\calcular.png'))
#Cambiar color
ventana.config(bg='#FFFFFF')
#Tamaño de la ventaba
ventana.geometry("300x400")
#ventana.resizable(0,0)

ventana.attributes('-alpha',0.96)

color_letras1 = "black"
color_letras2 = "#8D8DAA"
color_fondo = "white"
color_fondo2 = "#E94560"

color_letras1_n = "white"
color_letras2_n = "#F05454"
color_fondo_n = "#222831"
color_fondo2_n = "#30475E"


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
display2 = Entry(ventana, font= ("Futura", 14), bg=color_fondo, fg="gray", relief="flat" )
display2.grid(row=1,columnspan=4,sticky=NSEW)
display2.config(justify=RIGHT)
display = Entry(ventana, font= ("Futura", 26, "bold"), bg=color_fondo, fg=color_letras1, relief="flat")
display.grid(row=2,columnspan=4,sticky=NSEW)
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
        display.config(bg=color_fondo, fg=color_letras1)
        display2.config(bg=color_fondo)
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
        #btn_me.config(bg=color_fondo, fg=color_letras2) 
        btnd.config(bg=color_fondo, fg=color_fondo, activebackground=color_fondo)

    else:
        display2.config(bg=color_fondo_n)
        display.config(bg=color_fondo_n, fg=color_letras1_n)
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
        #btn_me.config(bg=color_fondo_n, fg=color_letras2_n)
        btnd.config(bg=color_fondo_n, fg=color_fondo_n, activebackground=color_fondo_n)

#def agregar_elementos():
#    btn_me.destroy()
#    btn_cuadrado = Button(ventana,text="x²", font= ("Futura", 18), fg=color_fondo, bg=color_letras2, relief="flat", command=lambda:get_operation("**2"))
#    btn_cuadrado.grid(row=8, column=0, sticky=NSEW)
#    btn_raiz = Button(ventana,text="√", font= ("Futura", 18), fg=color_fondo, bg=color_letras2, relief="flat", command=lambda:get_operation("sqrt("))
#    btn_raiz.grid(row=8, column=1, sticky=NSEW)
#    btn_modulo = Button(ventana,text="mod", font= ("Futura", 18), fg=color_fondo, bg=color_letras2, relief="flat", command=lambda:get_operation("%"))
#    btn_modulo.grid(row=8, column=2, sticky=NSEW)
#    btn_exp = Button(ventana,text="exp", font= ("Futura", 18), fg=color_fondo, bg=color_letras2, relief="flat", command=lambda:get_operation("**"))
#    btn_exp.grid(row=8, column=3, sticky=NSEW)
#    btn_me2 = Button(ventana, text="^", font= ("Futura", 10, "bold"), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:quitar_elementos())
#    btn_me2.grid(row=9, columnspan=4, sticky=NSEW)

#def quitar_elementos():
#    btn_me2.destroy()
#    btn_me2.destroy()
#    btn_cuadrado.destroy()
#    btn_raiz.destroy()
#    btn_modulo.destroy()
#    btn_exp.destroy()
#    btn_me = Button(ventana, text="v", font= ("Futura", 10, "bold"), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:agregar_elementos())
#    btn_me.grid(row=8, columnspan=4, sticky=NSEW)

    

#Botones
boton_c = Button(ventana,text="(", font= ("Futura", 18), bg=color_fondo, fg=color_fondo2, relief="flat", command=lambda:get_operation("("))
boton_c.grid(row=3, column=0, sticky=NSEW)
boton_p = Button(ventana,text=")", font= ("Futura", 18), bg=color_fondo, fg=color_fondo2, relief="flat", command=lambda:get_operation(")"))
boton_p.grid(row=3, column=1, sticky=NSEW)
btn_eli = Button(ventana,text="⌫", font= ("Futura", 18), bg=color_fondo, fg=color_fondo2, relief="flat", command=lambda:undo())
btn_eli.grid(row=3, column=2, sticky=NSEW)
btn_bo = Button(ventana,text="AC", font= ("Futura", 18), bg=color_fondo, fg=color_fondo2, relief="flat", command=lambda:clear_display())
btn_bo.grid(row=7, column=2, sticky=NSEW)

btn7 = Button(ventana,text="7" , font= ("Futura", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(7))
btn7.grid(row=4, column=0, sticky=NSEW)
btn8 = Button(ventana,text="8", font= ("Futura", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(8))
btn8.grid(row=4, column=1, sticky=NSEW)
btn9 = Button(ventana,text="9", font= ("Futura", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(9))
btn9.grid(row=4, column=2, sticky=NSEW)

btn4 = Button(ventana,text="4", font= ("Futura", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(4))
btn4.grid(row=5, column=0, sticky=NSEW)
btn5 = Button(ventana,text="5", font= ("Futura", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(5))
btn5.grid(row=5, column=1, sticky=NSEW)
btn6 = Button(ventana,text="6", font= ("Futura", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(6))
btn6.grid(row=5, column=2, sticky=NSEW)

btn1 = Button(ventana,text="1", font= ("Futura", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(1))
btn1.grid(row=6, column=0, sticky=NSEW)
btn2 = Button(ventana,text="2", font= ("Futura", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(2))
btn2.grid(row=6, column=1, sticky=NSEW)
btn3 = Button(ventana,text="3", font= ("Futura", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(3))
btn3.grid(row=6, column=2, sticky=NSEW)

btn_pu = Button(ventana,text=".", font= ("Futura", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_operation("."))
btn_pu.grid(row=7, column=0, sticky=NSEW)
btn0 = Button(ventana,text="0", font= ("Futura", 18), bg=color_fondo, fg=color_letras1, relief="flat", command=lambda:get_numbers(0))
btn0.grid(row=7, column=1, sticky=NSEW)
btn_ig = Button(ventana,text="=", font= ("Futura", 20, "bold"), bg=color_fondo2, fg="white", relief="flat", command=lambda:calcular())
btn_ig.grid(row=7, column=3, sticky=NSEW)

btn_div = Button(ventana,text="÷", font= ("Futura", 20, "bold"), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:get_operation("/"))
btn_div.grid(row=3, column=3, sticky=NSEW)
btn_mul = Button(ventana,text="×", font= ("Futura", 20, "bold"), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:get_operation("*"))
btn_mul.grid(row=4, column=3, sticky=NSEW)
btn_re = Button(ventana,text="-", font= ("Futura", 20, "bold"), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:get_operation("-"))
btn_re.grid(row=5, column=3, sticky=NSEW)
btn_sum = Button(ventana,text="+", font= ("Futura", 20, "bold"), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:get_operation("+"))
btn_sum.grid(row=6, column=3, sticky=NSEW)

btn_cuadrado = Button(ventana,text="x²", font= ("Futura", 18), fg=color_fondo, bg=color_letras2, relief="flat", command=lambda:get_operation("**2"))
btn_cuadrado.grid(row=8, column=0, sticky=NSEW)
btn_raiz = Button(ventana,text="√", font= ("Futura", 18), fg=color_fondo, bg=color_letras2, relief="flat", command=lambda:get_operation("sqrt("))
btn_raiz.grid(row=8, column=1, sticky=NSEW)
btn_modulo = Button(ventana,text="mod", font= ("Futura", 18), fg=color_fondo, bg=color_letras2, relief="flat", command=lambda:get_operation("%"))
btn_modulo.grid(row=8, column=2, sticky=NSEW)
btn_exp = Button(ventana,text="exp", font= ("Futura", 18), fg=color_fondo, bg=color_letras2, relief="flat", command=lambda:get_operation("**"))
btn_exp.grid(row=8, column=3, sticky=NSEW)

#Pestaña desplegable
#btn_me = Button(ventana, text="v", font= ("Futura", 10, "bold"), bg=color_fondo, fg=color_letras2, relief="flat", command=lambda:agregar_elementos())
#btn_me.grid(row=8, columnspan=4, sticky=NSEW)
#btn_me2 = Button(ventana)

photo = PhotoImage(file="dia-noche.png")  
btnd = Button(ventana, text=" .                                                                                  ." ,image = photo, activebackground=color_fondo, bg=color_fondo, fg=color_fondo, relief="flat", compound=LEFT, command=lambda:cambiar_diseño())
btnd.grid(row=0,columnspan=4, sticky=NSEW)



ventana.mainloop()