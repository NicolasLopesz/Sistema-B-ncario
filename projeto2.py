from operacoes.banco import Banco
from ultilitarios.exceptions import SaldoInsuficienteError, ContaInexistenteError
 
def menu_principal():
     
    print('\n--- Sistema de Baco Virtual --- \n')
    print('1. Adcionar Cliente')
    print('2. Criar Conta')
    print('3. Acessar Conta')
    print('4. sair')
    
    return input('Ecolha uma opção:')

def menu_conta(banco):
    
    try: 
        
        num_conta = int(input('Digite o numero da conta: '))
        conta = banco.buscar_conta(num_conta)
        
        while True:
            
            print(f'--- Operações para a Conta N{conta._numero} ---')
            print(f'Cliente: {conta._cliente.nome} | Saldo: {conta._saldo:.2f}')
            print('1. Depositar')
            print('2. Sacar')
            print('3. Ver Extrato')
            print('4. Voltar ao Menu Principal')
            
            opcao = input('Escolha um das opções:')
            
            if opcao == '1':
                
                valor = float(input('Digite uma valor para depositar:'))
                conta.depositar(valor)
            
            elif opcao == '2':
                
                try:
                    
                    valor = float(input('Digite um valor para sacar:'))
                    conta.sacar(valor)
                    
                except SaldoInsuficienteError as e:
                    print(f'Erro na operação {e}') 
            
            elif opcao == '3':
                
                conta.extrato()
            
            elif opcao == '4':
                
                break
            
            else:
                
                print('Opção inválida!')
        
    
    except ContaInexistenteError as e:
        print(f'Erro: {e}')
    
    except ValueError:
        print('Erro: Entrada inválida. Por favor, digite um número.')
    
def main():
    
    banco = Banco('Banco Digital NS')
    
    while True:
        
        opcao = menu_principal()
        
        if opcao == '1':
            
            nome = input('Digite o nome do cliente:')
            cpf = input('Digite o cpf do cliente:')
            banco.adcionar_clientes(nome, cpf)
        
        elif opcao == '2':
            
            cpf = input('Digite o CPF do cliente para vincular a conta: ')
            cliente = banco._clientes.get(cpf)
            
            if cliente:
                
                tipo = input('Digite o tipo de conta (corrente/poupanca)')
                banco.criar_conta(cliente, tipo)
            
            else:
                print('Cliente não encontrado. Cadastre o cliente primeiro.')
        
        elif opcao == '3':
            menu_conta(banco)
        
        elif opcao == '4':
            print('\nObrigado por usar o nosso sistema! Até logo.\n')
            break
            
        else:
            print('\n Opção inválida. Por favor, tente novamente. \n')

if __name__ == '__main__':
    main()
            
            
