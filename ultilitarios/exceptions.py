class SaldoInsuficienteError(Exception):
    
    def __init__(self, saldo_atual, valor_saque, mensagem="Saldo insuficiente para realizar o saque."):
        self.saldo_atual = saldo_atual
        self.valor_sauqe = valor_saque
        self.mensagem = f"{mensagem} Saldo atual: R${saldo_atual}, Tentativa de saque: R${valor_saque:.2f}"
        
        super().__init__(self.mensagem)
    
class ContaInexistenteError(Exception):
    
    def __init__(self, numero_conta, mensagem='A conta que busca não existe'):
        self.numero_conta = numero_conta
        self.mensagem = f'{mensagem} Numero_conta: {numero_conta}'
        
                
        super().__init__(self.mensagem)