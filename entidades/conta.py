from abc import ABC, abstractmethod
from datetime import datetime
from ultilitarios.exceptions import SaldoInsuficienteError

class Conta(ABC):

    _total_contas = 0

    def __init__(self, numero: int, cliente):
        
        self._numero = numero
        
        self._saldo = 0.0
        
        self._cliente = cliente
        
        self._historico = []
        
        Conta._total_contas += 1 
    
    @property
    def Saldo(self):
        return self._saldo
    
    @classmethod
    def get_total_contas(cls):
        
        return cls._total_contas

    def depositar(self, valor: float):
        
        if valor > 0:
            
            self._saldo += valor
            
            self._historico.append((datetime.now(), f'Depósito ed R$:{valor:.2f}'))
            print(f'Depósito de R${valor:.2f} realizado com sucesso')
        else:
            print('Valor de depósito inválido!')
        
    @abstractmethod
    def sacar(self, valor: float):
        pass
    
    def extrato(self):
        
        print(f'\n--- Extrato da Conta numero: {self._numero} ---')
        print(f'Cliente: {self._cliente}')
        print(f'Saldo atua: R${self._saldo}')
        print(f'Histórico de Transações:')
        
        if not self._historico:
            print('Nenhum histórico foi salvo.')

        for data, transacao in self._historico:
            print(f' - {data.strftime('%d/%m/%Y %H:%M:$S')}: {transacao}')
            
        print('--------------------------------------\n')
        
class ContaCorrente(Conta):
    
    def __init__(self, numero: int, cliente, limite: float = 500.00):
        super().__init__(numero, cliente)
        
        self.limite = limite
        
    def sacar(self, valor: float):
        
        if valor <= 0:
            print('Valor de saque inválido')
            return

        saldo_disponivel = self._saldo + self.limite
        
        if valor > saldo_disponivel:
            raise SaldoInsuficienteError(saldo_disponivel, valor, 'Saldo e limites insuficientes.')

        self._saldo -= valor
        
        self._historico.append((datetime.now(), f'Saque de R$: {valor:2f}'))
        print(f'Saque de R${valor:.2f} realizado com sucesso.')
        
class ContaPoupanca(Conta):
    
    def __init__(self, numero: int, cliente):
        super().__init__(numero, cliente)
        
    def sacar(self, valor: float):
        
        if valor <= 0:
            print('Valor de saque invalido.')
            return

        if valor > self._saldo:
            raise SaldoInsuficienteError(self._saldo, valor)
        
        self.saldo -= valor
        
        self._historico.append((datetime.now(), f'Saque no valor de: R${valor:.2f}'))
        print(f'O saque no valor de {valor:.2f} foi realizado com sucesso.')
        
        