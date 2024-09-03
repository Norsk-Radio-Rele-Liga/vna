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
