t1=(10,14,17,"icecream",17.7,"milkshake")
t2=(12,14,16,18,20)

print("t1 : ",t1)
print("t2 : ",t2,"\n")

print("         TUPLE OPERATIONS            ")
print("--------------------------------------")

print("\n1. datatype \n2. no.of.elements \n3. repeat the elements \n4. element at the index \n5. unpacking the element \n6. concatenation \n7. remove first element \n8. print all characters except last 5 characters \n9. display last element of the t1 \n10. reversed the order of  t1 \n11. fetch middle elements of t1 \n12. fetch portion of an element \n13. maximum of elements in t2 \n14. minimum of elements in t2 \n15. sum of all elements in t2 \n16. sort the tuple t2 \n17. reverse sorting the tuple t2 \n18. delete a tuple \n19. convert into immutable sequence of elements")
n=int(input("\nenter your choice : "))

if(n==1):
  print("datatype of t1 : ",type(t1))
  print("datatype of t2 : ",type(t2))
elif(n==2):
  print("no of elements in t1 : ",len(t1))
  print("no of elements in t2 : ",len(t2))
elif(n==3):
  r=str(input("enter the tuple to be repeated : "))
  rn=int(input("enter no of times the tuple to be repeated : "))
  if(r=='t1'):
    print("tuple1 repeatation : ",t1*rn)
  else:
    print("tuple2 repeatation : ",t2*rn)
elif(n==4):
  t=str(input("enter the tuple name : "))
  i=int(input("enter the index value : "))
  if(t=='t1'):
    print("element at index ",i," is : ",t1[i])
  else:
    print("element at index ",i," is : ",t2[i])
elif(n==5):
  a,b,c,d,e,f=t1
  print("unpacked the elementsin t1 : ",a,b,c,d,e,f)
elif(n==6):
  print("concatenated the tuples, t1 and t2 : ",t1+t2)
elif(n==7):
  print("removed the first element of t1 : ",t1[1:])
elif(n==8):
  print("all elements expect the last 5 of t1 : ",t1[:-5])
elif(n==9):
  print("last element of tuple t1 : ",t1[-1])
elif(n==10):
  print("reversed the order of tuple : ",t1[::-1])
elif(n==11):
  print("elements from 2 to 5 : ",t1[2:6])
elif(n==12):
  print("portion of an element : ",t1[3][:5])
elif(n==13):
  print("maximum of elements in tuple t2 is : ",max(t2))
elif(n==14):
  print("minimum of elements in tuple t2 is : ",min(t2))
elif(n==15):
  print("sum of elements in tuple t2 is : ",sum(t2))
elif(n==16):
  print("sorted t2 : ",sorted(t2))
elif(n==17):
  print("reverse sorting of t2 : ",sorted(t2,reverse=True))
elif(n==18):
  del t2
  print("t2 is deleted : ",t2)
elif(n==19):
  strv="python programming"
  print("datatype of strv is : ",type(strv))
  t3=tuple(strv)
  print("converted into immutable sequence of elements : ",type(t3))
else:
  print("Invalid number")

