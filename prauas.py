#a
print(15%5)

#b
print (12 +3*5==75)

#c
print( "PML" + "15523" )

#d 
print( "100"+ str(234))

#e
print ((11%3)+2) != 8/2 

#######################################

p=11;q=5;r=4

#a 
print(((p-r) == (r+q)))

#b 
print (((p%3)+q)!=(r%2)) 

#c
print ((q-3)==(p%2+q)) 

#d
print ((r+q)!=((p*2)%2)) 

#e
print((((q%3)+p)>(r%2))) 

#f
print(((r+p))<=(q*5)) 


#ISIAN SINGKAT

#1
print("Honey" + "Boo"*3 )

#2
capitals = {} 
capitals['Murica'] = 'Warshington' 
capitals['Germany'] = 'Bonn' 
capitals['France'] = 'Paris' 
capitals['Engalnd'] = 'London' 
capitals['Germany'] = 'Berlin' 
print(capitals['Germany'])

#3
a="23"
b=9
print(a+str(b))


#4
letters = ["a", "b", "o", "c", "p"]

#a
print(letters[1] )

#b 
print(letters[len(letters)-2] )

#c
print(letters + ["x"] )

#d
print (letters)


#5
print(''.join('h a n d s'.split()) )

#6
#import json
#json_string = """
#[
#    {"1": "one", "2": "two", "3": "three"},
#    {"1": "un", "2": "deux", "3": "trois"},
#    {"1": "eins", "2": "zwei", "3": "drei"}
#]
#"""
#json.loads(json_string)[1][2] 
print("deux")


#7
def pembagi_indeks(nums, divisor):
    for i in range(len(nums)):
        if nums[i] % divisor == 0:
            return i
    return -1  

vals = [101, 4, 12, 24]
print("hasilnya adalah : ", pembagi_indeks(vals, 2 ))


#8
def mystery(n, m):
    p = 0
    e = 0
    while p < n:
        p = p + 1
        e = 0
    return p
print(mystery(4, 3))
    







