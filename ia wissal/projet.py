from experta import *
from tkinter import *

""" fonction d'interface graphique """
def poidint(a)->float:
    global q1
    choix = a
    try:
        choix=float(choix)
        if(choix>=50 and choix<=300):
            return choix
        else:
            q1.set("Erreur: le poid doit etre entre 50 et 300!")
                
    except ValueError:
        q1.set("Erreur:  le poid n'accepte que des valeur numerique!")
        
        
def sexeint(a):
    global q2
    choix =a
    if(choix=="homme" or choix =="femme"):
        return a
    else:
        q2.set("Erreur: le sexe ne accepte que les valeur \"Homme\"/\"Femme\"!")
    
def hauteurint(a)->float:
    global q3
    verfi = True;
    choix =a
    try:
        choix=float(choix)
        if(choix>=110 and choix<=230):
            return choix/100
        else:
            q3.set("Erreur: l'hauteur doit etre entre 110 et 230!")
            
    except ValueError:
        q3.set("Erreur:  l'hauteur n'accepte que des valeur numerique!")

def partieint(a):
    global q4
    choix =a
    if(choix=="pied" or choix =="poitrine"):
        return a
    else:
        q4.set("Erreur: selection l'une des partie cite au question!\n")





def btn_clicked():
    global q1,q2,q3,q4,exerciceAFaire,resultat,canvas
    exerciceAFaire="Liste des Exercice a faire :\n"
    r1=q1.get()
    r2=q2.get()
    r3=q3.get()
    r4=q4.get()
    
    p=poidint(r1)
    s=sexeint(r2)
    h=hauteurint(r3)
    part=partieint(r4)
    if(part != None and p != None and s != None and h != None):
        i= calculeicm(p,h)
        print("poid = ",p)
        print("sexe = ",s)
        print("hauteur = ",h)
        print("partie = ",part)
    
        engine = Sportif()
        engine.reset()
        engine.declare(Exercice(icm=i,
                            partie=part,
                            sexe=s))
        engine.run()
        canvas.itemconfig(resultat,  text=exerciceAFaire)

    



""" les variable global """
Options = {
  "sexe": False,
  "icm": False,
  "partie": False
}

exerciceAFaire="Liste des Exercice a faire :\n"
resultat=""
canvas=""
q1=""
q2=""
q3=""
q4=""



""" Controle de saisir """
def poid()->float:
    verfi = True;
    choix =""
    while(verfi):
        choix = input("1- Saisir votre poid en kg(un nombre entre 50 et 300):\n\t").lower()
        #verification du type
        try:
            choix=float(choix)
            if(choix>=50 and choix<=300):
                verif=False;
                return choix
            else:
                print("Erreur: le poid doit etre entre 50 et 300!\n")
                
        except ValueError:
            print("Erreur:  le poid n'accepte que des valeur numerique!\n")
            
        
def sexe():
    choix =""
    while(choix!="homme" or choix !="femme"):
        choix = input("2- Saisir votre Sexe (\"Homme\"/\"Femme\"):\n\t").lower()
        if(choix=="homme" or choix =="femme"):
            return choix
        else:
            print("Erreur: le sexe ne accepte que les valeur \"Homme\"/\"Femme\"!\n")
    
def hauteur()->float:
    verfi = True;
    choix =""
    while(verfi):
        choix = input("3- Saisir votre hauteur en cm(un nombre entre 110 et 230):\n\t").lower()
        #verification du type
        try:
            choix=float(choix)
            if(choix>=110 and choix<=230):
                verif=False;
                return choix/100
            else:
                print("Erreur: l\'hauteur doit etre entre 110 et 230!\n")
                
        except ValueError:
            print("Erreur:  l\'hauteur n'accepte que des valeur numerique!\n")

def partie():
    choix =""
    while(choix!="pied" or choix !="poitrine"):
        choix = input("4- Saisir la partie cible (\"pied\"/\"poitrine\"):\n\t").lower()
        if(choix=="pied" or choix =="poitrine"):
            return choix
        else:
            print("Erreur: selection l'une des partie cite au question!\n")


def calculeicm(poid ,hauteur)->float:
    return poid/(hauteur*hauteur)
    

""" saisir les faits """
def Questions():
    global Options
    p= poid()
    Options["sexe"] = sexe()
    h= hauteur()
    Options["partie"] = partie()
    i= calculeicm(p,h)
    Options["icm"] = i
    



""" definition de notre systeme expert """
class Exercice(Fact):
    """ choisir les exercice le plus approprier a votre cas """
    pass


