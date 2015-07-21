array=[3,2,4,2,2,2,2]
win = 3
marray=[]
head = 0
tail = 0

print "start moving..."
maxi = tail
maxj = tail
print 'array =',array
#print  'head', head, 'tail', tail, "maxi", array[maxi], 'maxj', array[maxj]


for i in range(0, len(array)-1):
    #print "move"
    if tail >= win-1 and head !=len(array)-1: head = head+1
    if tail< len(array)-1: tail += 1


    # out of window
    if head > maxi and head > maxj:
        maxi = head
        maxj = head
    if head > maxi and head <=maxj:
        maxi = maxj

    # in window
    if array[tail] > array[maxj]: maxj = tail
    if array[maxi] < array[maxj]: maxi = maxj

    if tail >= win-1:
        marray.append(array[maxi])

'''
    print 'head', head,\
          'tail', tail, \
          "maxi index is",  maxi, 'value is',array[maxi],\
          "maxj index is",  maxj, 'value is',array[maxj]
'''
print 'marray=',marray
