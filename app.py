import os

restaurantes = [
    {'nome':'Praca', 'categoria':'Japonesa', 'ativo':False},
    {'nome':'Pizza Suprema', 'categoria':'Italiana', 'ativo':True},
    {'nome':'Bacalhao a Bras', 'categoria':'Brasileira', 'ativo':False},
 ]

def exibir_nome_do_programa():

    print(""""      
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restauranteSabor Express')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizar App')  

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltaer ao menu principal') 
    main()

def exibir_subtitulo(texto):
    os.system('cls')      
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)

def opcao_invalida():
    print('Opção inválida!\n')   

def cadastrar_novo_restaurante():
    ''' Essa funcao e responsavel por cadastrar um novo restaurante 
    
    Inputs: 
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')   
    nome_do_restaurante = input('Digite o nome do restaurante ') 
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ') 
    dados_do_restaurante = {'nome': nome_do_restaurante,'categoria':categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi adicionado com successo!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando novos restaurantes')   

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()  

def alternar_estado_restaurante():
    exibir_subtitulo("Alterando o estado do restautante")
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ') 
    resturante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            resturante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso ' \
            if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not resturante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()                
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                print('Finalizar app')
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()