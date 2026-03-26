from abc import ABC, abstractmethod
from datetime import datetime
from ultilitarios.exceptions import SaldoInsuficienteError

class Conta(ABC):
    
    _total_contas = 0
    
    def __init__(self, numero: int, cliente):
        self.numero = numero
        self.saldo = 0.0
        self.cliente = cliente
        self._historico = []
        
        Conta._contas += 1
        
    @property
    def saldo(self):
        return self._saldo
    
    @classmethod
    def get_total_contas(cls):
        return cls._total_contas

    def depositar(self, valor: float):
        
        if valor > 0:
            
            self._saldo += valor
            self._historico.append((datetime.now(), f'Depósito de R${valor:.2f}'))
        else:
            print('Valor de depósito inválido!')
        
    @abstractmethod
    def sacar(self, valor:float):
        pass
    
    def extrato(self):
        
        print(f'\n--- Extrato da Conta {self.numero}')
        print(f'Cliente: {self._cliente.nome}' )
        print(f'saldo atual: R${self._saldo:.2f}')
        print(f'Histórico de Transações')
        
        if not self._historico:
            print('Não foi possivel encontar o historico')
        
        for data, transacao in self._historico:
            print(f'-{data.strftime('%d/$m/%Y %H:M%:%S')}: {transacao}')
        print("-------------------------------\n")
        
class ContaCorrente(Conta):
    
    def __init__(self, numero : int, cliente, limite: float = 500.0):
        super().__init__(numero, cliente)
        
        self.limite =limite 
    
    def sacar(self, valor:float):
        
        if valor <= 0:    
            print('Valor de saque inválido.')
            return 

      
    
        
        
            
        
    
        
    
    