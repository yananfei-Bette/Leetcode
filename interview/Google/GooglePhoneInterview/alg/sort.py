import math

#selection Sort
#TC:O(n^2)
def selectionSort(s):
	for i in range(len(s)-1):
		minInd = i
		for j in range(i, len(s)):
			if s[j] < s[minInd]:
				minInd = j
		s[i], s[minInd] = s[minInd], s[i]
	return s

def bubbleSort(s):
	for i in range(len(s)):
		for j in range(0,len(s)-1-i):
			if s[j] > s[j+1]:
				s[j], s[j+1] = s[j+1], s[j]
	return s

def insertionSort(s):
	for i in range(1,len(s)):
		previousInd = i-1
		currentValue = s[i]
		while previousInd >= 0 and s[previousInd] > currentValue:
			s[previousInd+1] = s[previousInd]
			previousInd -= 1
		s[previousInd+1] = currentValue
	return s

def shellSort(s):
	# initial gap
	gap = 1
	while gap < float(len(s))/3:
		gap = gap*3+1

	while gap > 0:
		for i in range(gap, len(s)):
			temp = s[i]
			j = i-gap
			while j >= 0 and s[j]>temp:
				s[j+gap] = s[j]
				j -= gap
			s[j+gap] = temp
		gap = math.floor(float(gap)/3)
	return s

def mergeSort(s): # Divide
	def merge(left, right): #Conquer
		#print('input')
		#print(left, right)	
		res = []
		while len(left) > 0 and len(right) > 0:
			if left[0] <= right[0]:
				res.append(left.pop(0))
			else:
				res.append(right.pop(0))
		while left:
			res.append(left.pop(0))
		while right:
			res.append(right.pop(0))
		#print('-----')
		#print(res)
		return res

	if len(s) < 2: return s
	mid = math.floor(float(len(s))/2)
	left = s[:mid]
	right = s[mid:]
	return merge(mergeSort(left), mergeSort(right))

def quickSort(s):
	#recursively solve
	def quickSortRecursive(s, first, last):
		if first < last:
			splitPoint = partition(s, first, last)
			quickSortRecursive(s, first, splitPoint-1)
			quickSortRecursive(s, splitPoint+1, last)
	
	def partition(s, first, last):
		pivotValue = s[first]
		leftMark = first+1
		rightMark = last
		done = False
		while not done:
			# if s[leftMark] > pivot, stop
			while leftMark <= rightMark and s[leftMark] <= pivotValue:
				leftMark += 1
			# s[rightMark] < pivot, stop
			while leftMark <= rightMark and s[rightMark] >= pivotValue:
				rightMark -= 1
			if leftMark > rightMark:
				done = True
			else:
				# switch
				s[leftMark], s[rightMark] = s[rightMark], s[leftMark]
		# switch pivot to the middle
		s[first], s[rightMark] = s[rightMark], s[first]
		return rightMark
		
	quickSortRecursive(s,0,len(s)-1)
	return s

def heapSort(s):
	l = len(s)

	def buildMaxHeap(s):
		for i in range(math.floor(float(len(s))/2),-1,-1):
			heapify(s, i)

	def heapify(s,root):
		left = 2*root+1
		right = 2*root+2
		largest = root
		if left < l and s[left] > s[largest]:
			largest = left
		if right < l and s[right] > s[largest]:
			largest = right
		if largest != root:
			swap(s, root, largest)
			heapify(s, largest)

	def swap(s, i, j):
		s[i], s[j] = s[j], s[i]

	buildMaxHeap(s)
	for i in range(len(s)-1,-1,-1):
		swap(s, 0, i)
		l -= 1
		heapify(s, 0)
	return s		

if __name__ == '__main__':
	s = [40,9,-1,0,90,35,67,83,35,2,14,25,5,6]
	print('******** Selection Sort ***********')
	print(selectionSort(s))
	print('******** Bubble Sort **************')
	print(bubbleSort(s))
	print('******** Insertion Sort ***********')
	print(insertionSort(s))
	print('******** Shell Sort ***************')
	print(shellSort(s))
	print('******** Merge Sort ***************')
	print(mergeSort(s))
	print('******** Quick Sort ***************')
	print(quickSort(s))
	print('******** Heap Sort ****************')
	print(heapSort(s))
