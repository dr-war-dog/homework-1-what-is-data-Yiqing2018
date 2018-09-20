# homework1
# What is data
# author @ Yiqing Liu

# Question 1: What is the average/mean score of the LA County Resturant Inspections?
# Question 2: How many times was facility address 17660 CHATSWORTH ST visited?
# Question 3: How many times was facility city LANCASTER visited?
# Question 4: What percentage of times did employee EE0000145 visit any facility?
# Question 5: What percentage of times was facility FA0013858 visited?
# Question 6: What percentage of times did employee EE0000593 visit GRANADA HILLS?

import csv
import os
class Dataset:

	def __init__(self,filename,codingstyle):
		self.f = open(filename,encoding=codingstyle)
		self.csv_reader=csv.reader(self.f)
		self.size=-1
		self.header=next(self.csv_reader)
		self.f.seek(0)

	def getSize(self):
		if(self.size==-1):
			count=0
			for row in self.csv_reader:
				count=count+1
			self.size=count
			self.f.seek(0)
		return self.size

	def getPercentage(self,column_name,target):
		count=self.countVisited(column_name,target)
		return ('%.2f%%' %((count/self.getSize())*100))

	def find_which_column(self,to_find_column_name):
		res=[]
		for i in range(len(to_find_column_name)):
			target=to_find_column_name[i]
			for index in range(len(self.header)):
				if (self.header[index]==target):
					res.append(index)
		if(len(res)!=len(to_find_column_name)):
			print("OMG, no such column!")
			# quit!!
			os._exit(0)
		return res

	def getAverage(self,column):
		column_name=[]
		column_name.append(column)
		column_index=self.find_which_column(column_name)[0]
		sum=0
		number=0
		for row in self.csv_reader:
			if(row[column_index].isdigit()):
				score= int(row[column_index])
				number=number+1
				sum+=score
		self.f.seek(0)
		if(number==0):
			print("no data")
			return None
		return (sum/number)
	def countVisited(self,column_name,targets):
		column_index=self.find_which_column(column_name) # list
		count=0
		flag=0
		for row in self.csv_reader:
			for check_index in range(len(column_index)):
				data=row[column_index[check_index]]
				tar=targets[check_index]
				if(data!=tar):
					flag=-1
					break
			if(flag==0):
				count=count+1
			flag=0
		self.f.seek(0)
		return count

def main():
	d=Dataset("la-county-restaurant-inspections.csv","utf-8")
	# print(d.header)
	# d.find_which_column(["hello"])
	print('''Question 1:
	the average of score is ''',d.getAverage("score"))
	print('''Question 2:
	visit '17660 CHATSWORTH ST' for how many times? ''',d.countVisited(['facility_address'],["17660 CHATSWORTH ST"]))
	print('''Question 3:
	visit 'LANCASTER' for how many times? ''',d.countVisited(['facility_city'],["LANCASTER"]))
	print('''Question 4:
	employee EE0000145 visits for what percentage? ''',d.getPercentage(["employee_id"],["EE0000145"]))
	print('''Question 5:
	facility FA0013858 visits for what percentage? ''',d.getPercentage(["facility_id"],["FA0013858"]))
	print('''Question 6:
	employee EE0000593 visits GRANADA HILLS for what percentage? ''',d.getPercentage(['employee_id','facility_city'],['EE0000593','GRANADA HILLS']))
	
if __name__=='__main__':
	main()

