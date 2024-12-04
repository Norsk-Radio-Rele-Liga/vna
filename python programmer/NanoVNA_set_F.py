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

# Sett opp seriell kommunikasjon
ser = serial.Serial('COM3', 115200, timeout=1)  
# Endre 'COM3' til riktig port for ditt system
time.sleep(2)

# Skriv kommando til NanoVNA for å sette frekvensområde
ser.write(b'sweep 5000000 30000000\n')
time.sleep(0.1)

# Hent S21 data fra NanoVNA
ser.write(b'data 1\n')
time.sleep(0.1)
data = ser.read(ser.inWaiting()).decode('utf-8')

# Skriv ut dataene og lukk tilkoblingen
print(data)
ser.close()
