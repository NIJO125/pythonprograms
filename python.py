import random

# You may change the deufalt:
array_len = 6

# Acquire random numbers
def create_random_array():
  print("Acquire", array_len, "random numbers.")
  arr = []
  for i in range(array_len):
    arr.append(random.randint(0, 50))

  return arr


#
# This function bubble sorts the given list
#
def sort(arr):
   size = len(arr)
   for i in range(1, size):
      for j in range(i, size):
         if arr[i - 1] > arr[j]:
            temp = arr[i - 1]
            arr[i - 1] = arr[j]
            arr[j] = temp

   # Thats it
   return arr


# These are random unsorted numbers
ls = create_random_array()

print ("\U0001f600 Unsorted list:\n" ,ls)

# SORTING THE LIST...
ls = sort(ls)

print("\n\U0001f600 Sorted list:\n", ls)

print ("\n\U0001f602 You are welcome to UpVote \U0001f640")

