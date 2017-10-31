# The Best Rank (25)
# https://www.nowcoder.com/pat/1/problem/3992
# 时间限制 1000 ms 内存限制 32768 KB 代码长度限制 100 KB 判断程序 Standard (来自 小小)
# 题目描述
# To evaluate the performance of our first year CS majored students, we consider their grades of three courses only: C - C Programming Language, M - Mathematics (Calculus or Linear Algebra), and E - English.  At the mean time, we encourage students by emphasizing on their best ranks -- that is, among the four ranks with respect to the three courses and the average grade, we print the best rank for each student.
# For example, The grades of C, M, E and A - Average of 4 students are given as the following:
#
# StudentID  C  M  E  A
# 310101     98 85 88 90
# 310102     70 95 88 84
# 310103     82 87 94 88
# 310104     91 91 91 91
#
# Then the best ranks for all the students are No.1 since the 1st one has done the best in C Programming Language, while the 2nd one in Mathematics, the 3rd one in English, and the last one in average.
#
# 输入描述:
# Each input file contains one test case.  Each case starts with a line containing 2 numbers N and M (<=2000), which are the total number of students, and the number of students who would check their ranks, respectively.  Then N lines follow, each contains a student ID which is a string of 6 digits, followed by the three integer grades (in the range of [0, 100]) of that student in the order of C, M and E.  Then there are M lines, each containing a student ID.
#
#
# 输出描述:
# For each of the M students, print in one line the best rank for him/her, and the symbol of the corresponding rank, separated by a space.
# The priorities of the ranking methods are ordered as A > C > M > E.  Hence if there are two or more ways for a student to obtain the same best rank, output the one with the highest priority.
# If a student is not on the grading list, simply output "N/A".
#
# 输入例子:
# 5 6
# 310101 98 85 88
# 310102 70 95 88
# 310103 82 87 94
# 310104 91 91 91
# 310105 85 90 90
# 310101
# 310102
# 310103
# 310104
# 310105
# 999999
#
# 输出例子:
# 1 C
# 1 M
# 1 E
# 1 A
# 3 A
# N/A
# 原题有错，这里约定，平均分想下取整，同时排名如果分数一样则排名一致。

# 这个程序的版本是做的流数据版本，非离线版。
line_1 = input().split(' ')
n,m = line_1[0],line_1[1]
courses_names = ('A','C','M','E')
courses = [[0]*101 for _ in courses_names]
logs = dict()
for i in range(int(n)):
    line_data = input().split(' ')
    avg_score = int((sum(map(lambda x:int(x), line_data[1:])))/(len(courses_names)-1)-.5)
    logs[line_data[0]] = [avg_score, line_data[1], line_data[2], line_data[3]]
    courses[0][avg_score] += 1
    for j in range(1,len(line_data)):
        courses[j][int(line_data[j])] += 1
for j in range(int(m)):
    t_log = logs.get(input().strip())
    if t_log is None:
        print('N/A')
    else:
        best_rank = 2001
        best_course = 'A'
        for k in range(len(courses_names)):
            score = int(t_log[k])
            rank = 1
            for t_score in range(score+1,101):
                rank += courses[k][t_score]
            if rank < best_rank:
                best_rank = rank
                best_course = courses_names[k]
        print(best_rank,best_course)