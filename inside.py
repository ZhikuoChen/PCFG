def inside(parses,d_A_BC,d_BC_A,words,alpha,gamma,phi,n_lenOfsen):
    #此循环表示每个非终结符->各个单词的概率
    for i in range(n_lenOfsen):
        A=[x for x in d_BC_A[words[i]]][0]  #非终结符(符号)
        parses[(i,i)].append(A)  #向[i,i]添加元素
        #A->wi 此为Inside算法
        alpha[(i,i)][A]=d_A_BC[A][words[i]]
        #此为CYK算法
        gamma[(i,i)][A]=d_A_BC[A][words[i]]
    for j in range(1,n_lenOfsen):
        for i in range(n_lenOfsen-j):
            for k in range(i,i+j):
                for B in parses[(i,k)]:
                    for C in parses[(k+1,i+j)]:
                        #' '.join((B,C))将B和C合并为一个字符串，通过空格分隔
                        As=[x for x in d_BC_A[' '.join((B,C))]]
                        if As:
                           for A in As:
                               parses[(i,i+j)].append(A)
                               #比如d_A_BC['VP']['VBD NP']  此为Inside算法
                               alpha[(i,i+j)][A] +=d_A_BC[A][' '.join((B,C))]*alpha[(i,k)][B]*alpha[(k+1,i+j)][C]
                               #此为Inside算法
                               prob=d_A_BC[A][' '.join((B,C))]*gamma[(i,k)][B]*gamma[(k+1,i+j)][C]
                               #CYK算法选择句法结构树t使其具有最大概率
                               if prob>gamma[(i,i+j)][A]:
                                  gamma[(i,i+j)][A]=prob
                                  phi[(i,i+j)][A]=(k,B,C)

