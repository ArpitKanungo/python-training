''' Write a python program
Step 1: create a filename p4.py
Step 2 : read any two disks partition name from <STDIN>
Step 3 : read an individual partition size from <STDIN>
Step 4: calculate sum of partition size
Step 5: use multiline statement & display input details in below format '''

partition1 = input("Enter a disk partition: ")
size1 = int(input("Enter " + partition1 + " partition Size: "))

partition2 = input("Enter a disk partition: ")
size2 = int(input("Enter " + partition2 + " partition Size: "))

totalSize = size1 + size2

print("Partition " + partition1 + " Size : " + str(size1) + "\n" +
      "Partition " + partition2 + " Size : " + str(size2) + "\n" +
      "---------------------------------------------\n" +
      "Total Partition Size: " + str(totalSize) + "\n" +
      "------------------------------------------------")

