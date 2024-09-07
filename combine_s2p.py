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

import sys

def read_s2p_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    header = lines[0].strip()
    data_lines = [line.strip().split() for line in lines[1:]]
    return header, data_lines

def combine_s2p(file1, file2, output_file):
    # Read the input files
    header1, data1 = read_s2p_file(file1)
    header2, data2 = read_s2p_file(file2)
    
    # Check if headers match (except for parameter positions)
    if header1 != header2:
        raise ValueError("Headers of the files do not match!")

    # Combine data assuming both files have the same frequencies
    combined_data = []
    for d1, d2 in zip(data1, data2):
        frequency = d1[0]  # Extract frequency
        # Combine S-parameters: S11, S21 from file1 and S12, S22 from file2
        combined_data.append(
            [frequency] + d1[1:3] + d1[3:5] + d2[3:5] + d2[1:3]
        )
    
    # Write the combined data to the output file
    with open(output_file, 'w') as out_file:
        out_file.write(header1 + '\n')
        for data in combined_data:
            out_file.write(' '.join(data) + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python combine_s2p.py file_S11_S21.s2p file_S22_S12.s2p output_file.s2p")
        sys.exit(1)
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output_file = sys.argv[3]
    
    combine_s2p(file1, file2, output_file)
    print(f"Combined file created: {output_file}")
