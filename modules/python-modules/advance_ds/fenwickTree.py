
def fenwickGet(ump,index):
    n=len(ump);sm=ump[0]
    while index>0:
        sm+=ump[index]
        index-=(index&(-index))
    return sm
    pass
def fenwickUpdate(ump,index,delta):
    n=len(ump)
    if index==0:ump[index]+=delta;return
    while index<n:
        ump[index]+=delta
        index+=(index&(-index))
    pass
