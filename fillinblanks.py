def solution(array):
	valid = 0
	res = []
	for i in nums:
		if i is not None:
			res.append(i)
			valid = i
		else:
			res.append(valid)

	return res