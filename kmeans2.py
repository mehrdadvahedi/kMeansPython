import random as rn

a = [2, 4, 10, 12, 3, 20, 30, 11, 25]
k = 2
n = len(a)

mu = []
mu.append(a[rn.randint(-1, n-1)])
for i in range(1, k):
    while True:
        t = a[rn.randint(-1, n-1)]
        end = True
        for j in range(len(mu)):
            if t == mu[j]:
                end = False
        if end:
            break
    mu.append(t)

branch = []
for i in range(k):
    branch.append([mu[i]])


def addBranch(branch, mu, ai):
    save = 0
    Min = mu[0]
    for i in range(len(mu)):
        mean = mu[i]
        if Min >= abs(mean-ai):
            Min = abs(mean-ai)
            save = i
    for i in range(len(branch)):
        if ai in branch[i]:
            branch[i].remove(ai)
    branch[save].append(ai)


def updateMu(kh, mu):
    for i in range(len(mu)):
        if len(kh[i]) == 0:
            continue
        mtemp = 0
        l = 0
        for temp in kh[i]:
            l += 1
            mtemp += temp
        mtemp /= l
        mu[i] = mtemp


def updateEnd(kh):
    end = []
    for i in range(len(kh)):
        t = []
        for j in range(len(kh[i])):
            t.append(kh[i][j])
        end.append(t)
    return end


print(a)
print(branch)
print(mu)
print((50*'*'), '\n')

while True:
    end = updateEnd(branch)
    # print(end)
    for i in range(n):
        addBranch(branch, mu, a[i])
    updateMu(branch, mu)
    if end == branch:
        break
    print('a:', a)
    print('branch: ', branch)
    print('mu: ', mu)
    print((50*'*'), '\n')


# out ->
# [2, 4, 10, 12, 3, 20, 30, 11, 25]
# [[25], [20]]
# [25, 20]
# **************************************************

# a: [2, 4, 10, 12, 3, 20, 30, 11, 25]
# branch:  [[30, 25], [2, 4, 10, 12, 3, 20, 11]]
# mu:  [27.5, 8.857142857142858]
# **************************************************

# a: [2, 4, 10, 12, 3, 20, 30, 11, 25]
# branch:  [[20, 30, 25], [2, 4, 10, 12, 3, 11]]
# mu:  [25.0, 7.0]
# **************************************************