from entidades.cliente import Cliente
from entidades.conta import Conta, ContaCorrente, ContaPoupanca
from ultilitarios.exceptions import ContaInexistenteError

class Banco:
    
    def __init__(self, nome:str):
        
        self.nome = nome
        
        self._clientes = {}
        
        self._contas = {}
        
    def adcionar_clientes(self, nome:str, cpf:str) -> Cliente:
        
        if cpf in self._clientes:
            print('Erro: Cliente com este CPF ja cadastrado.')
            return self._clientes[cpf]

        novo_cliente = Cliente(nome, cpf)
        self._clientes[cpf] = novo_cliente
        
        print(f'Cliente {nome} adcionando com sucesso!')
        
    def criar_conta(self, cliente: Cliente, tipo: str) -> Conta:
        
        numero_conta = Conta.get_total_contas() + 1 
        
        if tipo.lower() == 'corrente':
            nova_conta = ContaCorrente(numero_conta, cliente)
        elif tipo.lower() == 'poupança':
            nova_conta = ContaPoupanca(numero_conta, cliente)
        else:
            
            print('Tipo de conta inválido!')
            return None

        self._contas[numero_conta] = nova_conta
        
        cliente.adcionar_conta(nova_conta)
        print(f'Conta{tipo} n {numero_conta} criada para o cliente {cliente.nome}')
        
        return nova_conta
    
    def buscar_conta(self, numero_conta: int) -> Conta:
        conta = self._contas.get(numero_conta)
        
        if not conta:
            raise ContaInexistenteError(numero_conta)
        return conta