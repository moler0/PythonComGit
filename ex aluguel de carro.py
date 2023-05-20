km = float(input('Quantos km foram percorridos com o carro ?'))
dia = float(input('Por quanto dias o carro foi alugado?'))

preçok = km * 0.15
preçod = dia * 60
total = preçok + preçod

print('Você devera parar po dia usado  R${}, e pagara por km rodado R${:.2f} Total a pagar sera de R${}'.format(preçod, preçok, total))
