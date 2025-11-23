import tkinter as tk
from tkinter import messagebox, scrolledtext
import datetime

# Função para salvar o humor com horário
def salvar_humor(humor):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("registro_humor.txt", "a") as f:
        f.write(f"{now} - {humor}\n")

# Sugestões por humor
def sugerir_atividade(humor):
    sugestoes = {
        "Feliz": "Dance um pouco! Coloque sua música preferida e aproveite esse momento.",
        "Triste": "Tente escrever como se sente, ou ouvir uma música calma com fones.",
        "Ansiosa": "Feche os olhos por 1 minuto. Respire fundo e solte lentamente.",
        "Cansada": "Levante-se e faça um alongamento suave com os braços e costas.",
        "Outro": "Lembre-se: você não precisa se encaixar. Apenas sinta. Está tudo bem."
    }
    return sugestoes.get(humor, "Respire fundo e pense com carinho em você mesma.")

# Quando o botão é clicado
def registrar_e_sugerir(humor):
    salvar_humor(humor)
    atividade = sugerir_atividade(humor)
    messagebox.showinfo("Sugestão pra você 💛", atividade)

# Mostrar histórico em uma nova janela
def mostrar_historico():
    try:
        with open("registro_humor.txt", "r") as f:
            conteudo = f.read()
    except FileNotFoundError:
        conteudo = "Nenhum registro ainda."

    historico = tk.Toplevel(root)
    historico.title("Histórico de Humores")
    text_area = scrolledtext.ScrolledText(historico, width=50, height=15)
    text_area.pack(padx=10, pady=10)
    text_area.insert(tk.END, conteudo)
    text_area.config(state="disabled")

# Janela principal
root = tk.Tk()
root.title("Organizador Emocional da Luminha")
root.geometry("400x500")

tk.Label(root, text="🌈 Como você está se sentindo hoje?", font=("Helvetica", 16)).pack(pady=20)

# Emojis + humores
humores_emojis = {
    "Feliz": "😊",
    "Triste": "😢",
    "Ansiosa": "😰",
    "Cansada": "😩",
    "Outro": "🤔"
}

for humor, emoji in humores_emojis.items():
    btn = tk.Button(root, text=f"{emoji} {humor}", width=25, height=2,
                    font=("Helvetica", 12),
                    command=lambda h=humor: registrar_e_sugerir(h))
    btn.pack(pady=5)

# Botão para ver histórico
btn_hist = tk.Button(root, text="📜 Ver histórico", command=mostrar_historico)
btn_hist.pack(pady=20)

root.mainloop()
