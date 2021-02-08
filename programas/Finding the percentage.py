if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum=0.0
    for note in student_marks[query_name]:
        sum+=note      
    sum/=3.0
    print ("{0:.2f}".format(sum))
    #print(round(sum, 3))
