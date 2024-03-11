# importing csv module
import csv

# Create a CSV file named 'persons.csv'
with open (r'persons.csv', 'w') as csvfile:
  writer = csv.writer(csvfile)

# Insert data into into 'persons.csv'
with open (r'persons.csv', 'w', newline = '') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['ID', 'NAME', 'AGE', 'GENDER'])
  writer.writerow([1, 'James', 20, 'M'])
  writer.writerow([2, 'Katey', 10, 'F'])
  writer.writerow([3, 'Kiran', 40, 'M'])
  writer.writerow([4, 'Sana', 19, 'F'])
  
with open (r'persons.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for record in reader:
    print(record)

# display/fetch/read data from 'persons.csv' - 1
with open (r'persons.csv', 'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for record in reader:
    if record['GENDER'] == 'F':
      print(record['ID'],' ',record['NAME'])

# display/fetch/read data from 'persons.csv' - 2
with open (r'persons.csv', 'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for record in reader:
    if record['AGE'] < 18:
      print(record['ID'],' ',record['NAME'])

# Insert data into into 'persons.csv' when order is different
with open (r'persons.csv', 'a', newline = '') as csvfile:
  fields = ['ID', 'NAME', 'AGE', 'GENDER']
  writer = csv.DictWriter(csvfile, fields)
  # writer.writeheader()  # not required as HEader is already inserted
  writer.writerow({'ID':5, 'AGE':23, 'GENDER':'M', 'NAME':'Raja'})
  writer.writerow({'ID':6, 'AGE':30, 'GENDER':'F', 'NAME':'Sara'})
  writer.writerow({'ID':7, 'AGE':25, 'GENDER':'M', 'NAME':'Sash'})

with open (r'persons.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for record in reader:
    print(record)
