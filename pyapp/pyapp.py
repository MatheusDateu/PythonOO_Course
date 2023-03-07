class pyapp:
    pass

print("Testando o projeto")

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("Joao", "114444-2222")

conta = Conta(c1.nome, 6565, 0)

print(conta.titular, " Numero: ", conta.numero, " Seu saldo: ", conta.saldo)
