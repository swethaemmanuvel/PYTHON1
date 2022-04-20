print("----------------------")
print("list operations")
print("----------------------")
l1=[12,13,5,"chips","mango",13]
l2=[73,63,33,23]
print("list 1 elements : ",l1)
print("list 2 elements : ",l2)
print(" 1. Append\n 2.insert\n 3.extend\n 4.remove\n 5.pop\n 6.reverse\n 7.maximum\n 8.minimum\n 9.count\n 10.sorted\n 11.find index\n 12.concatenate two list\n 13.repeatation\n 14.len\n 15.clear\n")

c=int(input("enter your choice : "))

if c==1:
  l1.append("icecream")
  print("appended an element : ",l1)
elif c==2:
  l1.insert(1,"blue")
  print("inserted an element : ",l1)
elif c==3:
  l1.extend(["value1","value2"])
  print("extent : ",l1)
elif c==4:
  l1.remove("chips")
  print("removed an element : ",l1)
elif c==5:
  l1.pop(4)
  print("poped an element : ",l1)
elif c==6:
  l1.reverse()
  print("reversed list order : ",l1)
elif c==7:
  print("maimum value in list2 : ",max(l2))
elif c==8:
  print("minimum value in list2 : ",min(l2))
elif c==9:
  print("count of 3 in list1 : ",l1.count(3))
elif c==10:
  l2.sorted()
  print("sorted list2",l2)
elif c==11:
  print("index of element 5 in list1 : ",l1.index(5))
elif c==12:
  print("concatenation of list1 and list2 : ",l1+l2)
elif c==13:
  print("repetatin of list 1 (2time) : ",l1*2);
elif c==14:
  print("lenght of the list 1 : ",len(l1))
elif c==15:
  print("elements in list1 (cleared) : ",l1.clear())
else:
  print("invalid number");
