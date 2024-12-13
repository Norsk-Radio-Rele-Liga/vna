# © Thomas S. Knutsen LA3PNA  2024
#
# English:
# This source code is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
# You are free to:
# - Share — copy and redistribute the source code in any medium or format
# - Adapt — remix, transform, and build upon the source code
# Under the following terms:
# - Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made.
#   You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
# - NonCommercial — You may not use the source code for commercial purposes.
# - ShareAlike — If you remix, transform, or build upon the source code, you must distribute your contributions under
#   the same license as the original.
# View the full license at: https://creativecommons.org/licenses/by-nc-sa/4.0/
#
# Norsk:
# Denne kildekoden er lisensiert under en Creative Commons Navngivelse-Ikkekommersiell-DelPåSammeVilkår 4.0 Internasjonal Lisens.
# Du står fritt til å:
# - Dele — kopiere, distribuere og spre kildekoden i hvilket som helst medium eller format
# - Tilpasse — remikse, endre, og bygge videre på kildekoden
# På følgende vilkår:
# - Navngivelse — Du må gi korrekt kreditering, lenke til lisensen, og indikere om endringer er gjort.
#   Dette kan gjøres på en rimelig måte, men ikke på en måte som antyder at lisensgiveren godkjenner deg eller din bruk.
# - Ikkekommersiell — Du kan ikke bruke kildekoden til kommersielle formål.
# - DelPåSammeVilkår — Hvis du remikser, endrer, eller bygger videre på kildekoden, må du distribuere dine bidrag
#   under samme lisens som originalen.
# Se hele lisensen på: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.no

import serial
import time
import matplotlib.pyplot as plt
import math

# Funksjon for å sende kommando og motta respons fra en COM-port
def send_and_receive(ser, command):
    command_with_crlf = command + "\r\n"  # Legger til CR LF (Carriage Return + Line Feed)
   # print(command)
    ser.write(command_with_crlf.encode())  # Send kommandoen
    ser.flush()  # Sørg for at alt blir sendt
    time.sleep(0.1)  # Kort delay for å sikre riktig timing
    response = ser.readlines()  # Mottar linjer fra porten
    return response

# Oppretter forbindelser til COM-portene
com6 = serial.Serial('COM6', baudrate=9600, timeout=1)
com11 = serial.Serial('COM11', baudrate=9600, timeout=1)


# Liste for å lagre S-parameterverdier i dB
s_parameter_values_db = []
dBset = []

# For loop for å sende "dB:nn.n" på COM11, motta data fra COM6 og plotte
for i in range(64):  # Fra 0.0 til 31.5 med steg på 0.5 (64 verdier)
    db_value =  31.5 - (i * 0.5)
    command = f"dB:{db_value:.1f}"
    
    # Sender dB-kommando til attenuator
    send_and_receive(com11, command)
    
    # Sender sweep-kommandoen til VNA
    send_and_receive(com6, "scan 10000000 10000000 1")

    # Sender "data 1" til VNA og mottar responsen
    response = send_and_receive(com6, "data 1")  
    
    dBset.append(db_value*-1.0)

    # Debug: Skriv ut hva vi mottar fra VNA
    print(f"Response for dB:{db_value:.1f}: {response}")

    # Behandler responsen for å finne S-parameterverdien og konvertere til dB
    if response and len(response) > 1:
        try:
            s_param_line = response[1].decode().strip()  # Henter linjen med S-parametere
            s_param_value = float(s_param_line.split()[0])  # Tar første verdi (den reelle S-parameteren)
            s_param_value_db = 20 * math.log10(abs(s_param_value))  # Konverterer til dB
            s_parameter_values_db.append(s_param_value_db)
        except (ValueError, IndexError) as e:
            print(f"Error processing response: {e}")
    else:
        print(f"No valid response for dB:{db_value:.1f}")

# Sjekk om listen er tom før plotting
if len(s_parameter_values_db) == 0:
    print("Ingen S-parameterverdier ble mottatt. Sjekk kommunikasjonen med VNA.")
else:
    # Plotter S-parameterverdiene i dB
    plt.plot(dBset, s_parameter_values_db)
    plt.xlabel("dB relative (attenuator)")
    plt.ylabel("dB measured (S21)")
    plt.title("NanoVNA linearity 10MHz")
    plt.grid(True)
    plt.show()

# Lukk serieportene
com6.close()
com11.close()
