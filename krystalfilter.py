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
