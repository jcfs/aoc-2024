R=[list(map(int,l.split()))for l in open('a')]
f=lambda r:any(all(a<=r[i+1]-r[i]<=b for i in range(len(r)-1))for a,b in[(1,3),(-3,-1)])
print(sum(f(r)for r in R),sum(f(r)or any(f(r[:i]+r[i+1:])for i in range(len(r)))for r in R))
