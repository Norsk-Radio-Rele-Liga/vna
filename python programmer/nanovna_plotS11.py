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
import numpy as np
import matplotlib.pyplot as plt
import time
import sys

# Funksjon for å konvertere normaliserte real + imaginær til Return Loss og fasevinkel
def convert_to_return_loss_and_phase(r, x):
    # Beregn reflekteringskoeffisient rho (normalisert)
    rho = np.sqrt(r**2 + x**2)
    # Beregn Return Loss (RL) i dB, og sørg for at det blir negativt
    return_loss = 20 * np.log10(rho)
    # Beregn fasevinkelen (vinkel) i grader
    phase_angle = np.degrees(np.arctan2(x, r))
    return return_loss, phase_angle

# Funksjon for å lese data fra NanoVNA
def read_data_from_nanovna(serial_port, command):
    # Send kommando for å hente data
    serial_port.write(command)
    time.sleep(0.1)
    serial_port.flush()

    # Les respons fra NanoVNA
    data = []
    while True:
        line = serial_port.readline().decode('utf-8').strip()
        if line.startswith(command.decode().strip()):
            continue  # Hopp over første linje
        if line.startswith("ch>"):
            break  # Slutt på data

        try:
            data.append(float(line))
        except ValueError:
            print(f"Ugyldig linje mottatt: {line}")
            continue
    
    return np.array(data)

# Funksjon for å lese normaliserte S11-data (r og x) fra NanoVNA
def read_s11_data(serial_port):
    # Send kommando for å hente S11-data
    serial_port.write(b"data 0\r\n")
    serial_port.flush()

    # Les respons fra NanoVNA
    data = []
    while True:
        line = serial_port.readline().decode('utf-8').strip()
        if line.startswith("data 0"):
            continue  # Hopp over første linje
        if line.startswith("ch>"):
            break  # Slutt på data

        try:
            r, x = map(float, line.split())
            data.append((r, x))
        except ValueError:
            print(f"Ugyldig linje mottatt: {line}")
            continue
    
    return np.array(data)

# Funksjon for å plotte Return Loss og fasevinkel
def plot_return_loss_and_phase(frequencies, data):
    r = data[:, 0]
    x = data[:, 1]

    # Konverter til Return Loss og fasevinkel
    return_loss, phase_angle = convert_to_return_loss_and_phase(r, x)

    # Plot Return Loss
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(frequencies, return_loss)
    plt.title("Return Loss")
    plt.ylabel("Return Loss (dB)")
    plt.xlabel("Frekvens (Hz)")
    
    # Plot fasevinkel
    plt.subplot(2, 1, 2)
    plt.plot(frequencies, phase_angle)
    plt.title("Fasevinkel")
    plt.ylabel("Vinkel (grader)")
    plt.xlabel("Frekvens (Hz)")

    plt.tight_layout()
    plt.show()

def main():
    # Sjekk om riktige antall argumenter er gitt
    if len(sys.argv) != 3:
        print("Bruk: python NanoVNA_plots11.py <start_frekvens> <slutt_frekvens>")
        return
    
    # Hent frekvenser fra kommandolinjeargumenter
    try:
        start_frekvens = int(sys.argv[1])
        slutt_frekvens = int(sys.argv[2])
    except ValueError:
        print("Feil: Frekvensene må være gyldige heltall.")
        return

    # Konfigurer serie port
    try:
        serial_port = serial.Serial('COM6', baudrate=115200, timeout=1)
    except serial.SerialException as e:
        print(f"Feil ved åpning av seriell port: {e}")
        return

    # Send scan-kommandoen basert på frekvensene som er gitt
    scan_command = f'scan {start_frekvens} {slutt_frekvens}\r\n'.encode('utf-8')
    read_data_from_nanovna(serial_port, scan_command)
    time.sleep(0.1)

    try:
        # Hent frekvensdata
        print("Henter frekvenser...")
        frequencies = read_data_from_nanovna(serial_port, b"frequencies\r\n")
        if len(frequencies) == 0:
            print("Ingen frekvensdata mottatt.")
            return

        # Hent normaliserte S11-data (r og x)
        print("Henter S11-data...")
        s11_data = read_s11_data(serial_port)
        if len(s11_data) == 0:
            print("Ingen S11-data mottatt.")
            return
        
    except Exception as e:
        print(f"Feil ved mottak av data: {e}")
        return
    finally:
        serial_port.close()

    # Plot data med frekvenser som X-akse
    plot_return_loss_and_phase(frequencies, s11_data)

if __name__ == "__main__":
    main()
