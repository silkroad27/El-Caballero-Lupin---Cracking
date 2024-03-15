import os
import codecs



home = print ('=========================MundoLupin==========================' )
home2 = print ('-------------------------------------------------------------' )
home3 = print ('¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦El Caballero Ladron¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦' )
home4 = print ('-------------------------------------------------------------' )
home45 = print ('¦¦¦¦¦¦¦¦¦¦¦¦¦¦Version: 1.1 | Author: @Sr_Lupin¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦' )
home4 = print ('-------------------------------------------------------------' )
palabra_elegida = input('[1] ¿Que buscamos hoy?: ')
home6 = print ('-------------------------------------------------------------' )
home6 = print ('ejemplo de ruta (c:/users/mipc/desktop/nueva carpeta)' ), print ('-------------------------------------------------------------' )
ruta = input('[2] Ruta para leer: ')
home7 = print ('-------------------------------------------------------------' )
home8 = print ('////////////////////buscando////////////////////' )
contenido = os.listdir(ruta)
found = False

with open("Accesos Filtrados @MundoLupin.txt", "w", encoding='utf-8') as output_file:
    for archivo in contenido:
        if archivo.endswith(".txt"):
            file_path = os.path.join(ruta, archivo)
            with codecs.open(file_path, mode='r', encoding='utf-8', errors='replace') as prueba:
                inside_block = False
                url = ""
                lines_to_print = 0

                for linea in prueba:
                    if linea.startswith("Host:") or linea.startswith("URL:") or linea.startswith("http://") or linea.startswith("https://"):
                        inside_block = palabra_elegida.lower() in linea.lower()
                        if inside_block:
                            url = linea.strip()

                            print("Enlace:", url)
                            #print("Ruta del archivo:", file_path)
                            found = True
                            lines_to_print = 3
                            output_file.write(f"Enlace: {url}\n")
                            #output_file.write(f"Ruta del archivo: {file_path}\n")
                        continue

                    if inside_block:
                        print(linea.strip())
                        lines_to_print -= 1
                        output_file.write(linea)
                        if lines_to_print == 0:
                            inside_block = False

    if not found:
        print("No se encontró el enlace solicitado.")
        output_file.write("No se encontró el enlace solicitado.\n")