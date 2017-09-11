from collections import defaultdict
from inside import inside
from outside import outside
from tree import tree

d_A_BC=defaultdict(lambda: defaultdict(float))
d_BC_A=defaultdict(lambda: defaultdict(float))

#alpha用于存储内向算法中对应的概率值
alpha=defaultdict(lambda: defaultdict(float))
#beta用于存储外向算法中对应的概率值
beta=defaultdict(lambda: defaultdict(float))

#gamma用于存储CYK算法中对应的概率值
gamma=defaultdict(lambda: defaultdict(float))
#phi用于存储CYK算法中对应的句法结构树
phi=defaultdict(lambda: defaultdict(float))

infile=open("data/model.txt",'r')
lines=infile.readlines()
for line in lines:
    l,r,prob=tuple(line.split(" # "))
    d_A_BC[l][r]=float(prob)    #l为非终结符，r为终结符或非终结符
    d_BC_A[r][l]=float(prob)
infile.close()
#for key1 in sorted(d_A_BC()):
#    for key2 in d_A_BC[key1].keys():
#        print(key2,d_A_BC[key1][key2])
sentence="A boy saw a girl with a telescope"
words=sentence.lower().split(' ')
length=len(words)
#此字典键对应的值为列表
parses=defaultdict(list)
#PCFG第一个问题
inside(parses,d_A_BC,d_BC_A,words,alpha,gamma,phi,length)
print("在给定句子和文法G的情况下,P(W|G)为:",alpha[(0,length-1)]['S'])
#PCFG第二个问题
print("在给定句子和文法G的情况下,最合理的句法树为:")
print(tree(words,phi,'S',0,length-1))
print("该句法树的最大概率为:",gamma[(0,length-1)]['S'])

outside(parses,d_A_BC,d_BC_A,alpha,beta,length)

output=open("data/output.txt",'w')
output.write(tree(words,phi,'S',0,length-1) + '\n')
output.write(str(gamma[(0,length-1)]['S']) + '\n')
output.write("Pos"+' # '+'Num'+' # '+'Num'+' # '+'Prob'+' # '+'Prob'+'\n')
results=[]
#i为(0, 0)等数字
for i in parses:
    #j为'DT'等符号
    for j in parses[i]:
        if beta[i][j]:
            results.append(str(j)+' # '+str(i[0]+1)+' # '+str(i[1]+1)+' # '+str(alpha[i][j])+' # '+str(beta[i][j]))
#对results列表进行排序
results.sort()

for result in results:
    output.write(result+'\n')
output.close()