import matplotlib.pyplot as plt
import sys
import numpy as np
#arg: nomeFileDeiCount nomeFileDelleLatenze titoloGrafico nomeImg
# Set the figure size
plt.rcParams["figure.figsize"] = [30.00, 10]
plt.rcParams["figure.autolayout"] = True

with open(sys.argv[1],'r') as file:
	print(sys.argv[1])
	content = file.read()
	#print(content)
	numbers = [float(num) for num in content.split(',') if num]
#	print(numbers)

	file_latenze = open(sys.argv[2],'r')
	print(sys.argv[2])
	content_latenze = file_latenze.read()
	content_latenze = content_latenze[:-2]
	latenze = [str(num) for num in content_latenze.split(',') if num]
	k = numbers
	label = latenze
#	print(k)
	print(label)
	print(k)
	print(len(k))
	print(len(latenze))
# Plot the histogram
	plt.bar(np.arange(len(label)), k, align='center')

	plt.xticks(np.arange(len(label)), label, rotation='vertical', fontsize=7)
# Save the histogram
# giving title to the plot
# BIND UDP 200000_40000
	plt.title("Latency Buckets di "+sys.argv[3])
	
	# giving X and Y labels
	plt.xlabel("Range di latenze")
	plt.ylabel("Numero di risposte")
#bindudp2000_4000.png
	plt.savefig(sys.argv[4])

# Display the plot
	plt.show()

