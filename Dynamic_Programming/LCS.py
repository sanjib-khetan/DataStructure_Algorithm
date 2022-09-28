str1 = "ABCDEFGHI"
str2 = "ABCDEFGHI"

#Recusrsion Aproach

def recursion_method(str1, str2, l1, l2, m1, m2):

    if l1 < m1 and l2 < m2:
        if len(str1) == 0 or len(str2) == 0:
            return 0

        if str1[l1] == str2[l2]:
            return 1 + recursion_method(str1, str2, l1+1, l2+1, m1, m2)

        else:
            return max( recursion_method(str1, str2, l1+1, l2, m1, m2), recursion_method(str1, str2, l1, l2+1, m1, m2) )

    else:
        return 0

print(recursion_method(str1, str2, 0, 0, len(str1), len(str2)))

def dp_method(str1, str2, m, n):

    arr = [[None] * (m+1) for i in range(n+1)]

    for i in range(m+1):
        for j in range(n+1):

            if i == 0 or j == 0:
                arr[i][j] = 0

            elif str1[i-1] == str2[j-1]:
                arr[i][j] = 1 + arr[i-1][j-1]

            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])

    return arr[m][n]

print(dp_method(str1, str2, len(str1), len(str2)))