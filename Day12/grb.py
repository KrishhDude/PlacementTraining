a=str(input())
b=str(input())
x=''.join(sorted(a))
y=''.join(sorted(b))
print(x); print(y)
if(len(a)==len(b) and x==y):
    print("YES")
else:
    print("NO")