mat=input().split(' ')
new_value=[]
size=len(mat)
mat_set=list(set(mat))
dict1={}
for i in range (0,len(mat)):
	if mat[i]  in dict1.keys():
		val=dict1.get(mat[i])
		val1=val[-1]
		dif_val=i-val1
		answer=val[0:-1:]
		answer.extend([dif_val,i])
		dict1[mat[i]]=answer
	else:
		dict1[mat[i]]=[i+1,i]#----->[-1,i]
for i in mat_set:
	value=dict1.get(i)
	value[-1]=size-value[-1]
	new_value.append(max(value))
print(min(new_value))

