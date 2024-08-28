# © Thomas S. Knutsen LA3PNA  2024
#
# MF transformator type kjerner, transformatorkoblet på utgangen.
# Input parametere i bunnen.
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

def calculate_values(F, B, L, Qu=200):
    
    pi = math.pi
    omega = 2 * pi * F
    
    # Her starter beregningene
    C0 = 1 / (omega**2 * L)
    k = 1 / math.sqrt(2)
    q = math.sqrt(2)
    
    C12 = (C0 * k * B) / F  # koblingskondensator
    Ct = C0 - C12           # tuningkondensator
    Qend = (q * F * Qu) / (B * Qu - q * F)
    Rp = Qend * omega * L
    
    # Beregn antall turns
    L_in_microhenries = L * 1e6
    turns = math.sqrt((1000 * L_in_microhenries) / 16)
    tap = turns / (math.sqrt(Rp / 50))
    
    C0_pF = C0 * 1e12
    C12_pF = C12 * 1e12
    Ct_pF = Ct * 1e12

    # Beregne L anbefalt:
    Lrecommended = (250 / (2 * pi * F)) * 1e6 # 150-300 fungerer greit, det kan tunes her for å få mer hensiktsmessige kondensatorer
    
    # Print resultatet
    print(f"Given F = {F} Hz, B = {B} Hz, L = {L} H, and Qu = {Qu}:")
    print(f"omega = {omega:.4f}")
    print(f"C0 = {C0_pF:.4f} pF")
    print(f"C12 = {C12_pF:.4f} pF")
    print(f"Ct = {Ct_pF:.4f} pF")
    print(f"Qend = {Qend:.4f}")
    print(f"Rp = {Rp:.4f} Ohms")
    print(f"turns = {turns:.4f}")
    print(f"tap = {tap:.4f}")
    print(f"Lrecommended = {Lrecommended:.4f} µH")

# input beregningsparametere her: 
F = 7.1 * 10**6  # Senterfrekvens
B = 500000     # Bandwidth
L = 5 * 10**-6  # 5.7 µH 
Qu = 200  # Ikke endre om du ikke har målt Q
# Calling the function with the updated parameters
calculate_values(F, B, L, Qu)
