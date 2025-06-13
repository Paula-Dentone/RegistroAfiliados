import random

afiliados = []

while True:
    print("\n===== ISAPRE VIDA Y SALUD - MENÚ PRINCIPAL =====")
    print("1. Grabar afiliado")
    print("2. Buscar afiliado por RUT")
    print("3. Imprimir certificados")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n--- GRABAR NUEVO AFILIADO ---")
        try:
            rut = input("Ingrese RUT (sin puntos y con guion): ")
            if len(rut) < 8:
                raise ValueError("RUT muy corto")
            if "-" in rut:
                posicion_guion = rut.index("-")
            else:
                raise ValueError("RUT debe contener guion")

            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido paterno: ")
            edad = int(input("Ingrese edad (debe ser mayor a 18): "))
            if edad <= 18:
                raise ValueError("Edad debe ser mayor a 18")

            estado_civil = input("Ingrese estado civil (C: Casado, S: Soltero, V: Viudo): ").upper()
            if estado_civil != "C" and estado_civil != "S" and estado_civil != "V":
                raise ValueError("Estado civil no válido")

            genero = input("Ingrese género (M/F): ").upper()
            if genero != "M" and genero != "F":
                raise ValueError("Género no válido")

            fecha_afiliacion = input("Ingrese fecha de afiliación (dd/mm/aaaa): ")

            persona = {
                "rut": rut,
                "nombre": nombre,
                "apellido": apellido,
                "edad": edad,
                "estado_civil": estado_civil,
                "genero": genero,
                "fecha_afiliacion": fecha_afiliacion
            }

            afiliados.append(persona)
            print("Afiliado registrado correctamente.")

        except ValueError as error_dato:
            print("Hubo un problema con los datos:", error_dato)
        except Exception as error_general:
            print("Algo salió mal durante el registro:", error_general)

    elif opcion == "2":
        print("\n--- BUSCAR AFILIADO ---")
        rut_buscar = input("Ingrese el RUT a buscar: ")
        encontrado = False
        for persona in afiliados:
            if persona["rut"] == rut_buscar:
                print("Datos del afiliado:")
                print("RUT:", persona["rut"])
                print("Nombre:", persona["nombre"])
                print("Apellido:", persona["apellido"])
                print("Edad:", persona["edad"])
                print("Estado Civil:", persona["estado_civil"])
                print("Género:", persona["genero"])
                print("Fecha de afiliación:", persona["fecha_afiliacion"])
                encontrado = True
                break
        if encontrado == False:
            print("Afiliado no encontrado.")

    elif opcion == "3":
        print("\n--- IMPRIMIR CERTIFICADOS ---")
        rut_cert = input("Ingrese el RUT del afiliado: ")
        encontrado = False
        for persona in afiliados:
            if persona["rut"] == rut_cert:
                valor = random.randint(1000, 1500)
                print("==== CERTIFICADO DE AFILIACIÓN ====")
                print("Nombre del certificado: Certificado de Afiliación a la Isapre Vida y Salud")
                print("Nombre del afiliado:", persona["nombre"])
                print("RUT:", persona["rut"])
                print("Apellido:", persona["apellido"])
                print("Edad:", persona["edad"])
                print("Estado Civil:", persona["estado_civil"])
                print("Género:", persona["genero"])
                print("Fecha de afiliación:", persona["fecha_afiliacion"])
                print("Valor del certificado: $" + str(valor))
                encontrado = True
                break
        if encontrado == False:
            print("Afiliado no encontrado para emitir certificado.")

    elif opcion == "4":
        print("\nGracias por usar el sistema.")
        print("Programa desarrollado por: Paula Dentone")
        print("Versión: 1.0")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
