print("Hello world!")
# python
cash = [-200, 90, 90, 90]
r = 0.10
npv = sum(cf / (1 + r) ** t for t, cf in enumerate(cash))
print(f"NPV = {npv:.2f}") # NPV = 23.82


print("Hello world!")
cash = [-200, 90, 90, 90]
for t, cf in enumerate(cash):
    print(f"t={t}, cf={cf}")
# t=0, cf=-200
# t=1, cf=90

for t in range(10):
    print(t)
print(list(range(10)))
for t in list(range(10)):
    print(t)

# question 3
######################
# 正确的代码实现
r = 0.08
# 定义复利系数表
df = [round(1/(1+r)**t,4) for t in range(13)]
print("df = ", df)
# 定义现金流量
A = [-6000,2300,2300,-3700,2300,2300,-3700,2300,2300,-3700,2300,2300,2300]
B = [-8000,3100,3100,3100,-4700,3100,3100,3100,-4700,3100,3100,3100,3300]
C = [-10000,2800,2800,2800,2800,2800,-6850,2800,2800,2800,2800,2800,3150]

# 定义NPV计算函数
def npv(cf): 
    return sum(cf[t]*df[t] for t in range(len(cf)))

# 分别计算每个方案的NPV
print("NPV_A =", round(npv(A),2)) # -212.53
print("NPV_B =", round(npv(B),2)) # 5493.93
print("NPV_C =", round(npv(C),2)) # 5158.87



for num in (1, 2, 3):     #循环，成员遍历
    for latter in['a', 'b', 'c']:
        print("num = ", num, " latter = ", latter)


