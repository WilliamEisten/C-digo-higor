import tkinter as tk
from tkinter import messagebox
import random

def is_prime(num):
    """Função para verificar se um número é primo."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sortear_numero():
    """Função para sortear um número primo entre 1 e 100."""
    while True:
        numero = random.randint(1, 100)
        if is_prime(numero):
            break
    messagebox.showinfo("Número Sorteado", f"O número primo sorteado é: {numero}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Sorteio de Número Primo")

label = tk.Label(root, text="Clique no botão para sortear um número primo entre 1 e 100")
label.pack(pady=20)

botao = tk.Button(root, text="Sortear", command=sortear_numero)
botao.pack(pady=10)

root.mainloop()
