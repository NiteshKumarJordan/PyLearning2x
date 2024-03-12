# writing a file in csv

import csv

with open('test.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Name', 'Age'])
    csv_writer.writerow(['<rahul>', 25])
    csv_writer.writerow(['<mukesh>', 26])
    csv_writer.writerow(['<ajay>', 27])
    csv_writer.writerow(['<vishal>', 28])

    csv_file.close()








