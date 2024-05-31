votos=0
candidato1_votos=0
candidato2_votos=0
candidato3_votos=0
for votos in range(1,2500000):
    voto =int(input("Ingrese numero de candidato que elija : "))
    if voto == 1: 
        candidato1_votos +=1
    elif voto == 2:
        candidato2_votos +=1
    elif voto == 3:
        candidato3_votos+=1
if candidato1_votos > candidato2_votos and candidato1_votos > candidato3_votos:
    print("El ganador es el candidato 1")
elif candidato2_votos > candidato1_votos and candidato2_votos > candidato3_votos:
    print("El ganador es el candidato 2")
elif candidato3_votos > candidato1_votos and candidato3_votos > candidato2_votos:
    print("El ganador es el candidato 3")
print(f"Numero de votos para el candidato 1: {candidato1_votos},numero de votos para el candidato 2:{candidato2_votos},numero de votos para el candidato 3 :{candidato3_votos}" )
      

