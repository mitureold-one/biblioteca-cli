versao_build = 3.0
data_versao = "Data Da Versão: 2024-16-10"

link = "https://github.com/mitureold-one/biblioteca-/tree/main"

outras_versoes = f"""
    Confiras versões anteriores em: {link}
"""

aviso_importante = """
Feito 100% Pela estupidez humana ! 
"""

titulo = """
    
    ██████╗░██╗██████╗░██╗░░░░░██╗░█████╗░████████╗███████╗░█████╗░░█████╗░
    ██╔══██╗██║██╔══██╗██║░░░░░██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗
    ██████╦╝██║██████╦╝██║░░░░░██║██║░░██║░░░██║░░░█████╗░░██║░░╚═╝███████║
    ██╔══██╗██║██╔══██╗██║░░░░░██║██║░░██║░░░██║░░░██╔══╝░░██║░░██╗██╔══██║
    ██████╦╝██║██████╦╝███████╗██║╚█████╔╝░░░██║░░░███████╗╚█████╔╝██║░░██║
    ╚═════╝░╚═╝╚═════╝░╚══════╝╚═╝░╚════╝░░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝

    ██╗░░░██╗██╗██████╗░████████╗██╗░░░██╗░█████╗░██╗░░░░░
    ██║░░░██║██║██╔══██╗╚══██╔══╝██║░░░██║██╔══██╗██║░░░░░
    ╚██╗░██╔╝██║██████╔╝░░░██║░░░██║░░░██║███████║██║░░░░░
    ░╚████╔╝░██║██╔══██╗░░░██║░░░██║░░░██║██╔══██║██║░░░░░
    ░░╚██╔╝░░██║██║░░██║░░░██║░░░╚██████╔╝██║░░██║███████╗
    ░░░╚═╝░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝
"""
subtitulo = f"""
    \tBem-Vindo a Nova Versão da nossa... a sua.... \"Biblioteca {versao_build}\" !
       
"""

linha = "-"*100

menu = f"""
    {linha}
    ⬧ Livros
    ⬧ Usuários
    ⬧ Empréstimos
    ⬧ Devoluções
    ⬧ sair
    {linha}
"""
Header = titulo + subtitulo
main = menu
footer = f"{data_versao}\n{outras_versoes}\n{aviso_importante}"

tela_01 = Header + main + footer

print(tela_01)

