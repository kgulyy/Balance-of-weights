from itertools import chain, combinations

def powerset(iterable):
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def listOutput(list):
	return ' '.join(str(i) for i in list)
	
sequence = [int(i) for i in input('Enter sequence of number (1 2 3 4): ').split()]
if sum(sequence) % 2 != 0:
	print('no')
else:
	scale = 2
	result = [[] for i in range(scale)]
	weight = {i:0 for i in range(scale)}

	sequence.sort()
	sequence.reverse()

	temp = 0
	for element in sequence:
		for w in weight:
			if temp == weight[w] or weight[w] + element == sum(sequence)//scale:
				result[w].append(element)
				weight[w] += element
				break
		temp = min(weight.values())

	if sum(result[0]) != sum(result[1]):
		print('no')
	else:
		print(listOutput(result[0]), '-', listOutput(result[1]))
print('yes' if [i for i in powerset(sequence) if sum(i) == 100] else 'no')