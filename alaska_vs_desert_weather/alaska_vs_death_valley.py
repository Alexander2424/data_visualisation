import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Get dates and high temperatures from file.
# filename = 'sitka_weather_2018_simple.csv'
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	# print(header_row)
	# for index, column_header in enumerate(header_row):
	# 	print(index, column_header)
	
	# Get high, and low temperatures from file.
	dates, highs, lows = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[2], "%Y-%m-%d")
			high = int(row[5])
			low = int(row[6])
		except ValueError:
			print(current_date, 'missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

filename1 = 'death_valley_2018_simple.csv'
with open(filename1) as f1:
	reader1 = csv.reader(f1)
	header_row1 = next(reader1)
	# print(header_row)
	# for index, column_header in enumerate(header_row):
	# 	print(index, column_header)
	
	# Get high, and low temperatures from file.
	dates1, highs1, lows1 = [], [], []
	for row in reader1:
		try:
			current_date1 = datetime.strptime(row[2], "%Y-%m-%d")
			high1 = int(row[5])
			low1 = int(row[6])
		except ValueError:
			print(current_date, 'missing data')
		else:
			dates1.append(current_date1)
			highs1.append(high1)
			lows1.append(low1)

	# Plot data
	fig = plt.figure(dpi=128, figsize=(10,6))
	plt.plot(dates, highs, c='red', alpha=0.5)
	plt.plot(dates, lows, c='blue', alpha=0.5)
	plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
	# print(highs)

	plt.plot(dates1, highs1, c='green', alpha=0.5)
	plt.plot(dates1, lows1, c='yellow', alpha=0.5)
	plt.fill_between(dates1, highs1, lows1, facecolor='green', alpha=0.1)

	# Format plot.
	title = ("Daily Temp. Comparison Sitka(b-r), Alaska vs Death Valley(g-y),"  
		+ " CA (2018).")
	plt.title(title, fontsize=18)
	plt.xlabel('', fontsize=16)
	fig.autofmt_xdate()
	plt.ylabel("Temperature (F)", fontsize=16)
	plt.ylim(20, 115)
	plt.tick_params(axis='both', which='major', labelsize=16)

	plt.show()