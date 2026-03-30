class SaldoInsuficienteError(Exception):
    
    def __init__(self, saldo_atual, valor_saque, mensagem='Saldo insuficiente para realizar o saque.'):
        
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
        self.mensagem = f'{mensagem} Saldo atual: R${saldo_atual:.2f}, Tentativa de saque: R${valor_saque:.2f}'
        
        super().__init__(self.mensagem)
        
        
        