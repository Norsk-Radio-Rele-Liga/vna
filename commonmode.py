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
    s21_values = []

    for line in data_lines:
        values = line.strip().split()
        frequency = float(values[0])
        s21_real = float(values[3])
        s21_imag = float(values[4])

        s21 = s21_real + 1j * s21_imag

        frequencies.append(frequency)
        s21_values.append(s21)

    return np.array(frequencies), np.array(s21_values)

def calculate_cmrr(s21_values, s31_values):
    cmrr_values = 20 * np.log10(np.abs((s21_values + s31_values) / (s21_values - s31_values)))
    return cmrr_values

def plot_cmrr(frequencies, cmrr_values):
    plt.figure()

    plt.plot(frequencies, cmrr_values, color='tab:blue', label='CMRR (dB)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('CMRR (dB)')
    plt.title('CMRR vs Frequency')
    plt.grid(True)

    # Sett X-aksen til ingeniørnotasjon med SI-prefikser (kHz, MHz, GHz, osv.)
    plt.gca().xaxis.set_major_formatter(ticker.EngFormatter(unit='Hz'))
    plt.gca().xaxis.set_minor_formatter(ticker.EngFormatter(unit='Hz'))

    plt.tight_layout()
    plt.show()

def main(file_s21, file_s31):
    frequencies_s21, s21_values = parse_touchstone(file_s21)
    frequencies_s31, s31_values = parse_touchstone(file_s31)

    # Sjekk om frekvensene matcher
    if not np.array_equal(frequencies_s21, frequencies_s31):
        print("Error: The frequency points in the two files do not match.")
        return

    cmrr_values = calculate_cmrr(s21_values, s31_values)
    plot_cmrr(frequencies_s21, cmrr_values)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <s21_file.s2p> <s31_file.s2p>")
    else:
        file_s21 = sys.argv[1]
        file_s31 = sys.argv[2]
        main(file_s21, file_s31)
