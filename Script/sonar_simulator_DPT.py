import serial
import math
import datetime
import time

def generate_nmea_dpt(depth):
    # Génère une phrase NMEA DPT avec la profondeur spécifiée
    return checksum(f"$SDDPT,{depth:.1f},M,0.1,100")

def checksum(sentence):
    # Calcule le checksum NMEA
    checksum_value = 0
    for char in sentence:
        checksum_value ^= ord(char)
    return f'{sentence}*{hex(checksum_value)[2:].upper().zfill(2)}'

def main(serial_port, baud_rate):
    try:
        ser = serial.Serial(serial_port, baud_rate, timeout=1)
        print(f"Connecté au port série {serial_port} à {baud_rate} baud.")

        while True:
            # Génération de la valeur de profondeur en sinusoidale entre 10m et 60m
            current_time = datetime.datetime.now()
            depth = 10 + int(current_time.strftime('%S'))
            
            # Envoi de la phrase NMEA DPT sur le port série
            nmea_sentence = generate_nmea_dpt(depth)
            ser.write((nmea_sentence + '\r\n').encode())
            print(nmea_sentence)

            time.sleep(1)  # Attendez une seconde avant de générer la prochaine valeur de profondeur

    except KeyboardInterrupt:
        print("Arrêt du script.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
    finally:
        ser.close()

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Utilisation : python nmea_generator.py <port_serie> <vitesse>")
        sys.exit(1)

    serial_port = sys.argv[1]
    baud_rate = int(sys.argv[2])

    main(serial_port, baud_rate)

