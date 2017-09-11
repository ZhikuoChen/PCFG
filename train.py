infile=open("data/input.txt",'r')
lines=infile.readlines()
infile.close()

s=[]
current=[]
results={}
buf=''
for line in lines:
    for char in line:
        #当char等于'('时，判断buf是否为空，下面会给buf赋值
        if char=='(':
            if len(buf):
                current.append(buf)
                buf=''
            s.append(current)
            current=[]
        #当char等于')'时，判断buf是否为空，下面会给buf赋值
        elif char==')':
            if len(buf):
                current.append(buf)
                buf=''
            #left表示词的标注
            left=current[0]
            if len(current) == 2:
                #right表示词
                right=current[1].lower()
            else:
                right=' '.join(current[1:])
            if not left in results:
                #如果left代表的内容不在results中，则以其内容创建一个对应的主键
                results[left]={}
            if not right in results[left]:
                #如果right代表的内容不在results中，则以其内容创建一个对应的副键
                #并且将副键right的值赋为0
                results[left][right]=0
            #若已存在，则值+1
            results[left][right]+=1
            tmp=current[0]
            #弹出列表中最后一个元素
            #这里的作用是当连续有多个')'时，从里到外求results的键以及值。
            current=s.pop(-1)
            current.append(tmp)
        #当char等于' '时，判断buf是否为空，下面会给buf赋值
        elif char==' ':
            if len(buf):
                current.append(buf)
                buf=''
        #这里会使buf不一直为空
        else:
            buf+=char
print("输出规则对应的概率:")
print(results)
outfile=open("data/model.txt", 'w')
for result in results:
    total=0
    rights=results[result]
    for right in rights:
        total+=rights[right]
    for right in rights:
        outfile.write(result+" # "+right+" # "+str(float(rights[right])/total)+'\n')
outfile.close()