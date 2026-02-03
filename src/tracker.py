import requests
import os
import sys
import re
from datetime import datetime
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# Colores
BLUE = '\033[34m'
GREEN = '\033[32m'
RED = '\033[31m'
YELLOW = '\033[33m'
RESET = '\033[0m'
BOLD = '\033[1m'

def limpiar_pantalla():
    """Limpia la pantalla de forma multiplataforma"""
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    """Muestra el banner de la aplicación"""
    print("")
    print(f"{BLUE} ._____________        ___________                     __                  {RESET}")
    print(f"{BLUE} |   \\______   \\       \\__    ___/___________    ____ |  | __ ___________  {RESET}")
    print(f"{BLUE} |   ||     ___/  ______ |    |  \\_  __ \\__  \\ _/ ___|  |/ // __ \\_  __ \\ {RESET}")
    print(f"{BLUE} |   ||    |     /_____/ |    |   |  | \\// __ \\\\  \\___|    <\\  ___/|  | \\/ {RESET}")
    print(f"{BLUE} |___||____|             |____|   |__|  (____  /\\___  >__|_ \\\\___  >__|    {RESET}")
    print(f"{BLUE}                                             \\/     \\/     \\/    \\/        {RESET}")
    print("")

def crear_carpeta_resultados():
    """Crea carpeta para guardar resultados"""
    carpeta = "Resultados_Tracker"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    return carpeta

def validar_ip(ip):
    """Valida formato de dirección IP"""
    patron = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(patron, ip):
        octetos = ip.split('.')
        return all(0 <= int(octeto) <= 255 for octeto in octetos)
    return False

def validar_telefono(numero_completo):
    """Valida formato de número de teléfono"""
    try:
        phone_obj = phonenumbers.parse(numero_completo)
        return phonenumbers.is_valid_number(phone_obj)
    except:
        return False

def pausar():
    """Pausa para que el usuario pueda leer los resultados"""
    input(f"\n{BOLD}[Presiona ENTER para continuar...]{RESET}")

