import re
import csv

log_file = open('../task1/sample.log')
data = log_file.readlines()

output_file = open('output.csv', 'w', newline='')
output_dict_writer = csv.DictWriter(output_file, ['Date', 'Error Type', 'Message'])
output_dict_writer.writeheader()


for line in data:
	match = re.search(r'\[([0-9]{4}-[0-9]{2}-[0-9]{2}).+ERROR:\s(\w+)\s-\s(.+)', line)
	if match: 
		output_dict_writer.writerow({'Date': match.group(1), 'Error Type': match.group(2), 'Message': match.group(3)})
		
		
output_file.close()
		
