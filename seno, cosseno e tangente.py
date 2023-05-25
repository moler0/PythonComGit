from math import radians, sin, cos, tan
angulo = float(input('Digite o valor do angulo desejado :'))

seno = sin(radians(angulo))
print('O angulo de {} tem o seno de {:.2f}'.format(angulo, seno))

cosseno = cos(radians(angulo))
print('O angulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))

tangente = tan(radians(angulo))
print('O angulo de {} tem o tangente de {:.2f}'.format(angulo, tangente))
