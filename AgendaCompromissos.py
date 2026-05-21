from datetime import datetime, date
from colorama import Fore, Style
import json

try:
    with open("compromissos.json", "r") as arquivo:
        dicionario_eventos = json.load(arquivo)

except FileNotFoundError:
    dicionario_eventos = {}

def SalvarEventos():
    with open("compromissos.json", "w") as arquivo:
        json.dump(dicionario_eventos, arquivo)

def AdicionarEvento():
    global dicionario_eventos
    hoje = date.today()

    print("-"*70)
    print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}ADICIONANDO COMPROMISSOS{Style.RESET_ALL}\n")

    nome_evento = str(input("Digite o nome do compromisso: "))
    data_texto = input("Digite a data do compromisso (dd/mm/aaaa): ")
    
    pode_registrar_evento = False

    if not dicionario_eventos:
        pode_registrar_evento = True
    
    else:
        for evento, index in dicionario_eventos.items():
            if nome_evento == evento or data_texto == index:
                pode_registrar_evento = False

                break

            else:
                pode_registrar_evento = True
            
    if pode_registrar_evento == True:
        try:
            data_ = datetime.strptime(data_texto, "%d/%m/%Y").date()

            if data_ < hoje:
                print(f"{Fore.YELLOW}O compromisso já aconteceu{Style.RESET_ALL}")

            else:
                
                if pode_registrar_evento == False:
                    print(f"{Fore.RED}Esse compromisso ja foi registrado, tente novamente{Style.RESET_ALL}")
                
                else:
                    dicionario_eventos[nome_evento] = data_texto
                    SalvarEventos()

                    print(f"{Fore.GREEN}Data Registrada!{Style.RESET_ALL}")

        except ValueError:
            print(f"{Fore.RED}Data invalida{Style.RESET_ALL}")
    
    else:
        print(f"{Fore.RED}Esse compromisso ja foi registrado{Style.RESET_ALL}, tente novamente")
        
    print("\n")

    continuar_programa = input("Aperte Enter para continuar ")

    if continuar_programa == "":
        print("\n")

def VerEventos():
    global dicionario_eventos
    
    print("-"*70)
    print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}VER COMPROMISSOS{Style.RESET_ALL}\n")

    if not dicionario_eventos:
        print(f"{Fore.YELLOW}Nenhum compromisso registrado!{Style.RESET_ALL}")

    else:
        texto_all_eventos = ""

        for chave, index in dicionario_eventos.items():
            texto_all_eventos += f"{Fore.CYAN}Compromisso:{Style.RESET_ALL} {chave}, data: {index} \n"
        
        print(texto_all_eventos)
    
    continuar_programa = input("Aperte Enter para continuar ")

    if continuar_programa == "":
        print("\n")

def ExcluirEventos():
    global dicionario_eventos

    print("-"*70)
    print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}EXCLUIR COMPROMISSOS{Style.RESET_ALL}\n")

    print("Qual compromisso você quer excluir?")

    if not dicionario_eventos:
        print(f"{Fore.YELLOW}Nenhum Compromisso registrado!{Style.RESET_ALL}")

    else:
        texto_all_eventos = ""

        for chave, index in dicionario_eventos.items():
            texto_all_eventos += f"{Fore.CYAN}Compromisso:{Style.RESET_ALL} {chave}, data: {index} \n"

        print(texto_all_eventos)

        input_delete_evento = str(input("Digite o nome do compromisso para remover ou aperte Enter para cancelar: "))

        if input_delete_evento in dicionario_eventos:
            dicionario_eventos.pop(input_delete_evento)
            SalvarEventos()

            print(f"{Fore.GREEN}compromisso: {input_delete_evento} removido!{Style.RESET_ALL}")
        
        elif input_delete_evento == "":
            return None
        
        else:
            print(f"{Fore.YELLOW}Compromisso não encontrado, talvez você digitou errado{Style.RESET_ALL}")
    
    continuar_programa = input("Aperte Enter para continuar ")

    if continuar_programa == "":
        print("\n")
    

def Menu():
    global aviso_menu_interface

    texto_erro = ""
    opcoes_menu = [
        "1: Adicionar compromisso.", "2: Ver compromissos", "3: Excluir compromisso", "4: Sair"
    ]

    while True:

        print("-"*70)
        print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}=== AGENDA DE COMPROMISSOS ==={Style.RESET_ALL}\n")

        if texto_erro:
            print(f"{Fore.RED}{texto_erro}{Style.RESET_ALL}\n")

        print("Selecione uma das opções.")
        for i in opcoes_menu:
            print(i)
        
        try:
            opcao_selecionada = int(input("\nDigite uma das opções: "))
            texto_erro = ""

        except ValueError:
            texto_erro = "ERRO: Digite apenas números válidos que está nas opções."
            continue

        match opcao_selecionada:

            case 1:
                AdicionarEvento()

            case 2:
                VerEventos()

            case 3:
                ExcluirEventos()
            
            case 4:
                print(f"{Fore.CYAN}Saindo do programa...\n{Style.RESET_ALL}")
                break

            case _:
                texto_erro = "Nenhuma opção encontrada, tente novamente."

Menu()