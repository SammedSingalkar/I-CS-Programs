mx = [ ['M','F','H','I','K'],
           ['U','N','O','P','Q'],
           ['Z','V','W','X','Y'],
           ['E','L','A','R','G'],
           ['D','S','T','B','C']]
d={}
msg="Must see you over Cadogan West Coming at once"
for i in range(len(mx)):
    for j in range(len(mx[i])):
        if mx[i][j] not in d:
            d[mx[i][j]] = [i,j]
# print(d)
# ks = d.items()
# print(ks)

# msg = "MFMUMN"
msg = msg.upper()
m = msg.split()
ans=[]#cipher
groups=[]
for s in m:
    l=len(s)
    for i in range(0,l,2):
        ss = s[i:i+2]
        if len(ss)==1:
            ss+='X'
        groups.append(ss)
# print(groups)

for c in groups:
    x,y=c[0],c[1]
    xi,yi = d[x],d[y]
    # print(xi,yi)
    xxi,yyi = None,None
    if xi[0]==yi[0]:
        xxi = [xi[0],(xi[1]+1)%5]
        yyi = [yi[0], (yi[1]+1)%5]
    elif xi[1]==yi[1]:
        xxi = [(xi[0]+1)%5,xi[1]]
        yyi = [(yi[0]+1)%5, yi[1]]
    else:
        xxi = [xi[0],yi[1]]
        yyi = [yi[0], xi[1]]
    # print(xxi,yyi)
    ans.append(mx[xxi[0]][xxi[1]])
    ans.append(mx[yyi[0]][yyi[1]])
    # print(mx[xxi[0]][xxi[1]],mx[yyi[0]][yyi[1]])
    # print()
print("".join(ans))
# UZTBDLRZWQPZNWLGTGTUERPVZATBTQFKQLTHPODG