# python numbers
a=5
print(a,"is of type",type(a))
a=2.0
print(a,"is of type",type(a))
a=1+2j
print(a,"is complex",isinstance(1+2j,complex))

#python list

a=[1,2.2,'python']
print(a)

a=[5,10,15,20,25,30,35,40]
print("a[2] is ",a[2])
print("a[0:3] is",a[0:3])
print("a[5:]",a[5:])


a=[1,2,3]
a[2]=4
print(a)

#python strings
s="this is a string"
print(s)
s='''this is a multiline
  string'''
print(s)

s='hello world'
print("s[4]",s[4])
print("s[6:11]",s[6:11])

#python set

a={5,2,3,1,4}
print("a = ",a)
print(type(a))

#python dictonary
a={1,1,2,2,3,3}
print(a)
d={1:'value','key':2}
print(type(d))

print("d[1]",d[1])
print("d['key']=",d['key'])

#conversion between data types
a=float(5)
print(a)
a=int(10.6)
print(a)
a=int(-10.6)
print(a)

a=set([1,2,3])
print(a)

a=tuple({5,6,7})
print(a)

a=list('hello')
print(a)

a=dict([[1,2],[3,4]])
print(a)
a=dict([(3,26),(4,44)])
print(a)


