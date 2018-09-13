#Sam's Club OA

# 1
'''
There are N students who applied to perform on stage, but there is a interesting regulation that the height difference between highest and shortest students on stages should be no more than K. Please output the possible maximum number of students who can make a performance on stage.
Input
Heights : an array of students’ heights ,  0<=heights<=10^9, 0<=N=len(heights)<=10^5
K: an integer (0<=K<=10^9)
Output
The maximum number of students

Sample
Input
5 5 5 4 6 7 1 2           
0

Output
3
'''
# time : O (n^2)
'''
def maxNumofStudents(students, k):
	if not students:
		return 0
	students.sort()
	maxCount = 0
	for i in range(len(students)):
		count = 0
		for j in range(i, len(students)):
			if students[j]-students[i] <= k:
				count += 1
				continue
			else:
				break
		maxCount = max(maxCount, count)
	return maxCount


if __name__ == '__main__':
	students = [5,5,5,4,6,7,1,2]
	k = 0
	print(maxNumofStudents(students, k))
'''
#