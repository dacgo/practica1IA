import sys
import string
import random
def calcularCosto():
	'Se calculan las hipotesis de todas las lineas'
	xs = open(sys.argv[1], 'r')
	ys = open(sys.argv[2], 'r')
	hipotesisTotales = 0
	'Obtengo todas las y y las pongo en un vector que va de 1 a n lineas y'
	valsy = [-1]
	for liney in ys:
		valsy.append(liney)
	ys.close()
	'Recorro el archivo de x para sacar hipotesis'
	for linex in xs:
		hipotesis=0.0
		cntx = 1
		cnty = 1
		lineax = linex.split(',')
		'Calculando las hipotesis'
		for valx in lineax:
			hipotesis = hipotesis + (float(tetasn[cntx])*float(valx))
			cntx = cntx + 1
		'Sumar la nueva hipotesis calculada con las anteriores'
		hipotesisTotales = hipotesisTotales + (hipotesis - float(valsy[cnty]))**2
		cnty = cnty+1
	'Calcular el costo'
	costo = hipotesisTotales * (1/(2*float(txs)))
	xs.close()
	return costo

def optimizarTetas(tlineax):
	'Se calculan las hipotesis de todas las lineas'	
	ys = open(sys.argv[2], 'r')
	hipotesisTotales = 0
	'Obtengo todas las y y las pongo en un vector que va de 1 a n lineas y'
	valsy = [-1]
	for liney in ys:
		valsy.append(liney)
	ys.close()
	tetasv = tetasn
	'CALCULO CADA UNA DE LAS TETAS DEL PROBLEMA'
	for i in range(1,tlineax+1):
		'Recorro el archivo de x para sacar hipotesis'
		xs = open(sys.argv[1], 'r')
		for linex in xs:
			hipotesis=0.0
			cntx = 1
			cnty = 1
			lineax = linex.split(',')
			'Calculando las hipotesis'
			for valx in lineax:
				hipotesis = hipotesis + (float(tetasn[cntx])*float(valx))
				cntx = cntx + 1
			'Sumar la nueva hipotesis calculada con las anteriores'
			tetasn[i] = tetasv[i] - (float(sys.argv[3])* ((hipotesis - float(valsy[cnty]))*float(lineax[cnty-1])))
			cnty = cnty+1
		xs.close()
'----------------------------- INICIO DEL PROGRAMA -----------------------------'
'---NUMERO DE LINEAS DEL ARCHIVO xs Y ys---'
xs = open(sys.argv[1], 'r')
ys = open(sys.argv[2], 'r')
txs = len(xs.readlines())
tys = len(ys.readlines())
xs.close()
ys.close()
'---NUMERO DE x EN LAS LINEAS---'
xs = open(sys.argv[1], 'r')
for linex in xs:
	lineax = linex.split(',')
	tlineax = len(lineax)
xs.close
tetasn = [-1]
tetasv = [-1]
'---DEFINIENDO TETAS INICIALES QUE SON ALEATORIAS, SIENDO LOS VALORES ENTRE 0 y 10---'
for i in range(1,tlineax+1):
	tetasn.append(random.randrange(11))

'REALIZAR EL NUMERO DE ITERACIONES DEFINIDAS POR EL USUARIO'
f = open('salida.csv', 'w')
for i in range(int(sys.argv[4])):
	costocalculado = calcularCosto()
	f.write(str(costocalculado)+'\n')
	'print costocalculado'
	if costocalculado < float(sys.argv[5]):
		f.write('Tolerancia alcanzada')
		break
	else:
		optimizarTetas(tlineax)
f.close()
