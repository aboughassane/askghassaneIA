import openai
import tkinter

openai.api_key = "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"

def generate_response():
    ask = input_box.get('1.0', tkinter.END) # Récupère la question saisie par l'utilisateur
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=ask,
        temperature=0.9,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    text = response['choices'][0]['text']
    output_box.delete('1.0', '5.0') # Efface le contenu de la boîte de sortie
    output_box.insert(tkinter.END, text) # Affiche la réponse de l'API OpenAI
    input_box.delete("1.0", "end") # Efface le contenu de saisie

root = tkinter.Tk()
root.title("Boot Aboughassane")
root.geometry('800x400')

# Crée une boîte de saisie pour l'utilisateur
input_label = tkinter.Label(root, text="ASK ABOUGHASSANE:",bg="#c7bbc9")
input_label.pack()
input_box = tkinter.Entry(root)
input_box = tkinter.Text(root, width=80, height=5)    

input_box.pack()
input_box.configure(bg="#E0E0E0",font=('Arial', 11)) # mettre un fond  pour la boîte de saisie


# Crée un bouton pour générer une réponse à partir de la question saisie
generate_button = tkinter.Button(root, text="Générer une réponse", command=generate_response,bg="#c7bbc9")
generate_button.pack()

# Crée une boîte de sortie pour afficher la réponse générée par l'API OpenAI
output_label = tkinter.Label(root, text="Réponse:",bg="#c7bbc9")
output_label.pack()
output_box = tkinter.Text(root, height=10)
output_box.pack()
output_box.configure(bg="#99004C",font=('Arial', 14),fg = "#FFFFFF") # mettre un fond bleu pour la boîte de reponse




root.configure(bg= "#404040")  # Définit la couleur fond de la fenêtre principale

output_box.configure(height=10)
output_box.configure(width=80)



root.mainloop()


# input_box.config(bg=custom_red) # Définit la couleur de fond de la boîte de saisie
# generate_button.config(bg=custom_red, fg="white") # Définit la couleur de fond et de texte du bouton

