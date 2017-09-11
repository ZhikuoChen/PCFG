# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 09:40:37 2017

@author: E601
"""
def outside(parses,d_A_BC,d_BC_A,alpha,beta,n_lenOfsen):
    #'S'为句子的起始标志
    beta[(0,n_lenOfsen-1)]['S']=1.0
    for j in range(n_lenOfsen-1,-1,-1):
        for i in range(n_lenOfsen-j):
            #右侧
            for k in range(i+j,n_lenOfsen):
                for B in parses[(i,i+j)]:
                    for C in parses[(i+j+1,k)]:
                        As = [x for x in d_BC_A[' '.join((B,C))]]
                        for A in As:
                            if B!=C:
                                beta[(i,i+j)][B]+=d_A_BC[A][' '.join((B,C))]*alpha[(i+j+1,k)][C]*beta[(i,k)][A]
            #左侧
            for k in range(i):
                for C in parses[(i,i+j)]:
                    for B in parses[(k,i-1)]:
                        As=[x for x in d_BC_A[' '.join((B,C))]]
                        for A in As:
                            if B!=C:
                               #这里的beta[(i,i+j)][C]和上面的beta[(i,i+j)][B]可能代表同一内容
                               beta[(i,i+j)][C]+=d_A_BC[A][' '.join((B,C))] * alpha[(k,i-1)][B]*beta[(k,i+j)][A]
