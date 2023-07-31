class Conta:

    def __init__(self, numero, titular, saldo, limite = 1000.0):#função construtora
        
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def obter_extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor
    
    def __poder_sacar(self, valor):
        valor_disponivel_para_sacar = self.__saldo + self.__limite
        return valor <= valor_disponivel_para_sacar
    
    def sacar(self, valor):
        if(self.__poder_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor de {} está acima do limite".format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
      
    @property   
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        
    @staticmethod  
    def mostrar_codigo_do_banco():
        return '001'
    
    @staticmethod
    def mostrar_codigos_dos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}