class Sportif(KnowledgeEngine):    
    @Rule(Exercice(icm=MATCH.icm,sexe="homme",partie="pied"))
    def hommepied(self,icm):
        global exerciceAFaire
        if(icm>30):
            exerciceAFaire +="Exercice de pied pour homme avec icm >30"
        elif(icm<30 and icm>15):
            exerciceAFaire +="Exercice de pied pour homme avec icm>15 et icm<30"
        
    @Rule(Exercice(icm=MATCH.icm,sexe="femme",partie="pied"))
    def femmepied(self,icm):
        global exerciceAFaire
        if(icm>30):
            exerciceAFaire +="Exercice de piedpour femme avec icm >30"
        elif(icm<30 and icm>15):
            exerciceAFaire +="Exercice de pied pour femme avec icm>15 et icm<30"
    

def consolemenu():
    global Options,exerciceAFaire,canvas,result
    Questions()
    engine = Sportif()
    engine.reset()
    engine.declare(Exercice(icm=Options["icm"],
                        partie=Options["partie"],
                        sexe=Options["sexe"]))
    engine.run()
    print(exerciceAFaire)




""" interface graphique """
def interfacegraphique():
    global q1,q2,q3,q4,resultat,canvas
    window = Tk()
    q1 = StringVar()
    q2 = StringVar()
    q3 = StringVar()
    q4 = StringVar()
    q1.set("50")
    q2.set("femme")
    q3.set("110")
    q4.set("pied")
    
    
    
    window.geometry("1220x660")
    window.configure(bg = "#000000")
    window.title("Bour La Fourme")
    canvas = Canvas(
        window,
        bg = "#000000",
        height = 660,
        width = 1220,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    background_img = PhotoImage(file = f"background.png")
    background = canvas.create_image(
        610.0, 330.0,
        image=background_img)
    
    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")
    
    b0.place(
        x = 509, y = 567,
        width = 201,
        height = 53)
    
    canvas.create_text(
        247.5, 414.5,
        text = "4- Saisir la partie cible ( pied/ poitrine ):",
        fill = "#ffffff",
        font = ("Sen-Regular", int(17.0)))
    
    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(
        352.5, 448.0,
        image = entry0_img)
    
    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        textvariable=q4,
        highlightthickness = 0)
    
    entry0.place(
        x = 50.0, y = 435,
        width = 605.0,
        height = 26)
    
    canvas.create_text(
        346.5, 335.5,
        text = "3- Saisir votre hauteur en cm (un nombre entre 110 - 230):",
        fill = "#ffffff",
        font = ("Sen-Regular", int(17.0)))
    
    entry1_img = PhotoImage(file = f"img_textBox1.png")
    entry1_bg = canvas.create_image(
        352.5, 369.0,
        image = entry1_img)
    
    entry1 = Entry(
        bd = 0,
        bg = "#ffffff",
        textvariable=q3,
        highlightthickness = 0)
    
    entry1.place(
        x = 50.0, y = 356,
        width = 605.0,
        height = 26)
    
    canvas.create_text(
        314.5, 175.5,
        text = "1- Saisir votre poid en kg(un nombre entre 50 - 300):",
        fill = "#ffffff",
        font = ("Sen-Regular", int(17.0)))
    
    entry2_img = PhotoImage(file = f"img_textBox2.png")
    entry2_bg = canvas.create_image(
        352.5, 209.0,
        image = entry2_img)
    
    entry2 = Entry(
        bd = 0,
        bg = "#ffffff",
        textvariable=q1,
        highlightthickness = 0)
    
    entry2.place(
        x = 50.0, y = 196,
        width = 605.0,
        height = 26)
    
    entry3_img = PhotoImage(file = f"img_textBox3.png")
    entry3_bg = canvas.create_image(
        352.5, 290.0,
        image = entry3_img)
    
    entry3 = Entry(
        bd = 0,
        bg = "#ffffff",
        textvariable=q2,
        highlightthickness = 0)
    
    entry3.place(
        x = 50.0, y = 277,
        width = 605.0,
        height = 26)
    
    canvas.create_text(
        258.5, 256.5,
        text = "2- Saisir votre Sexe ( Homme / Femme):",
        fill = "#ffffff",
        font = ("Sen-Regular", int(17.0)))
    
    resultat=canvas.create_text(
        875.5, 200.5,
        text = "Liste d'exercice a faire:",
        fill = "#ffffff",
        font = ("Sen-Regular", int(17.0)))
    
    window.resizable(False, False)
    window.mainloop()
 
 
 
 #consolemenu()
interfacegraphique()
