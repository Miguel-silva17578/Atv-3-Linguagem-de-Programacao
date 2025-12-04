import tkinter as tk
from tkinter import messagebox
from database import inserir_paciente


# Função para calcular IMC
def calcular_imc():
    try:
        altura = float(entry_altura.get()) / 100  # converte cm para metros
        peso = float(entry_peso.get())
        imc = peso / (altura ** 2)

        # Criando a variável classificacao
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 24.9:
            classificacao = "Peso normal"
        elif imc < 29.9:
            classificacao = "Sobrepeso"
        elif imc < 34.9:
            classificacao = "Obesidade grau I"
        elif imc < 39.9:
            classificacao = "Obesidade grau II"
        else:
            classificacao = "Obesidade grau III"

        # Aqui montamos o texto final
        resultado = f"IMC: {imc:.2f}\nClassificação: {classificacao}"

        label_resultado.config(text=resultado)

        # 🔥 Aqui você já pode salvar no banco
        inserir_paciente(
            entry_nome.get(),
            entry_endereco.get(),
            float(entry_altura.get()),
            peso,
            imc,
            classificacao
        )

    except ValueError:
        messagebox.showerror("Erro", "Valores inválidos!")


    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para altura e peso.")
    
# Função para limpar os campos
def reiniciar():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    label_resultado.config(text="Resultado")

# Função para sair
def sair():
    janela.destroy()

# Criação da janela principal
janela = tk.Tk()
janela.title("Cálculo do IMC - Índice de Massa Corporal")
janela.geometry("640x360")


tk.Label(janela, text="Nome do Paciente:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_nome = tk.Entry(janela, width=40)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Endereço Completo:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_endereco = tk.Entry(janela, width=40)
entry_endereco.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Altura (cm):").grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_altura = tk.Entry(janela)
entry_altura.grid(row=2, column=1, sticky="w", padx=10, pady=5)

tk.Label(janela, text="Peso (Kg):").grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_peso = tk.Entry(janela)
entry_peso.grid(row=3, column=1, sticky="w", padx=10, pady=5)


label_resultado = tk.Label(janela, text="Resultado", width=50, height=5, bg="#f0f0f0", relief="sunken", anchor="w", justify="left")
label_resultado.grid(row=2, column=2, rowspan=2, padx=10, pady=5)


tk.Button(janela, text="Calcular", width=12, command=calcular_imc).grid(row=5, column=0, pady=15)
tk.Button(janela, text="Reiniciar", width=12, command=reiniciar).grid(row=5, column=1, pady=15)
tk.Button(janela, text="Sair", width=12, command=sair).grid(row=5, column=2, pady=15)

janela.mainloop()

