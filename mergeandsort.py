# merge and sort by aviraj

lst1 = [7,2,5]
lst2 = [3,9,1]

def merg(a,b):
  res = []
 for i in a:
    res.append(i)
 for j in b:
   res.append(j)
  # now try to sort by merge-like approach
def mergesort(x):
 if len(x) <=1:
    return x
 mid = len(x)//2
 left = mergesort(x[:mid])
 right = mergesort(x[mid:])
 # merge
 i=j=0
 out = []
 while i < len(left) and j < len(right):
    if left[i] < right[j]:
      out.append(left[i])
      i +=1
    else:
     out.append(right[j])
      j +=1
 while i < len(left):
  out.append(left[i])
  i+=1
 while j < len(right):
   out.append(right[j])
   j+=1
 return out

print('original1 =', lst1)
print('original2 =', lst2)
merged = merg(lst1,lst2)
print('merged (raw) =', merged)
print('sorted =', mergesort(merged))
