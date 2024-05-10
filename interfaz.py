from junta_dinero import JuntaDeDinero


def obtener_informacion():
    num_personas = int(
        input("Ingrese el número de personas que participarán en la junta de dinero: "))
    aporte = float(
        input("Ingrese el monto que cada persona aportará en cada mes: "))
    return num_personas, aporte


def main():
    print("Bienvenido a la junta de dinero")
    num_personas, aporte = obtener_informacion()
    junta = JuntaDeDinero(num_personas=num_personas, aporte=aporte)
    junta.ejecutar_junta()


if __name__ == "__main__":
    main()
