import os
from rich.console import Console
from rich.prompt import Prompt
from rich.progress import Progress
import time
import shutil

console = Console()

def opcoes():
    console.print("[1] Desvincular rockstar")
    console.print("[2] Limpar Cache Fivem")
    console.rule("[bold blue]Escolha")
    opcao = Prompt.ask("[>]")

    if opcao == "1":
        os.system("cls")
        with console.status("[green] Limpando conta rockstar"):
            time.sleep(5)
            caminho_pasta = os.path.join(os.environ['USERPROFILE'],'AppData','Local','DigitalEntitlements')
            try:
                shutil.rmtree(caminho_pasta)
                console.print("[!] Conta rockstar [blink]desvinculada[/]", style="b green")
            except FileNotFoundError:
                console.print(f'[!] Não há conta rockstar [blink]vinculada[/]', style="b red")
            except Exception as e:
                console.print(f'Ocorreu um erro ao [blink]desvincular[/] sua conta', style="b blue")
        time.sleep(5)
        os.system("cls")
        os._exit(1)
    elif opcao == "2":
        os.system("cls")
        with console.status("[blue]Limpando cache do fivem[/]"):
            time.sleep(5)
            cacheFivem = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'FiveM', 'FiveM.app', 'data')
            naoApagar = "game-storage"
            try:
                subdiretorios = [subdir for subdir in os.listdir(cacheFivem) if os.path.isdir(os.path.join(cacheFivem, subdir))]
                for subdiretorio in subdiretorios:
                    if subdiretorio != naoApagar:
                        caminho_completo = os.path.join(cacheFivem, subdiretorio)
                        shutil.rmtree(caminho_completo)
                        console.print(f"[!] Limpeza de cache feita com sucesso!", style="b green")
                    else:
                        console.print("[-] Não há cache para ser limpo!", style="b red")
                        time.sleep(2)
                        os._exit(1)
            except Exception as e:
                console.print("[-] Erro ao limpar o cache", style="b red")
                time.sleep(2)
                opcoes()
    else:
        console.print("[-] Escolha uma opção válida!", style="b red")
        time.sleep(2)
        os.system("cls")
        opcoes()

opcoes()
        