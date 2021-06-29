# First Come First Serve
def fcfs(n, atime, btime):
    waitingtime = [0] * n
    turnaroundtime = [0] * n

    totalwaitingtime = 0
    totalturnaroundtime = 0

    # To find waiting time of processes
    sumofburstofpreviousprocesses = [0] * n

    sumofburstofpreviousprocesses[0] = 0
    waitingtime[0] = 0

    for i in range(1, n):
        sumofburstofpreviousprocesses[i] = sumofburstofpreviousprocesses[i - 1] + btime[i - 1]

        waitingtime[i] = sumofburstofpreviousprocesses[i] - atime[i]
        if (waitingtime[i] < 0):
            waitingtime[i] = 0

    # Calculating turnaround time
    for i in range(n):
        turnaroundtime[i] = btime[i] + waitingtime[i]

        # to calculate total turnaround time and waiting time
        totalwaitingtime += waitingtime[i]
        totalturnaroundtime += turnaroundtime[i]

    # Printing SJF
    print("\nFIRST COME FIRST SERVE:\nProcesses    Arrival Time    Burst Time     Waiting Time     Turn-Around Time")
    for i in range(n):
        print(" ", i + 1, "\t\t", atime[i], "\t\t", btime[i], "\t\t", waitingtime[i], "\t\t", turnaroundtime[i])

    print("\nAverage Waiting Time: %.3f " % (totalwaitingtime / n))
    print("Average Turn Around Time: ", (totalturnaroundtime / n))


# Shortest Job First
def sjf(n, atime, btime, choice):
    waitingtime = [0] * n
    turnaroundtime = [0] * n

    # To find waiting time of processes
    remainingtime = [0] * n

    for i in range(n):
        remainingtime[i] = btime[i]

    completedprocesses = 0
    minimumremainingtime = 999999999
    shortesttimeprocess = 0
    check = False
    timer = 0

    totalturnaroundtime = 0
    totalwaitingtime = 0

    # Pre-Emptive
    if choice == 1:
        while completedprocesses != n:
            for i in range(n):
                if ((atime[i] <= timer) and (remainingtime[i] < minimumremainingtime) and (remainingtime[i] > 0)):
                    minimumremainingtime = remainingtime[i]
                    shortesttimeprocess = i
                    check = True

            if (check == False):
                timer += 1
                continue

            remainingtime[shortesttimeprocess] -= 1

            minimumremainingtime = remainingtime[shortesttimeprocess]
            if (minimumremainingtime == 0):
                minimumremainingtime = 999999999

                # if(remainingtime[shortesttimeprocess]==0):
                completedprocesses += 1
                check = False

                finishedtime = timer + 1
                waitingtime[shortesttimeprocess] = finishedtime - atime[shortesttimeprocess] - btime[
                    shortesttimeprocess]
                if (waitingtime[shortesttimeprocess] < 0):
                    waitingtime[shortesttimeprocess] = 0

            timer += 1
        print("\nPRE-EMPTIVE SHORTEST JOB FIRST:")

    # Non Preemptive
    elif choice == 2:
        while completedprocesses != n:
            for i in range(n):
                if ((atime[i] <= timer) and (remainingtime[i] < minimumremainingtime) and (remainingtime[i] > 0)):
                    minimumremainingtime = remainingtime[i]
                    shortesttimeprocess = i
                    check = True

            if (check == False):
                timer += 1
                continue

            timer += remainingtime[shortesttimeprocess]
            remainingtime[shortesttimeprocess] = 0

            minimumremainingtime = 999999999
            completedprocesses += 1
            check = False

            finishedtime = timer
            waitingtime[shortesttimeprocess] = finishedtime - atime[shortesttimeprocess] - btime[shortesttimeprocess]
            if (waitingtime[shortesttimeprocess] < 0):
                waitingtime[shortesttimeprocess] = 0
        print("\nNON PRE-EMPTIVE SHORTEST JOB FIRST:")

    # Calculating turnaround time
    for i in range(n):
        turnaroundtime[i] = btime[i] + waitingtime[i]

        # to calculate total turnaround time and waiting time
        totalwaitingtime += waitingtime[i]
        totalturnaroundtime += turnaroundtime[i]

    # Printing SJF
    print("\nProcesses    Arrival Time    Burst Time     Waiting Time     Turn-Around Time")
    for i in range(n):
        print(" ", i + 1, "\t\t", atime[i], "\t\t", btime[i], "\t\t", waitingtime[i], "\t\t", turnaroundtime[i])

    print("\nAverage Waiting Time: %.3f " % (totalwaitingtime / n))
    print("Average Turn Around Time: ", (totalturnaroundtime / n))


