import csv

# newline
outputFile = open('output.tsv', 'w', newline='')
outputWriter = csv.writer(outputFile, delimiter='\t', lineterminator='\n\n')
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.1415926, 4])
outputFile.close()


