n = input()
s = raw_input()
l = raw_input().split()
l1 = [x for x in range(len(s)-1) if s[x] == 'R' and s[x+1]=='L']
d = [int(l[i+1]) - int(l[i])for i in l1]
if len(d): print min(d)/2
else:
	print -1