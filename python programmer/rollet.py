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

import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib.ticker as ticker

def parse_touchstone(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Finn dataene etter header
    data_lines = [line for line in lines if not line.startswith('!') and not line.startswith('#')]
    frequencies = []
    s_params = []

    for line in data_lines:
        values = line.strip().split()
        frequency = float(values[0])
        s11_real = float(values[1])
        s11_imag = float(values[2])
        s21_real = float(values[3])
        s21_imag = float(values[4])
        s12_real = float(values[5])
        s12_imag = float(values[6])
        s22_real = float(values[7])
        s22_imag = float(values[8])

        s11 = s11_real + 1j * s11_imag
        s21 = s21_real + 1j * s21_imag
        s12 = s12_real + 1j * s12_imag
        s22 = s22_real + 1j * s22_imag

        frequencies.append(frequency)
        s_params.append([[s11, s12], [s21, s22]])

    return np.array(frequencies), np.array(s_params)

def calculate_k_and_delta(s_params):
    s11, s12, s21, s22 = s_params[0,0], s_params[0,1], s_params[1,0], s_params[1,1]

    # Beregn stabilitetsfaktoren K
    delta = s11 * s22 - s12 * s21
    k = (1 - abs(s11)**2 - abs(s22)**2 + abs(delta)**2) / (2 * abs(s12 * s21))

    return k, delta

def plot_k_and_delta(frequencies, k_values, delta_values):
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_ylabel('K (Stability Factor)', color='tab:blue')
    ax1.plot(frequencies, k_values, color='tab:blue', label='K (Stability Factor)')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Δ (Delta)', color='tab:red')
    ax2.plot(frequencies, np.abs(delta_values), color='tab:red', label='Δ (Delta)')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    # Sett X-aksen til ingeniørnotasjon med SI-prefikser (kHz, MHz, GHz, osv.)
    ax1.xaxis.set_major_formatter(ticker.EngFormatter(unit='Hz'))
    ax1.xaxis.set_minor_formatter(ticker.EngFormatter(unit='Hz'))

    fig.tight_layout()
    plt.title('Stability Factor (K) and Δ (Delta) vs Frequency')
    plt.show()

def main(file_path):
    frequencies, s_params = parse_touchstone(file_path)

    k_values = []
    delta_values = []

    for s in s_params:
        k, delta = calculate_k_and_delta(s)
        k_values.append(k)
        delta_values.append(delta)

    plot_k_and_delta(frequencies, k_values, delta_values)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <touchstone_file.s2p>")
    else:
        file_path = sys.argv[1]
        main(file_path)
