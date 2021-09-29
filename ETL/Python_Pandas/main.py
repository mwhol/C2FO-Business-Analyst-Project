#!/usr/bin/python

import pandas as pd


def main():

	# Importing just the columns we need to save memory
	fields = ['Call Date', 'Received DtTm', 'On Scene DtTm', 'Battalion']
	data = pd.read_csv('Fire_Department_Calls_for_Service.csv', usecols=fields)

	# I debated back and forth on this, I wasn't sure whether I should be dropping calls
	# that don't receive a response or whether I should be valuing them as 0
	# I ended up deciding to drop them but I could easily be convinced to go the other way
	data = data[data['On Scene DtTm'].notna()]

	# Was super duper slow so specified date format to speed it up
	data['Call Date'] = pd.to_datetime(data['Call Date'], format='%m/%d/%Y')

	# Calculate one year back then go to first of that month, that's our start date
	dateCutoff = (data['Call Date'].max() - pd.DateOffset(months=11)).replace(day=1)
	data = data[~(data['Call Date'] < dateCutoff)]

	# Formatting the other datetime columns
	data['Received DtTm'] = pd.to_datetime(data['Received DtTm'], format='%m/%d/%Y %I:%M:%S %p')
	data['On Scene DtTm'] = pd.to_datetime(data['On Scene DtTm'], format='%m/%d/%Y %I:%M:%S %p')

	# Calculating Response Times with datetime subtraction
	data.insert(1, '90th Percentile Response Time', 0)
	data['90th Percentile Response Time'] = (data['On Scene DtTm'] - data['Received DtTm']).dt.total_seconds()

	# A little cleanup to make our final answer formatted like the sample
	data = data.rename(columns={'Battalion':'EmergencyResponseDistrict'})
	data['Month'] = data['Call Date'].dt.to_period('M')
	data = data[['EmergencyResponseDistrict', 'Month', '90th Percentile Response Time']]


	# Generating our answer table with a group by and quantile (and fixing the index)
	answer = data.groupby([data['EmergencyResponseDistrict'], data['Month']]).quantile(0.9).reset_index()

	# Sorting for proper ordering
	answer.sort_values(by=['EmergencyResponseDistrict', 'Month'], ascending=[1,0], inplace=True)

	# Printing the answer to a file
	answer.to_csv('answer.csv', index=False)






if __name__ == '__main__':
  main()