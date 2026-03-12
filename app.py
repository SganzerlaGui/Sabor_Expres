import os

# A variável 'restaurantes' é uma lista de dicionários.
# Cada dicionário representa um restaurante, com as chaves: 'nome', 'categoria' e 'ativo'.
# Isso permite guardar vários restaurantes e acessar os dados de cada um facilmente.

restaurantes = [{'nome': 'Praça', 'categoria': 'brasileira', 'ativo': False}, 
               {'nome': 'sushi place', 'categoria': 'japonesa', 'ativo': True},
               {'nome': 'pasta fresca', 'categoria': 'italiana', 'ativo': False}]
 

# As funções (def) dividem o programa em tarefas: cadastrar, listar, ativar/desativar restaurante, finalizar, etc.
# O menu chama cada função conforme a escolha do usuário.
# Os dados dos restaurantes ficam numa lista de dicionários.
# Funções auxiliares ajudam na navegação e apresentação.



def exibir_nome_do_programa():
     print('''S̲a̲b̲o̲r̲ e̲x̲p̲r̲e̲s̲s̲
          ''')


def exibir_opcoes():
    print('1. Cadastrar restaurate')
    print('2. listar restaurante')
    print('3. ativar/desativar restautante')
    print('4. Sair\n')


def finalizar_app():
# def é uma function no python   
     exibir_subtitulo('Finalizando o app...')
     print() 


def voltar_ao_menu_principal():
     input('Aperte ENTER para voltar ao meu principal\n')
     main()


def opcao_invalida():
     print('Opção inválida!\n')
     voltar_ao_menu_principal()


def exibir_subtitulo(texto):
     os.system('cls')
     linha = '*' * (len(texto) + 1)
     print(linha)
     print(texto)
     print(linha)
     print()


# Cada função tem:
# - inputs: dados que ela recebe (exemplo: nome e categoria do restaurante, digitados pelo usuário)
# - outputs: resultado ou efeito (exemplo: adiciona restaurante à lista, mostra mensagem na tela)
# Isso ajuda a entender o que informar e o que esperar de cada função, facilitando manutenção e uso.


def cadastrar_novo_restaurante():
     '''Essa função é responsável por cadastrar um novo restaurante

     inputs:
     -nome do restaurante
     - categoria

     outputs:
     -adiciona um novo restaurante na lista de restaurantes
     
     '''

     exibir_subtitulo('Cadastro de novos restaurantes')
     nome_do_restaurante = input('Digite o nome do seu restaurante para ser cadastrado: ')
     categoria = input(f'Digite a categoria do seu restaurante {nome_do_restaurante}: ')
     dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo': False}
     restaurantes.append(dados_do_restaurante)
     print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
     voltar_ao_menu_principal()


def listar_restaurantes():
     exibir_subtitulo('Listagem de restaurantes cadastrados')

     print(f'{'nome_restaurante'.ljust(22)} | {'categoria'.ljust(20)} | estatus')
     for restaurante in restaurantes:
          nome_restaurante = restaurante['nome']
          categoria = restaurante['categoria']
          ativo = 'ativado' if restaurante['ativo'] else 'desativado'
  # O for é uma estrutura de repetição utilizada para iterar sobre uma sequência de elementos.        
          print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

          
     voltar_ao_menu_principal()    



def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    voltar_ao_menu_principal()


def escolher_opcao():
     
     try:

          opcao_escolhida = int(input('Escolha uma opção: '))
          # apcao_escolhida = int(opcao_escolhida)

          if opcao_escolhida == 1:
               cadastrar_novo_restaurante()
          
          elif opcao_escolhida == 2:
               listar_restaurantes() 
          
          elif opcao_escolhida == 3:
               alternar_estado_restaurante()
          
          elif opcao_escolhida == 4:
               finalizar_app()
          
          else:
               opcao_invalida()
     
     except: 
          opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
     main()