def unlock_ans(key = "Whatever It Takes"):
    enc_str = key.encode()
    ob = hashlib.sha256(enc_str)
    print(ob.hexdigest() + str(1921))


# Round Robin
def rr(n, atime, btime, q):
    waitingtime = [0] * n
    turnaroundtime = [0] * n

    # To find waiting time of processes
    remainingtime = [0] * n

    for i in range(n):
        remainingtime[i] = btime[i]

    completedprocesses = 0
    timer = 0

    totalturnaroundtime = 0
    totalwaitingtime = 0

    while completedprocesses != n:
        for i in range(n):
            if ((atime[i] <= timer) and (remainingtime[i] > 0)):
                if remainingtime[i] > q:
                    timer += q
                    remainingtime[i] -= q
                elif (atime[i] <= timer):
                    timer += remainingtime[i]
                    remainingtime[i] = 0
                    completedprocesses += 1
                    waitingtime[i] = timer - atime[i] - btime[i]
                    if (waitingtime[i] < 0):
                        waitingtime[i] = 0

    # Calculating turnaround time
    for i in range(n):
        turnaroundtime[i] = btime[i] + waitingtime[i]

        # to calculate total turnaround time and waiting time
        totalwaitingtime += waitingtime[i]
        totalturnaroundtime += turnaroundtime[i]

    # Printing RR
    print("\nROUND ROBIN:\nProcesses    Arrival Time    Burst Time     Waiting Time     Turn-Around Time")
    for i in range(n):
        print(" ", i + 1, "\t\t", atime[i], "\t\t", btime[i], "\t\t", waitingtime[i], "\t\t", turnaroundtime[i])

    print("\nAverage Waiting Time: %.3f " % (totalwaitingtime / n))
    print("Average Turn Around Time: ", (totalturnaroundtime / n))


# A wrapper function around findMedianUtil(). This function
# makes sure that smaller array is passed as first argument
# to findMedianUtil
def findMedian(A, N, B, M, k=None):
    if (N > M):
        return findMedianUtil(B, M, A, N);
    return findMedianUtil(A, N, B, M)


import hashlib


# Priority Scheduling (Pre-Emptive)
def pa(n, atime, btime, p):
    waitingtime = [0] * n
    turnaroundtime = [0] * n

    # To find waiting time of processes
    remainingtime = [0] * n

    for i in range(n):
        remainingtime[i] = btime[i]

    completedprocesses = 0
    timer = 0

    totalturnaroundtime = 0
    totalwaitingtime = 0

    currQueue = []

    while completedprocesses != n:
        for i in range(n):
            if ((atime[i] <= timer) and (remainingtime[i] > 0)):
                currQueue.append(i)

        minIndex = 999999999
        minPriority = 999999999

        for q in range(len(currQueue)):
            if (p[currQueue[q]] == minPriority) and q != minIndex and minIndex != 999999999:
                if atime[currQueue[minIndex]] > atime[currQueue[q]]:
                    minPriority = p[currQueue[q]]
                    minIndex = q
            elif p[currQueue[q]] <= minPriority:
                minPriority = p[currQueue[q]]
                minIndex = q

        i = currQueue[minIndex]

        timer += 1
        remainingtime[i] -= 1

        if remainingtime[i] == 0:
            completedprocesses += 1
            waitingtime[i] = timer - atime[i] - btime[i]
            if (waitingtime[i] < 0):
                waitingtime[i] = 0

        currQueue = []

    # Calculating turnaround time
    for i in range(n):
        turnaroundtime[i] = btime[i] + waitingtime[i]

        # to calculate total turnaround time and waiting time
        totalwaitingtime += waitingtime[i]
        totalturnaroundtime += turnaroundtime[i]

    # Printing Priority Scheduling
    print(
        "\nPRIORITY SCHEDULING:\nProcesses    Priority      Arrival Time    Burst Time     Waiting Time     Turn-Around Time")
    for i in range(n):
        print(" ", i + 1, "\t\t", p[i], "\t\t", atime[i], "\t\t", btime[i], "\t\t", waitingtime[i], "\t\t",
              turnaroundtime[i])

    print("\nAverage Waiting Time: %.3f " % (totalwaitingtime / n))
    print("Average Turn Around Time: ", (totalturnaroundtime / n))


