venta_total=0
n_vendedores=int(input("ingrese cantidad de vendedores"))
sueldo_base=int(input("ingrese sueldo base"))
for vendedor in range(n_vendedores) :
    venta_total=0
    print(f"vendedor{vendedor +1}")
    n_ventas = int( input(f"INgrese cantidad de ventas vendedor{vendedor + 1}  :"))
    for venta in range(n_ventas):
        valor_venta = int(input(f"INgrese valor de la venta {venta+1}.."))
        venta_total = venta_total+valor_venta
    
    comision=venta_total * 0.10
    salario_total=sueldo_base + comision
    print(f"El salario total del vendedit{vendedor} es : {salario_total}")
        