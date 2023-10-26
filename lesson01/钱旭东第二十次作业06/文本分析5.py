with open("诸葛亮4.txt","r",encoding="utf-8") as f1:
    s1=f1.readlines()
a=0    
for i in s1:
    a+=1
print(f"诸葛亮共说话{a}次")
b=0
with open("诸葛亮5.txt","r",encoding="utf-8") as f2:
    s2=f2.read()
for i in s2:
    b+=1
print(f"诸葛亮共说话{b}字")    
