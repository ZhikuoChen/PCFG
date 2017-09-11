def tree(words, Note, S, l, r):
    if l==r:
        return '('+S+' '+words[l]+')'
    num,left,right=Note[(l,r)][S]
    L=tree(words,Note,left,l,num)
    R=tree(words,Note,right,num+1,r)
    return '('+S+L+R+')'
