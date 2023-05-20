produto = float(input('Coloque o preço do seu produto para ver o seu desconto : R$'))

preço =  produto - (produto * 5 / 100)

print('O produto que custava R${}, na promção com desconto de 5% vai custar R${}'.format(produto, preço))
