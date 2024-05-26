leche = 1000
unidades = int(input("Ingrese cuántas unidades va a comprar: "))
jubilado = str(input("Ingrese si es jubilado s/n: "))

def desc_diez():
    descuento = unidades * leche * 0.10
    total = (unidades * leche) - descuento
    return total

def desc_quince():
    descuento = unidades * leche * 0.15
    total = (unidades * leche) - descuento
    return total

def desc_jubliado(total):
    descuento = total * 0.10
    total2 = total - descuento
    return total2


if unidades > 12 and unidades <= 24:
    total = desc_diez()
    print(f"Tiene un descuento del 10%. Total: ${total} ")
elif unidades > 24:
    total = desc_quince()
    print(f"Tiene un descuento del 15%. Total: ${total}")
else:
    total = unidades * leche
    print(f"El total es: ${total}")

if jubilado == "s":
    costo = desc_jubliado(total)
    print(f"Aplicando descuento de jubilado. El total es: ${costo}")