while True:
    try:
        file_name = input("Enter filename: ")
        file_handle = open(file_name)
        break
    except:
        print("File doesn't exist")
total = 0
count = 0
for line in file_handle:
        if line.startswith("X-DSPAM-Confidence:"):
            value = line[20:]
            value_conv = float(value)
            total += value_conv
            count += 1

print('Average spam confidence:',total/count)