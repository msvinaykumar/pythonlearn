print('Enter the depth of pyramid pattern stars and press Enter.')
depth = int(input())
mid = int(depth/2)
i=mid
j=0
while(j<depth):
    print ("%s%s%s"%(' '*i,'*'*(j+1),' '*i))
    i = i - 1
    j = j + 2
