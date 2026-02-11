#dictionary methods
student={
    "name" : "soha" ,
    "subjects" : {
        "phy" : 99,
        "chem" : 97,
        "math" : 98,
    }
}

print(student.keys()) # return all keys
print(student.values())#return all values
print(student.items())#returns all (key,val) pairs as tuples
print(student.get("name"))#returns key according to values
print(student.update({"city": "Pune"}))
print(student)


