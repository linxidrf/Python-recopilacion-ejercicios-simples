estado_tienda= input( "¿La tienda esta abierta?  (si/no):")
if estado_tienda.lower() == "si":
    print("Listo para registar ventas")
    registrar_venta = input("¿Desea registrar una venta? (sí/no): ")
    while registrar_venta.lower() == "si":
        valor_sin_descuento = float(input("¿Cual es el valor de la venta ?"))
        color_balota= input("¿De que color es la balota?")
        if color_balota.lower() =="amarillo":
           descuento= valor_sin_descuento * 0.25
           valor_con_descuento=  valor_sin_descuento - descuento  
           print("El total de la compra es:",valor_con_descuento)
        elif color_balota.lower() =="rojo":
           descuento= valor_sin_descuento * 0.40
           valor_con_descuento=  valor_sin_descuento - descuento  
           print("El total de la compra es:",valor_con_descuento)
        elif color_balota.lower() =="blaco":
           print("No se aplica descuento por lo tanto el total es:",valor_sin_descuento)
        registrar_venta = input("¿Desea registrar otra venta? (sí/no): ")
    if registrar_venta.lower() == "no":
        print  ("Preparandose para cerrar tienda")
elif estado_tienda.lower() == "no":
    print("La tienda está cerrada en este momento.")
    