import tkinter as tk
from tkinter import ttk
import random
import threading


def roll_die_simulation():
    def run_simulation():
        # Inicializa as frequências
        frequencies = [0, 0, 0, 0, 0, 0]
        
        # Roda os lançamentos
        for _ in range(6000000):
            face = random.randint(1, 6)
            frequencies[face - 1] += 1

        # Atualiza os resultados na interface
        for i in range(6):
            results_labels[i].config(text=str(frequencies[i]))

        # Reativa o botão
        simulate_button.config(state=tk.NORMAL)

    # Desativa o botão durante a simulação
    simulate_button.config(state=tk.DISABLED)

    # Cria e executa a thread
    threading.Thread(target=run_simulation).start()


# Configuração da interface gráfica
app = tk.Tk()
app.title("Simulador de Lançamento de Dados")
app.geometry("550x450")
app.config(bg="#222831")

# Título
title_label = tk.Label(
    app, 
    text="Simulador de Lançamento de Dados 🎲", 
    font=("Helvetica", 20, "bold"), 
    bg="#222831", 
    fg="#f2a365"
)
title_label.pack(pady=15)

# Descrição
description_label = tk.Label(
    app, 
    text="Clique no botão para simular 6.000.000 lançamentos.", 
    font=("Helvetica", 12), 
    bg="#222831", 
    fg="#eeeeee"
)
description_label.pack(pady=5)

# Cabeçalhos
header_frame = tk.Frame(app, bg="#222831")
header_frame.pack(pady=10)

tk.Label(
    header_frame, 
    text="Face 🎲", 
    font=("Helvetica", 14, "bold"), 
    bg="#222831", 
    fg="#f05454"
).grid(row=0, column=0, padx=50)
tk.Label(
    header_frame, 
    text="Frequência 📊", 
    font=("Helvetica", 14, "bold"), 
    bg="#222831", 
    fg="#f05454"
).grid(row=0, column=1, padx=50)

# Resultados
results_frame = tk.Frame(app, bg="#222831")
results_frame.pack()

results_labels = []
for i in range(6):
    tk.Label(
        results_frame, 
        text=f"🎲 {i + 1}", 
        font=("Helvetica", 12, "bold"), 
        bg="#222831", 
        fg="#00adb5"
    ).grid(row=i, column=0, padx=20, pady=5)
    label = tk.Label(
        results_frame, 
        text="0", 
        font=("Helvetica", 12), 
        bg="#393e46", 
        fg="#eeeeee", 
        width=15, 
        relief="solid"
    )
    label.grid(row=i, column=1, padx=20, pady=5)
    results_labels.append(label)

# Botão de simulação
simulate_button = tk.Button(
    app, 
    text="Simular 6.000.000 Lançamentos 🚀", 
    command=roll_die_simulation,
    font=("Arial",14,"bold"),
    bg = "Indigo",
    fg = "Yellow"
)
simulate_button.pack(pady=20)

# Loop principal da interface
app.mainloop()
