#Desafio 1 - Fundamentos de Python aplicado a dados  - FAST Transição
#Antonio Macena
from pathlib import Path
import pandas as pd

def menu():
    menu = '''
| Sistema de Gerenciamento de Registros de Estudantes |

    1 Adicionar um novo Registro de Estudante
    2 Exibir Registros de Estudantes
    3 Procurar por um Estudante
    4 Calcular Média das Notas
    5 Salvar Registros em Arquivo
    6 Carregar Registros do Arquivo
    7 Sair
    
    '''
    print(menu)

def valida_entrada(msg, erro = ""):
    num = input(msg)
    if num.isnumeric():
        return int(num)
    print(erro)
    return -1

def entrada_id():
    while True:
        id = valida_entrada("Digite o ID do Estudante: ", "Não é um id válido")
        if id != -1:
            break
    return id

def modelo_registro(nome = None, id = None, nota1=None, nota2=None, nota3=None):
    estudante = {
        'Nome': [nome],
        'Id': [id],
        'Nota1': [nota1],
        'Nota2': [nota2],
        'Nota3': [nota3]
    }
    return estudante

def adiciona_registro():
    nome = input("Digite o nome do Estudante: ")
    idnum = entrada_id()
    notas = input("Digite as Notas do Estudante (separadas por espaço): ")
    n1, n2, n3 = notas.split()
    return pd.DataFrame(modelo_registro(nome, idnum, float(n1), float(n2), float(n3)))


def main():
    dados_geral = pd.DataFrame(modelo_registro()).drop(0)
    
    while True:
        menu()
        opcao = input("\nDigite sua Escolha (1-7): ")
        if opcao == '1':
            temp = adiciona_registro()
            dados_geral = pd.concat([dados_geral.astype(temp.dtypes), temp ], ignore_index= True)
            
        elif opcao == '2':
           break
        elif opcao == '3':
            break
        elif opcao == '4':
            break
        elif opcao == '5':
            break
        elif opcao == '6':
            break
        elif opcao == '7':
            print("Sistema Finalizado")
            break
        else:
            print("\nEscolha Inválida\n")

if __name__ == "__main__": 
    main()