import statistics as st
count=int(input())
pp=list(map(int,input().split()))
qq=False
for r in range(1,count):
    l1=pp[:r]
    l2=pp[r:]
    if st.mean(l1)==st.mean(l2):
        qq=True
if qq==True:
    print("yes")
else:
    print("no")