def geolocalizar_ip_metodo1(ip_address):
    """Método 1: Usando ip-api.com (gratuito, sin límite estricto)"""
    print(f"\n{YELLOW}[*]{RESET} Consultando ip-api.com...")
    
    try:
        url = f'http://ip-api.com/json/{ip_address}'
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('status') == 'fail':
                print(f"{RED}[!]{RESET} Error: {data.get('message', 'IP inválida o privada')}")
                return None
            
            # Crear timestamp para el archivo
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            carpeta = crear_carpeta_resultados()
            nombre_archivo = os.path.join(carpeta, f"IP_{ip_address}_{timestamp}.txt")
            
            # Guardar resultados
            with open(nombre_archivo, "w", encoding="utf-8") as file:
                file.write("="*60 + "\n")
                file.write("INFORMACIÓN DE GEOLOCALIZACIÓN IP - MÉTODO 1\n")
                file.write("="*60 + "\n\n")
                file.write(f"Fecha de consulta: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"IP: {data.get('query', 'N/A')}\n")
                file.write(f"País: {data.get('country', 'N/A')}\n")
                file.write(f"Código de país: {data.get('countryCode', 'N/A')}\n")
                file.write(f"Región: {data.get('regionName', 'N/A')}\n")
                file.write(f"Ciudad: {data.get('city', 'N/A')}\n")
                file.write(f"Código postal: {data.get('zip', 'N/A')}\n")
                file.write(f"Latitud: {data.get('lat', 'N/A')}\n")
                file.write(f"Longitud: {data.get('lon', 'N/A')}\n")
                file.write(f"Zona horaria: {data.get('timezone', 'N/A')}\n")
                file.write(f"ISP: {data.get('isp', 'N/A')}\n")
                file.write(f"Organización: {data.get('org', 'N/A')}\n")
                file.write(f"AS: {data.get('as', 'N/A')}\n")
                file.write(f"\nGoogle Maps: https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}\n")
            
            # Mostrar resultados en pantalla
            print("\n" + "="*60)
            print("RESULTADOS DE GEOLOCALIZACIÓN")
            print("="*60)
            print(f"{BOLD}IP:{RESET} {data.get('query', 'N/A')}")
            print(f"{BOLD}País:{RESET} {data.get('country', 'N/A')} ({data.get('countryCode', 'N/A')})")
            print(f"{BOLD}Región:{RESET} {data.get('regionName', 'N/A')}")
            print(f"{BOLD}Ciudad:{RESET} {data.get('city', 'N/A')}")
            print(f"{BOLD}Código postal:{RESET} {data.get('zip', 'N/A')}")
            print(f"{BOLD}Coordenadas:{RESET} {data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}")
            print(f"{BOLD}Zona horaria:{RESET} {data.get('timezone', 'N/A')}")
            print(f"{BOLD}ISP:{RESET} {data.get('isp', 'N/A')}")
            print(f"{BOLD}Organización:{RESET} {data.get('org', 'N/A')}")
            print(f"\n{GREEN}[✓]{RESET} Resultados guardados en: {nombre_archivo}")
            print(f"{GREEN}[✓]{RESET} Ver en Google Maps: https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}")
            
            return data
        else:
            print(f"{RED}[!]{RESET} Error: Status code {response.status_code}")
            return None
            
    except requests.exceptions.Timeout:
        print(f"{RED}[!]{RESET} Error: Tiempo de espera agotado")
        return None
    except requests.exceptions.ConnectionError:
        print(f"{RED}[!]{RESET} Error: No se pudo conectar al servidor")
        return None
    except Exception as e:
        print(f"{RED}[!]{RESET} Error: {e}")
        return None

def geolocalizar_ip_metodo2(ip_address):
    """Método 2: Usando ipinfo.io"""
    print(f"\n{YELLOW}[*]{RESET} Consultando ipinfo.io...")
    
    try:
        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            # Verificar si hay error
            if 'error' in data:
                print(f"{RED}[!]{RESET} Error: {data.get('error', {}).get('message', 'Error desconocido')}")
                return None
            
            # Crear timestamp para el archivo
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            carpeta = crear_carpeta_resultados()
            nombre_archivo = os.path.join(carpeta, f"IP_{ip_address}_metodo2_{timestamp}.txt")
            
            # Separar coordenadas
            loc = data.get('loc', ',').split(',')
            latitude = loc[0] if len(loc) > 0 else 'N/A'
            longitude = loc[1] if len(loc) > 1 else 'N/A'
            
            # Guardar resultados
            with open(nombre_archivo, "w", encoding="utf-8") as file:
                file.write("="*60 + "\n")
                file.write("INFORMACIÓN DE GEOLOCALIZACIÓN IP - MÉTODO 2\n")
                file.write("="*60 + "\n\n")
                file.write(f"Fecha de consulta: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"IP: {data.get('ip', 'N/A')}\n")
                file.write(f"Hostname: {data.get('hostname', 'N/A')}\n")
                file.write(f"Ciudad: {data.get('city', 'N/A')}\n")
                file.write(f"Región: {data.get('region', 'N/A')}\n")
                file.write(f"País: {data.get('country', 'N/A')}\n")
                file.write(f"Código postal: {data.get('postal', 'N/A')}\n")
                file.write(f"Latitud: {latitude}\n")
                file.write(f"Longitud: {longitude}\n")
                file.write(f"Organización: {data.get('org', 'N/A')}\n")
                file.write(f"Zona horaria: {data.get('timezone', 'N/A')}\n")
                file.write(f"\nGoogle Maps: https://www.google.com/maps?q={latitude},{longitude}\n")
            
            # Mostrar resultados en pantalla
            print("\n" + "="*60)
            print("RESULTADOS DE GEOLOCALIZACIÓN")
            print("="*60)
            print(f"{BOLD}IP:{RESET} {data.get('ip', 'N/A')}")
            print(f"{BOLD}Hostname:{RESET} {data.get('hostname', 'N/A')}")
            print(f"{BOLD}Ciudad:{RESET} {data.get('city', 'N/A')}")
            print(f"{BOLD}Región:{RESET} {data.get('region', 'N/A')}")
            print(f"{BOLD}País:{RESET} {data.get('country', 'N/A')}")
            print(f"{BOLD}Código postal:{RESET} {data.get('postal', 'N/A')}")
            print(f"{BOLD}Coordenadas:{RESET} {latitude}, {longitude}")
            print(f"{BOLD}Organización:{RESET} {data.get('org', 'N/A')}")
            print(f"{BOLD}Zona horaria:{RESET} {data.get('timezone', 'N/A')}")
            print(f"\n{GREEN}[✓]{RESET} Resultados guardados en: {nombre_archivo}")
            print(f"{GREEN}[✓]{RESET} Ver en Google Maps: https://www.google.com/maps?q={latitude},{longitude}")
            
            return data
        else:
            print(f"{RED}[!]{RESET} Error: Status code {response.status_code}")
            return None
            
    except requests.exceptions.Timeout:
        print(f"{RED}[!]{RESET} Error: Tiempo de espera agotado")
        return None
    except requests.exceptions.ConnectionError:
        print(f"{RED}[!]{RESET} Error: No se pudo conectar al servidor")
        return None
    except Exception as e:
        print(f"{RED}[!]{RESET} Error: {e}")
        return None

def analizar_telefono():
    """Analiza información de número telefónico"""
    print("\n" + "="*60)
    print("ANÁLISIS DE NÚMERO TELEFÓNICO")
    print("="*60)
    
    # Solicitar información
    print(f"\n{BOLD}Ingresa el número de teléfono:{RESET}")
    print("Ejemplo: +593 99 123 4567")
    print("O ingresa por partes:")
    
    opcion = input(f"\n{BOLD}[1] Ingresar número completo con código\n[2] Ingresar por partes\nOpción: {RESET}").strip()
    
    if opcion == "1":
        numero_completo = input(f"{BOLD}Número completo (con +): {RESET}").strip()
        if not numero_completo.startswith('+'):
            numero_completo = '+' + numero_completo
    elif opcion == "2":
        codigo_pais = input(f"{BOLD}Código de país (sin +): {RESET}").strip()
        numero = input(f"{BOLD}Número: {RESET}").strip()
        numero_completo = f'+{codigo_pais}{numero}'
    else:
        print(f"{RED}[!]{RESET} Opción inválida")
        pausar()
        return
    
    try:
        print(f"\n{YELLOW}[*]{RESET} Analizando número: {numero_completo}")
        
        # Parsear número
        phone_obj = phonenumbers.parse(numero_completo)
        
        # Obtener información
        es_valido = phonenumbers.is_valid_number(phone_obj)
        es_posible = phonenumbers.is_possible_number(phone_obj)
        formato_internacional = phonenumbers.format_number(phone_obj, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formato_e164 = phonenumbers.format_number(phone_obj, phonenumbers.PhoneNumberFormat.E164)
        formato_nacional = phonenumbers.format_number(phone_obj, phonenumbers.PhoneNumberFormat.NATIONAL)
        
        # Información geográfica
        pais = geocoder.description_for_number(phone_obj, "es")
        region = geocoder.description_for_number(phone_obj, "en")
        
        # Operador
        operador = carrier.name_for_number(phone_obj, "es")
        
        # Zona horaria
        zonas_horarias = timezone.time_zones_for_number(phone_obj)
        
        # Tipo de número
        tipo_numero = phonenumbers.number_type(phone_obj)
        tipos = {
            0: "Fijo",
            1: "Móvil",
            2: "Fijo o Móvil",
            3: "Gratuito",
            4: "Tarifa Premium",
            5: "Costo Compartido",
            6: "VoIP",
            7: "Número Personal",
            8: "Pager",
            9: "UAN",
            10: "Desconocido"
        }
        tipo_str = tipos.get(tipo_numero, "Desconocido")
        
        # Crear timestamp para el archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        carpeta = crear_carpeta_resultados()
        nombre_archivo = os.path.join(carpeta, f"Telefono_{phone_obj.country_code}{phone_obj.national_number}_{timestamp}.txt")
        
        # Guardar resultados
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("="*60 + "\n")
            f.write("ANÁLISIS DE NÚMERO TELEFÓNICO\n")
            f.write("="*60 + "\n\n")
            f.write(f"Fecha de consulta: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"Número válido: {'Sí' if es_valido else 'No'}\n")
            f.write(f"Número posible: {'Sí' if es_posible else 'No'}\n\n")
            f.write(f"Formato internacional: {formato_internacional}\n")
            f.write(f"Formato E.164: {formato_e164}\n")
            f.write(f"Formato nacional: {formato_nacional}\n\n")
            f.write(f"País/Región: {pais}\n")
            f.write(f"Región (EN): {region}\n")
            f.write(f"Código de país: +{phone_obj.country_code}\n")
            f.write(f"Número nacional: {phone_obj.national_number}\n\n")
            f.write(f"Operador: {operador if operador else 'Desconocido'}\n")
            f.write(f"Tipo de número: {tipo_str}\n")
            f.write(f"Zonas horarias: {', '.join(zonas_horarias) if zonas_horarias else 'N/A'}\n")
        
        # Mostrar resultados en pantalla
        print("\n" + "="*60)
        print("RESULTADOS DEL ANÁLISIS")
        print("="*60)
        
        # Estado del número
        if es_valido:
            print(f"{GREEN}[✓]{RESET} Número válido")
        else:
            print(f"{RED}[✗]{RESET} Número no válido")
        
        if es_posible:
            print(f"{GREEN}[✓]{RESET} Número posible")
        else:
            print(f"{YELLOW}[!]{RESET} Número no posible")
        
        # Formatos
        print(f"\n{BOLD}Formatos:{RESET}")
        print(f"  Internacional: {formato_internacional}")
        print(f"  E.164: {formato_e164}")
        print(f"  Nacional: {formato_nacional}")
        
        # Información geográfica
        print(f"\n{BOLD}Ubicación:{RESET}")
        print(f"  País/Región: {pais}")
        print(f"  Código: +{phone_obj.country_code}")
        
        # Operador y tipo
        print(f"\n{BOLD}Información adicional:{RESET}")
        print(f"  Operador: {operador if operador else 'Desconocido'}")
        print(f"  Tipo: {tipo_str}")
        if zonas_horarias:
            print(f"  Zona horaria: {', '.join(zonas_horarias)}")
        
        print(f"\n{GREEN}[✓]{RESET} Resultados guardados en: {nombre_archivo}")
        
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(f"{RED}[!]{RESET} Error al parsear número: {e}")
    except Exception as e:
        print(f"{RED}[!]{RESET} Error: {e}")
    
    pausar()

def menu_ip():
    """Menú para geolocalización de IP"""
    while True:
        print("\n" + "="*60)
        print("GEOLOCALIZACIÓN DE IP")
        print("="*60)
        print("\n[1] Método 1 (ip-api.com) - Más información")
        print("[2] Método 2 (ipinfo.io) - Alternativo")
        print("[3] Comparar ambos métodos")
        print("[99] Volver al menú principal")
        
        opcion = input(f"\n{BOLD}[+] Ingrese una opción: {RESET}").strip()
        
        if opcion == "":
            print(f"{RED}[!]{RESET} Por favor ingrese una opción")
            continue
        
        if opcion in ["1", "2", "3"]:
            ip_address = input(f"\n{BOLD}Ingrese la dirección IP: {RESET}").strip()
            
            if not validar_ip(ip_address):
                print(f"{RED}[!]{RESET} Dirección IP inválida")
                pausar()
                continue
            
            if opcion == "1":
                geolocalizar_ip_metodo1(ip_address)
                pausar()
            elif opcion == "2":
                geolocalizar_ip_metodo2(ip_address)
                pausar()
            elif opcion == "3":
                geolocalizar_ip_metodo1(ip_address)
                geolocalizar_ip_metodo2(ip_address)
                pausar()
                
        elif opcion == "99":
            break
        else:
            print(f"{RED}[!]{RESET} Opción inválida")
            pausar()

def menu_principal():
    """Menú principal de la aplicación"""
    while True:
        limpiar_pantalla()
        banner()
        print("="*60)
        print("MENÚ PRINCIPAL")
        print("="*60)
        print("\n[1] Obtener geolocalización de una IP")
        print("[2] Obtener información de número de teléfono")
        print("[3] Salir")
        
        opcion = input(f"\n{BOLD}[+] Ingrese una opción: {RESET}").strip()
        
        if opcion == "":
            print(f"{RED}[!]{RESET} Por favor ingrese una opción")
            pausar()
        elif opcion == "1":
            menu_ip()
        elif opcion == "2":
            analizar_telefono()
        elif opcion == "3":
            limpiar_pantalla()
            print(f"\n{GREEN}[✓]{RESET} ¡Gracias por usar IP & Phone Tracker!\n")
            break
        else:
            print(f"{RED}[!]{RESET} Opción inválida")
            pausar()

def main():
    """Función principal"""
    try:
        crear_carpeta_resultados()
        menu_principal()
    except KeyboardInterrupt:
        limpiar_pantalla()
        print(f"\n{YELLOW}[!]{RESET} Programa interrumpido por el usuario\n")
        sys.exit(0)

if __name__ == "__main__":
    main()