str = 'X-DSPAM-Confidence: 0.8475 '
sliced = str.find(":")
print (sliced)
convert = float(str[sliced+1:])
print (convert)