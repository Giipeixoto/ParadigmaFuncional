import tkinter as tk
from tkinter import messagebox
import random
import os

class TelaSelecaoDificuldade(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jogo de Adivinhação")
        self.geometry("400x300")
        self.configure(bg="#b2d8fd")
        self.criar_widgets()

    def criar_widgets(self):
        tk.Label(self, text="Escolha o nível de dificuldade", font=("Segoe UI", 16, "bold"), bg="#b2d8fd").pack(pady=20)
        self.dificuldade = tk.IntVar(value=1)

        dificuldade_frame = tk.Frame(self, bg="#b2d8fd")
        dificuldade_frame.pack(pady=10)

        tk.Radiobutton(dificuldade_frame, text="Fácil", variable=self.dificuldade, value=1, font=("Segoe UI", 14), bg="#b2d8fd").pack(anchor=tk.W)
        tk.Radiobutton(dificuldade_frame, text="Médio", variable=self.dificuldade, value=2, font=("Segoe UI", 14), bg="#b2d8fd").pack(anchor=tk.W)
        tk.Radiobutton(dificuldade_frame, text="Difícil", variable=self.dificuldade, value=3, font=("Segoe UI", 14), bg="#b2d8fd").pack(anchor=tk.W)

        button_frame = tk.Frame(self, bg="#b2d8fd")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Iniciar Jogo", command=self.iniciar_jogo, font=("Segoe UI", 14), bg="#4CAF50", fg="white").pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Regras", command=self.mostrar_regras, font=("Segoe UI", 14), bg="#2196F3", fg="white").pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Pontuações", command=self.exibir_pontuacoes, font=("Segoe UI", 14), bg="#FFC107", fg="black").pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Sair", command=self.sair, font=("Segoe UI", 14), bg="#F44336", fg="white").pack(side=tk.LEFT, padx=10)

    def iniciar_jogo(self):
        self.destroy()
        jogo = Jogo(self.dificuldade.get())
        jogo.mainloop()

    def mostrar_regras(self):
        regras = (
            "Regras do Jogo de Adivinhação:\n"
            "1. O computador escolhe um número entre 1 e 100.\n"
            "2. Você tem um número limitado de tentativas para adivinhar o número.\n"
            "3. A pontuação por tentativa é a seguinte:\n"
            "   - Fácil (10 tentativas): 100, 90, 80, 70, 60, 50, 40, 30, 20, 10 pontos.\n"
            "   - Médio (7 tentativas): 100, 80, 60, 40, 20, 10, 0 pontos.\n"
            "   - Difícil (5 tentativas): 100, 80, 60, 40, 20 pontos.\n"
            "4. Após cada tentativa, o jogo dirá se o número é maior ou menor.\n"
            "5. Tente acertar o número antes que suas tentativas se esgotem!"
        )
        self.exibir_janela_info("Regras", regras)

    def exibir_janela_info(self, titulo, mensagem):
        info_janela = tk.Toplevel(self)
        info_janela.title(titulo)
        info_janela.geometry("400x300")
        info_janela.configure(bg="#b2d8fd")

        tk.Label(info_janela, text=mensagem, font=("Segoe UI", 14), bg="#b2d8fd", justify=tk.LEFT).pack(pady=10)
        tk.Button(info_janela, text="Voltar", command=info_janela.destroy, font=("Segoe UI", 14), bg="#FFC107", fg="black").pack(pady=20)

    def exibir_pontuacoes(self):
        pontuacoes = self.ler_pontuacoes()
        pontuacao_janela = tk.Toplevel(self)
        pontuacao_janela.title("Pontuações")
        pontuacao_janela.geometry("400x300")
        pontuacao_janela.configure(bg="#b2d8fd")

        tk.Label(pontuacao_janela, text="Pontuações:", font=("Segoe UI", 16, "bold"), bg="#b2d8fd").pack(pady=10)

        if pontuacoes:
            for linha in pontuacoes:
                tk.Label(pontuacao_janela, text=linha.strip(), font=("Segoe UI", 14), bg="#b2d8fd").pack(anchor=tk.W, padx=10)
        else:
            tk.Label(pontuacao_janela, text="Nenhuma pontuação registrada.", font=("Segoe UI", 14), bg="#b2d8fd").pack(pady=10)

        tk.Button(pontuacao_janela, text="Voltar", command=pontuacao_janela.destroy, font=("Segoe UI", 14), bg="#FFC107", fg="black").pack(pady=20)

    def ler_pontuacoes(self):
        if not os.path.exists("pontuacao.txt"):
            return []
        with open("pontuacao.txt", "r") as f:
            return f.readlines()

    def sair(self):
        self.quit()

class Jogo(tk.Tk):
    def __init__(self, dificuldade):
        super().__init__()
        self.dificuldade = dificuldade
        self.title("Jogo de Adivinhação")
        self.geometry("500x400")
        self.configure(bg="#b2d8fd")
        self.pontuacao = 0
        self.tentativa_index = 0
        self.tentativas_por_dificuldade = {1: 10, 2: 7, 3: 5}
        self.criar_widgets()
        self.iniciar_jogo()

    def criar_widgets(self):
        self.game_info = tk.Label(self, font=("Segoe UI", 16), bg="#b2d8fd")
        self.game_info.pack(pady=20)

        self.pontuacao_label = tk.Label(self, text="Pontuação: 0", font=("Segoe UI", 14), bg="#b2d8fd")
        self.pontuacao_label.pack(pady=10)

        self.tentativa_entry = tk.Entry(self, font=("Segoe UI", 14))
        self.tentativa_entry.pack(pady=10)
        self.tentativa_entry.bind('<Return>', lambda event: self.tentar_adivinhar())

        button_frame = tk.Frame(self, bg="#b2d8fd")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Tentar", command=self.tentar_adivinhar, font=("Segoe UI", 14), bg="#4CAF50", fg="white").pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Regras", command=self.mostrar_regras, font=("Segoe UI", 14), bg="#2196F3", fg="white").pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Voltar", command=self.voltar, font=("Segoe UI", 14), bg="#FFC107", fg="black").pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Sair", command=self.sair, font=("Segoe UI", 14), bg="#F44336", fg="white").pack(side=tk.LEFT, padx=10)

    def iniciar_jogo(self):
        self.intervalo = {1: 100, 2: 500, 3: 1000}[self.dificuldade]
        self.tentativas_restantes = self.tentativas_por_dificuldade[self.dificuldade]

        # Define a pontuação com base na dificuldade
        if self.dificuldade == 1:  # Fácil
            self.pontuacoes_por_tentativa = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
        elif self.dificuldade == 2:  # Médio
            self.pontuacoes_por_tentativa = [100, 80, 60, 40, 20, 10, 0]
        elif self.dificuldade == 3:  # Difícil
            self.pontuacoes_por_tentativa = [100, 80, 60, 40, 20]

        self.numero_aleatorio = random.randint(1, self.intervalo)
        self.atualizar_info()

    def atualizar_info(self):
        self.game_info.config(text=f"Adivinhe um número entre 1 e {self.intervalo}.\nTentativas restantes: {self.tentativas_restantes}")

    def tentar_adivinhar(self):
        tentativa = self.tentativa_entry.get()
        if not tentativa.isdigit():
            messagebox.showwarning("Entrada Inválida", "Digite um número válido.")
            return

        tentativa = int(tentativa)
        if tentativa < 1 or tentativa > self.intervalo:
            messagebox.showwarning("Entrada Inválida", f"Digite um número entre 1 e {self.intervalo}.")
            return

        if tentativa < self.numero_aleatorio:
            resultado = "O número é maior!"
        elif tentativa > self.numero_aleatorio:
            resultado = "O número é menor!"
        else:
            resultado = "Parabéns! Você acertou o número!"
            self.pontuacao += self.pontuacoes_por_tentativa[self.tentativa_index]
            self.pontuacao_label.config(text=f"Pontuação: {self.pontuacao}")
            self.gravar_pontuacao()
            self.iniciar_jogo()
            messagebox.showinfo("Resultado", resultado)
            return

        # Verificações de "perto" e "longe"
        if abs(tentativa - self.numero_aleatorio) <= 5:
            resultado += " Você está bem perto!"
        elif abs(tentativa - self.numero_aleatorio) <= 10:
            resultado += " Você está perto!"
        else:
            resultado += " Você está longe!"

        self.tentativa_index += 1
        self.tentativas_restantes -= 1

        if self.tentativas_restantes <= 0:
            messagebox.showinfo("Fim de Jogo", f"Você perdeu. O número era {self.numero_aleatorio}.")
            self.iniciar_jogo()
        else:
            self.atualizar_info()
            messagebox.showinfo("Resultado", resultado)

    def gravar_pontuacao(self):
        with open("pontuacao.txt", "a") as f:
            f.write(f"Pontuação: {self.pontuacao}\n")

    def mostrar_regras(self):
        regras = (
            "Regras do Jogo de Adivinhação:\n"
            "1. O computador escolhe um número entre 1 e 100.\n"
            "2. Você tem um número limitado de tentativas para adivinhar o número.\n"
            "3. A pontuação por tentativa é a seguinte:\n"
            "   - Fácil (10 tentativas): 100, 90, 80, 70, 60, 50, 40, 30, 20, 10 pontos.\n"
            "   - Médio (7 tentativas): 100, 80, 60, 40, 20, 10, 0 pontos.\n"
            "   - Difícil (5 tentativas): 100, 80, 60, 40, 20 pontos.\n"
            "4. Após cada tentativa, o jogo dirá se o número é maior ou menor.\n"
            "5. Tente acertar o número antes que suas tentativas se esgotem!"
        )
        self.exibir_janela_info("Regras", regras)

    def exibir_janela_info(self, titulo, mensagem):
        info_janela = tk.Toplevel(self)
        info_janela.title(titulo)
        info_janela.geometry("400x300")
        info_janela.configure(bg="#b2d8fd")

        tk.Label(info_janela, text=mensagem, font=("Segoe UI", 14), bg="#b2d8fd", justify=tk.LEFT).pack(pady=10)
        tk.Button(info_janela, text="Voltar", command=info_janela.destroy, font=("Segoe UI", 14), bg="#FFC107", fg="black").pack(pady=20)

    def voltar(self):
        self.destroy()
        selecao_janela = TelaSelecaoDificuldade()
        selecao_janela.mainloop()

    def sair(self):
        self.quit()

if __name__ == "__main__":
    app = TelaSelecaoDificuldade()
    app.mainloop()
