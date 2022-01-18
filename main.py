print("-------------------------------------------------------")

#DICTIONARY in Python

List1=[2,5,8,4]
tuple=(23,7,8,5,5)
Dict1={"Roll":31,"Name":"Vineet","Marks":77.5,"City":"Maithon"}

#to display keys
print(Dict1.keys())

#to display valus
print(Dict1.values())

#to display items
print(Dict1.items())

#change value
Dict1['City']="Mathura"
print(Dict1)

#to add value
Dict1['Mobile']=9631163320
print(Dict1)

#to delete key
del Dict1["City"]

print(Dict1)
print("-------------------------------------------------------")
#nested Dictionanry

data={"student1":{"Roll":31,"Name":"Vineet"},
        "student2":{"Roll":32,"Name":"aryan"},
        "student3":{"Roll":33,"Name":"anshu"}}
print(data)

print("-------------------------------------------------------")
print(data.keys())
print("-------------------------------------------------------")
print(data.values())
print("-------------------------------------------------------")
print(data.items())
print("-------------------------------------------------------")
print(data['student1'])
print("-------------------------------------------------------")

#deleteselected item
Dict1.pop('Marks')
print(Dict1)

print("-------------------------------------------------------")

#delete last item
Dict1.popitem()
print(Dict1)

print("-------------------------------------------------------")

#tocleardatain Dictionary
Dict1.clear()
print(Dict1)

print("-------------------------------------------------------")

#to delete dictionary
del Dict1


print("-------------------------------------------------------")

#dict Method
Dict2=dict(Roll=31,Name="Vineet",Marks=77.5,City="Maithon")
print(Dict2)
print("-------------------------------------------------------")
print(Dict2.keys())
print("-------------------------------------------------------")
print(Dict2.values())
print("-------------------------------------------------------")
print(Dict2.items())
print("-------------------------------------------------------")

print("-------------------------------------------------------")

#copy values
Dict3=Dict2.copy()
print(Dict3)

print("-------------------------------------------------------")

#getMethod

print(Dict2.get("Name"))

print("-------------------------------------------------------")

#updateMethd

Dict2.update({'Mobile':"7870153176"})
print(Dict2)

print("-------------------------------------------------------")

#keysAnd Values
keys=("K1","K2","K3")
Value=0
Dict3=dict.fromkeys(keys,Value)
print(Dict3)

print("-------------------------------------------------------")
