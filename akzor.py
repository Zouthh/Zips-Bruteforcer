from colorama import Fore, Style, init
import pyzipper
init()

logo = """ 
    ><<<<<<<  ><<< <<       ><<
    ><<    >< <><< >< ><<   ><<
    ><<    >< <><< ><< ><<  ><<
    ><<<<<<<  ><<> <<  ><< ><<<
    ><<       ><<> <<   >< ><<<
    ><<       ><<> <<    >< <<<
    ><<       ><<> <<      ><<< ...zip

    1.- Descompresor Normal
    2.- Descompresor por Fuerza Bruta                         """
print(Fore.GREEN + logo)

opcion = input(">> ")

if opcion == '1':
    print("Selecciona la ruta del archivo zip (Incluye el .zip)")
    ruta = input(">> ")
    print("Selecciona la ruta de extracción (por defecto, escritorio)")
    extraccion = input(">> ")
    with pyzipper.AESZipFile(ruta, 'r', compression=pyzipper.ZIP_STORED, encryption=pyzipper.WZ_AES) as archivo_zip:
        archivo_zip.extractall(path=extraccion)
    print(Fore.GREEN + Style.DIM + "Extracción exitosa!")

elif opcion == '2':
    print("Selecciona la ruta de la lista de palabras")
    ruta_lista = input(">> ")
    with open(ruta_lista, 'r') as archivo_lista:
        print("Selecciona la ruta del archivo zip a descomprimir")
        ruta_zip = input(">> ")
        print("Selecciona la ruta donde deseas guardar los archivos extraídos (por defecto, escritorio)")
        extraccion = input(">> ")
        contraseña_encontrada = False
        for contraseña in archivo_lista:
            contraseña = contraseña.strip()
            contraseña_bytes = contraseña.encode('utf-8')
            print(contraseña)
            try:
                with pyzipper.AESZipFile(ruta_zip, 'r', compression=pyzipper.ZIP_STORED, encryption=pyzipper.WZ_AES) as archivo_zip:
                    archivo_zip.pwd = contraseña_bytes
                    archivo_zip.extractall(path=extraccion)
                contraseña_encontrada = True
                print(Fore.MAGENTA + Style.DIM + Style.BRIGHT +  f"Extracción exitosa! Contraseña: {contraseña}")
                break
            except Exception as e:
                print(f"Error: {e}")

        if not contraseña_encontrada:
            print(Fore.RED + "Contraseña no encontrada en la lista de palabras.")
