# ============================================
# Projeto: Aplicativo Desktop com Webcam
# Tecnologias:
# - Tkinter
# - OpenCV
# - Pillow
# ============================================

import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import datetime
import os

# =========================
# Cria pasta para salvar fotos
# =========================
if not os.path.exists("capturas"):
    os.makedirs("capturas")

# =========================
# Janela principal
# =========================
janela = tk.Tk()
janela.title("Sistema de Captura com Webcam")
janela.geometry("900x700")
janela.configure(bg="#1e1e1e")

# =========================
# Título
# =========================
titulo = tk.Label(
    janela,
    text="Sistema de Captura com Webcam",
    font=("Arial", 22, "bold"),
    bg="#1e1e1e",
    fg="white"
)
titulo.pack(pady=10)

# =========================
# Label de status
# =========================
status = tk.Label(
    janela,
    text="Webcam iniciada.",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="#00ff88"
)
status.pack()

# =========================
# Área da webcam
# =========================
label_video = tk.Label(janela)
label_video.pack(pady=20)

# =========================
# Abre webcam
# =========================
cap = cv2.VideoCapture(0)

# =========================
# Contador de fotos
# =========================
contador = 0

# =========================
# Função atualizar vídeo
# =========================
def atualizar_video():

    ret, frame = cap.read()

    if ret:

        # Espelha imagem
        frame = cv2.flip(frame, 1)

        # Converte cores
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Converte imagem
        imagem = Image.fromarray(frame_rgb)

        # Redimensiona
        imagem = imagem.resize((700, 500))

        imagem_tk = ImageTk.PhotoImage(image=imagem)

        label_video.imgtk = imagem_tk
        label_video.configure(image=imagem_tk)

    label_video.after(10, atualizar_video)

# =========================
# Função capturar foto
# =========================
def capturar_foto():

    global contador

    ret, frame = cap.read()

    if ret:

        contador += 1

        # Nome da foto com horário
        horario = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

        nome_arquivo = f"capturas/foto_{horario}.png"

        cv2.imwrite(nome_arquivo, frame)

        # Som simples do sistema
        janela.bell()

        status.config(
            text=f"Foto salva: {nome_arquivo}",
            fg="#00ff88"
        )

        contador_label.config(
            text=f"Fotos capturadas: {contador}"
        )

# =========================
# Função sair
# =========================
def sair():

    resposta = messagebox.askyesno(
        "Sair",
        "Deseja realmente fechar o programa?"
    )

    if resposta:
        cap.release()
        janela.destroy()

# =========================
# Botão capturar
# =========================
botao_capturar = tk.Button(
    janela,
    text="Capturar Foto",
    command=capturar_foto,
    font=("Arial", 14, "bold"),
    bg="#00aa66",
    fg="white",
    width=20,
    height=2
)

botao_capturar.pack(pady=10)

# =========================
# Contador visual
# =========================
contador_label = tk.Label(
    janela,
    text="Fotos capturadas: 0",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)

contador_label.pack()

# =========================
# Botão sair
# =========================
botao_sair = tk.Button(
    janela,
    text="Fechar Programa",
    command=sair,
    font=("Arial", 12),
    bg="#aa2222",
    fg="white",
    width=20,
    height=2
)

botao_sair.pack(pady=20)

# =========================
# Inicia webcam
# =========================
atualizar_video()

# =========================
# Loop principal
# =========================
janela.mainloop()