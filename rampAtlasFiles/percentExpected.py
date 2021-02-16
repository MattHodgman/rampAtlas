import sys
import csv

inputFile = sys.argv[1]

rampD = {}
# [RH, RL, NH, NL]
percentD = {}


with open(inputFile) as open1:
	for line in open1:
		row = line.split(',')
		geneName = row[1]
		if geneName not in rampD.keys():
			rampD[geneName] = [0, 0, 0, 0]

		if row[6] == ' Y\n':
			if row[4] == 'High':
				rampD[geneName][0] += 1
			elif row[4] == 'Low':
				rampD[geneName][1] += 1
		elif row[6] == ' N\n':
			if row[4] == 'High':
				rampD[geneName][2] += 1
			elif row[4] == 'Low':
				rampD[geneName][3] += 1

header = ['gene', 'percent expected', 'high ramp', 'low ramp', 'high no ramp', 'low no ramp']

more50 = 0
more75 = 0
more90 = 0
total = 0
with open("percentExpected.csv", 'w') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow(header)
	for gene, nums in rampD.items():
		T = sum(nums)
		if T > 3:
			# RH/T + RL/T
			perExpected = round(((nums[0] + nums[3]) / T) * 100, 4)
			if perExpected > 50:
				more50 += 1
				if perExpected > 75:
					more75 += 1
					if perExpected > 90:
						more90 += 1
			total += 1

			writer.writerow([gene, perExpected, nums[0], nums[1], nums[2], nums[3]])

print(more50, more75, more90, total)
