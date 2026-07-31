input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")
file = open(input_file, "r")
lines = file.readlines()
file.close()
data = []
for line in lines:
    data.append(line.strip())
data.sort()
file = open(output_file, "w")
for line in data:
    file.write(line + "\n")
file.close()
print("Contents sorted successfully and written to", output_file)
