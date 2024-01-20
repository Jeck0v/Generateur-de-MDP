import tkinter as tk
from tkinter import Text, Scrollbar
import secrets
import string

def generate_password():
    try:
        base_length = length_var.get()
        additional_length = int(custom_length_entry.get()) if custom_length_var.get() else 0
        total_length = base_length + additional_length

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(total_length))

        output_text.delete(1.0, tk.END)  # Efface le contenu précédent
        output_text.insert(tk.END, f"Mot de Passe : {password}")
    except ValueError:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Erreur, veuillez entrer le nombre de caractères que vous souhaiter.")


window = tk.Tk()
window.title("Générateur de mot de passe sécurisé")


label = tk.Label(window, text="Taille du mot de passe:")
label.pack(pady=10)

length_var = tk.IntVar()
length_scale = tk.Scale(window, variable=length_var, from_=10, to=50, orient=tk.HORIZONTAL, tickinterval=5, length=300)
length_scale.pack(pady=10)

custom_length_var = tk.BooleanVar()
custom_length_checkbox = tk.Checkbutton(window, text="Utiliser un nombre personnalisé de caractères en plus des caractères", variable=custom_length_var)
custom_length_checkbox.pack(pady=5)

custom_length_label = tk.Label(window, text="Nombre personnalisé de caractères: ")
custom_length_label.pack(pady=5)

custom_length_entry = tk.Entry(window)
custom_length_entry.pack(pady=5)

button = tk.Button(window, text="Générer un mot de passe", command=generate_password)
button.pack(pady=20)

output_text = Text(window, height=5, width=40, wrap=tk.WORD)
output_text.pack(pady=10)


scrollbar = Scrollbar(window, command=output_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_text.config(yscrollcommand=scrollbar.set)




#PS: la couleur de base est blanche, grise vous pouvez la modifier en rajoutant 
# bg_color = "#e6e6e6"    #changer la couleur souhaiter
# window.configure(bg=bg_color)
# il faudra rajouter l'argument bg =bg_color sur le reste de la partie interface graphique pour que tout les éléments est la couleur


window.mainloop()
