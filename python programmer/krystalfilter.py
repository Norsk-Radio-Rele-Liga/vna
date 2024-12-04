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

import math

def calculate_C(f0, Cm_pF, B, Lm, N):
    # Konverter Cm fra pF til F
    Cm = Cm_pF * 1e-12
    
    # Beregn k
    k = 0.5 * math.exp(math.log(2) / N)
    
    # Beregn q
    q = 1 / k
    
    # Beregn C i F
    C_F = (f0 * Cm) / (B * k)
    
    # Konverter C fra F til pF
    C_pF = C_F * 1e12
    
    # Beregn Rt
    Rt = (2 * math.pi * B * Lm) / (2 * q)
    
    return C_pF, Rt

# Input verdier (du kan endre disse etter behov)
Lm = float(input("Enter Lm in Henry: "))  # Lm i H
Cm_pF = float(input("Enter Cm in picofarad (pF): "))  # Cm i pF
f0 = float(input("Enter f0 in Hz: "))  # f0 i Hz
B = float(input("Enter B: "))  # B er en konstant eller verdi du velger
N = float(input("Enter N: "))  # N er en konstant eller verdi du velger

# Beregn C og Rt
C_pF, Rt = calculate_C(f0, Cm_pF, B, Lm, N)

# Resultater
print(f"C = {C_pF:.2f} pF")
print(f"Rt = {Rt:.2f} Ohm")
