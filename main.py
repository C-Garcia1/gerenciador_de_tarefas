import os 
from datetime import date

def salvar_em_txt():
    with open('tarefas.txt', 'w', encoding='utf-8') as arquivo:
        for tarefa in tarefas:
            # Cada linha do arquivo terá: Nome;Data;Status
            linha = f"{tarefa['Nome']};{tarefa['Data']};{tarefa['Status']}\n"
            arquivo.write(linha)

def carregar_de_txt():
    tarefas_carregadas = []
    try:
        with open('tarefas.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                nome, data, status = linha.strip().split(';')
                tarefas_carregadas.append({
                    'Nome': nome,
                    'Data': data,
                    'Status': status == 'True'  # converte texto para booleano
                })
    except FileNotFoundError:
        pass  # se o arquivo não existir, ignora
    return tarefas_carregadas


tarefas = carregar_de_txt()

def exibir_nome_do_programa():
    print('==== GERENCIADOR DE TAREFAS === TaskMaster ===')

def exibir_menu():
    print('\n1- Cadastrar Tarefas')
    print('2- Listar Tarefas')
    print('3- Ativar Tarefas')
    print('4- Excluir Tarefas')
    print('5- Sair')

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '=' * len(texto)
    print(linha, texto, linha)

def encerrar_programa():
    exibir_subtitulo('Encerrando programa')
    exit()

def retornar_ao_menu():
    input('\nPressione ENTER para retornar ao menu')
   
def cadastrar_tarefa():
    exibir_subtitulo('Cadastrando Tarefa')
    nome_tarefa = input('Informe a tarefa que deseja cadastrar: ')
    nome_encontrado = False
    for tarefa in tarefas:
        if tarefa['Nome'] == nome_tarefa:
            nome_encontrado = True
            print('Tarefa já existente')
            return
            
    data_tarefa = date.today().strftime('%d/%m/%Y')
    status_tarefa = False
    tarefas.append({'Nome': nome_tarefa, 'Data': data_tarefa, 'Status': status_tarefa})
    salvar_em_txt()
    print(f'\nA tarefa {nome_tarefa} foi cadastrada com sucesso!')
    
    
    
def listar_tarefas():
    for tarefa in tarefas:
        nome_tarefa = tarefa['Nome']
        data_tarefa = tarefa['Data']
        status_tarefa = 'Concluida' if tarefa['Status'] else 'Não Concluida'
        print(f'\nNome: {nome_tarefa} - Data: {data_tarefa} - Status: {status_tarefa}')
    


def alterando_status_tarefa():
    exibir_subtitulo('Alterando Status')
    listar_tarefas()
    
    buscar_nome = input('\nInforme o nome da tarefa que deseja alterar o status: ')
    nome_encontrado = False
    
    for tarefa in tarefas:
        if buscar_nome == tarefa['Nome']:
            nome_encontrado = True
            tarefa['Status'] = not tarefa['Status']
            salvar_em_txt()
            mensagem = f'O status da tarefa {buscar_nome} foi alterado para Concluida!' if tarefa['Status'] else f'O status da tarefa {buscar_nome} foi alterado para NÃO Concluida!'
            print(mensagem)
        
    if not nome_encontrado:
        print('A tarefa não foi encontrada!')
      
        
def excluindo_tarefa():
    exibir_subtitulo('Excluindo Tarefa')
    listar_tarefas()
    
    buscar_nome = input('\nInforme o nome da tarefa que deseja deletar: ')
    nome_encontrado = False

    for tarefa in tarefas:
        if tarefa['Nome']  == buscar_nome:
            nome_encontrado = True
            tarefas.remove(tarefa)
            salvar_em_txt()
            print(f'\nA tarefa {buscar_nome} foi removida com sucesso!')
        
    if not nome_encontrado:
        print('A tarefa não foi encontrada!')
   
     


def escolher_opcao():
    try:
        escolha = int(input('\nInforme a opção que deseja realizar: '))
        if escolha == 1: 
            cadastrar_tarefa()
        elif escolha == 2: 
            exibir_subtitulo('Lista de Tarefas')
            listar_tarefas()
        elif escolha == 3: 
            alterando_status_tarefa()
        elif escolha == 4: 
            excluindo_tarefa()
        elif escolha == 5: 
            encerrar_programa()
        else: 
            print('Opção Inválida!!!')
    except ValueError as v: 
        print(f'Erro: {v}')
        retornar_ao_menu()
def main():
    while 1:
        os.system('cls')
        exibir_nome_do_programa()
        exibir_menu()
        escolher_opcao()
        retornar_ao_menu()

if __name__ == '__main__':
    main()