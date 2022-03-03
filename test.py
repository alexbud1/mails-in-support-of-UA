# files = ["1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg"]  # In same directory as script
# for f in files:
#     filename = f
#     print(filename)
receivers = []
with open ('emails.txt', 'rt') as myfile:  # Open lorem.txt for reading
	for myline in myfile:              # For each line, read to a string,
		receivers.append(myline.rstrip("\n"))

print(receivers)