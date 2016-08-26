# all sort algorithms


def InsertSort(alist):
	for idx in range(1, len(alist)):
		curvalue = alist[idx]
		pos = idx

		while pos > 0 and alist[pos - 1] > curvalue:
			alist[pos] = alist[pos - 1]
			pos = pos - 1

		alist[pos] = curvalue

alist = [9, 8, 7, 10, 12, 6, 5, 18, 2]
InsertSort(alist)
print alist


def SelectMinKey(alist, pos):
	minv = alist[pos]
	idx = pos

	if pos + 1 < len(alist):
		for i in range(pos + 1, len(alist)):
			if alist[i] < minv:
				minv = alist[i]
				idx = i

	return idx


def SelectSort(alist):
	if len(alist) <= 0:
		return

	for i in range(0, len(alist)):
		idx = SelectMinKey(alist, i)
		tmp = alist[i]
		alist[i] = alist[idx]
		alist[idx] = tmp

alist = [9, 8, 7, 10, 12, 6, 5, 18, 2]
SelectSort(alist)
print alist


def BubbleSort(alist):
	for i in range(1, len(alist)):
		for j in range(0, len(alist) - i):
			if alist[j] > alist[j + 1]:
				tmp = alist[j + 1]
				alist[j + 1] = alist[j]
				alist[j] = tmp


alist = [9, 8, 7, 10, 12, 6, 5, 18, 2]
BubbleSort(alist)
print alist


def partition(alist, low, high):


def QuickSort(alist, low, high):


alist = [9, 8, 7, 10, 12, 6, 5, 18, 2]
QuickSort(alist, 0, len(alist) - 1)
print alist
