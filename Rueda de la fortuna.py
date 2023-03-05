from tkinter import *
import random

root=Tk()
root.title("Rueda de la fortuna")
root.geometry("500x500")

label_1=Label(root,text="Rueda de la fortuna", bg="green", fg="white")
label_1.place(relx=0.5 , rely=0.3, anchor=CENTER)
label_2=Label(root,text="Pon el nombre de tu amigo" , bg="blue", fg="red")
label_2.place(relx=0.5,rely=0.4, anchor=CENTER)
entry_1=Entry(root)
entry_1.place(relx=0.5 , rely=0.5, anchor=CENTER)
label_3=Label(root,text="a")
label_3.place(relx=0.5 , rely=0.6 , anchor=CENTER)
label_4=Label(root,text="A")
label_4.place(relx=0.5 , rely=0.7 , anchor=CENTER)
label_5=Label(root,text="a")
label_5.place(relx=0.5 , rely=0.8 , anchor=CENTER)

lista_amigos=[]
def amigos():
   
    input_variable=entry_1.get()
    lista_amigos.append(input_variable)
    label_3["text"]="Tus amigos son" + str(lista_amigos)
    
def girar():
    tamaño=len(lista_amigos)
    amigo_afortunado=random.randint(0, len(lista_amigos))
    label_4["text"] = "El ganador es " + str(amigo_afortunado)
    amigo_afortunado_texto=lista_amigos[amigo_afortunado]
    label_5["text"] = amigo_afortunado_texto
        
    
    
    

button_1=Button(root,text="Agrgar a tu lista de amigos",command=amigos, bg="blue")
button_1.place(relx=0.4 , rely=0.7, anchor=CENTER)
button_2=Button(root,text="Girar la rueda" , command=girar, bg="red")
button_2.place(relx=0.7 , rely=0.7 , anchor=CENTER )
mainloop()

