import itertools
import csv

all_set = list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9]))
players = []

record_id = [362881]

id = 1
for i in all_set:
    players.append((id, i, '10k', '0', '1500', '0', '0', '0', '0'))
    id += 1

with open('profile.csv', 'w', newline='') as profile:
    csv_writer = csv.writer(profile)
    csv_writer.writerow(('id', 'sequence', 'level', 'pt', 'R', '1st', '2nd', '3rd', '4th'))
    for p in players:
        csv_writer.writerow(p)
    csv_writer.writerow(('362881', '(9,9,9,9,9,9,9,9,9)', '10k', '0', '1500', '0', '0', '0', '0'))
    profile.close()

for rid in record_id:
    f = open(str(rid)+'.txt', 'w')
    f.write('*******************************\n')
    f.write('Recorded id:' + str(rid)+'\n')
    f.close()