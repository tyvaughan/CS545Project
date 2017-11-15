import sys
print(sys.argv[1])
with open('sorted_emails.txt','r') as fp:
	emails = fp.readlines()
	with open('abrelsfo_labeled.txt', 'a') as f:
		for count, line in enumerate(emails[int(sys.argv[1]): int(sys.argv[2])]):
			print(count + int(sys.argv[1]))
			print(line.strip('\n').strip(' '))
			line = line.strip('\n')
			label = input('1:y, 2:m, 3:n  :  ')
			line = line + ':' + label + '\n'
			f.write(line)