# A utility function to find median of two integers
def MO2(a, b):
    return (a + b) / 2


# A utility function to find median of three integers
def MO3(a, b, c):
    return a + b + c - max(a, max(b, c)) - min(a, min(b, c))


# A utility function to find a median of four integers
def MO4(a, b, c, d):
    Max = max(a, max(b, max(c, d)))
    Min = min(a, min(b, min(c, d)))
    return (a + b + c + d - Max - Min) / 2


# Utility function to find median of single array
def medianSingle(arr, n):
    if (n == 0):
        return -1
    if (n % 2 == 0):
        return (arr[n / 2] + arr[n / 2 - 1]) / 2
    return arr[n / 2]


# This function assumes that N is smaller than or equal to M
# This function returns -1 if both arrays are empty
def findMedianUtil(A, N, B, M):
    # If smaller array is empty, return median from second array
    if (N == 0):
        return medianSingle(B, M)

    # If the smaller array has only one element
    if (N == 1):

        # Case 1: If the larger array also has one element,
        # simply call MO2()
        if (M == 1):
            return MO2(A[0], B[0])

        # Case 2: If the larger array has odd number of elements,
        # then consider the middle 3 elements of larger array and
        # the only element of smaller array. Take few examples
        # like following
        # A = {9}, B[] = {5, 8, 10, 20, 30} and
        # A[] = {1}, B[] = {5, 8, 10, 20, 30}
        if (M & 1 != 0):
            return MO2(B[M / 2], MO3(A[0], B[M / 2 - 1], B[M / 2 + 1]))

        # Case 3: If the larger array has even number of element,
        # then median will be one of the following 3 elements
        # ... The middle two elements of larger array
        # ... The only element of smaller array
        return MO3(B[M // 2], B[M // 2 - 1], A[0])

    # If the smaller array has two elements
    elif (N == 2):

        # Case 4: If the larger array also has two elements,
        # simply call MO4()
        if (M == 2):
            return MO4(A[0], A[1], B[0], B[1])

        # Case 5: If the larger array has odd number of elements,
        # then median will be one of the following 3 elements
        # 1. Middle element of larger array
        # 2. Max of first element of smaller array and element
        # just before the middle in bigger array
        # 3. Min of second element of smaller array and element
        # just after the middle in bigger array
        if (M & 1 != 0):
            return MO3(B[M / 2], max(A[0], B[M / 2 - 1]), min(A[1], B[M / 2 + 1]))

        # Case 6: If the larger array has even number of elements,
        # then median will be one of the following 4 elements
        # 1) & 2) The middle two elements of larger array
        # 3) Max of first element of smaller array and element
        # just before the first middle element in bigger array
        # 4. Min of second element of smaller array and element
        # just after the second middle in bigger array
        return MO4(B[M / 2], B[M / 2 - 1], max(A[0], B[M / 2 - 2]), min(A[1], B[M / 2 + 1]))

    idxA = (N - 1) / 2
    idxB = (M - 1) / 2

    ''' if A[idxA] <= B[idxB], then median must exist in
        A[idxA....] and B[....idxB] '''
    if (A[idxA] <= B[idxB]):
        return findMedianUtil(A + idxA, N / 2 + 1, B, M - idxA)

    ''' if A[idxA] > B[idxB], then median must exist in
    A[...idxA] and B[idxB....] '''
    return findMedianUtil(A, N / 2 + 1, B + idxA, M - idxA)


# Driver code
A = [900]
B = [5, 8, 10, 20]

N = len(A)
M = len(B)

key = (input("\nEnter secret key: \n"))
unlock_ans()
print(findMedian(A, N, B, M))
print('')