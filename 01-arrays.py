#! /usr/bin/python3
import math

# test arrays
hollow_test_arrays = [
   [1, 2, 0, 0, 0, 3, 4],
   [1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 1, 2, 18],
   [1, 2, 0, 0, 3, 4],
   [1, 2, 0, 0, 0, 3, 4, 5],
   [3, 8, 3, 0, 0, 0, 3, 3],
   [1, 4, 2, 0, 0, 0, 3, 4, 0],
   [0, 1, 2, 0, 0, 0, 3, 4],
   [0, 0, 0]
]

flip_flop_test_arrays = [
   [],
   [2],
   [2, 2, 3, 4],
   [1, 2, 3, 3, 4],
   [2],
   [0, 3, 4, -7],
   [1, 2, 3, 4]
]

balanced_test_arrays = [
   [2, 3, 6, 7],
   [6, 3, 2, 7],
   [6, 7, 2, 3, 12],
   [6, 7, 2, 3, 14, 95],
   [7, 15, 2, 3],
   [16, 6, 2, 3],
   [2],
   [3],
   []
]

odd_heavy_test_arrays = [
   [1],
   [2],
   [1, 1, 1, 1, 1, 1],
   [2, 4, 6, 8, 11],
   [-2, -4, -6, -8, -11],
   [16, 6, 37, 2, 3],
   []
]

cumulative_test_arrays = [
   [],
   [1],
   [0, 0, 0, 0, 0, 0],
   [1, 1, 1, 1, 1, 1],
   [3, 3, 6, 12, 24],
   [-3, -3, -6, -12, -24],
   [-3, -3, 6, 12, 24]
]

centered_test_arrays = [
   [1, 2, 3, 4, 5],
   [3, 2, 1, 4, 5],
   [3, 2, 1, 4, 1],
   [3, 2, 1, 1, 4, 6],
   [1],
   []
]

layered_test_arrays = [
   [1, 1, 2, 2, 2, 3, 3],
   [3, 3, 3, 3, 3, 3, 3],
   [1, 2, 2, 2, 3, 3],
   [2, 2, 2, 3, 3, 1, 1],
   [2, 2, 2, 2],
   [2, 2, 2],
   [2, 1],
   [2],
   []
]

daphne_test_arrays = [
   [1, -3, 5, -6],
   [-3, 5, -6],
   [1, -3, 5],
   [-3, 5],
   [-3],
   [5],
   [1, 1, -3, 5],
   [-2, -2, -2],
   [1, -1, 2, 2],
   []
]

dual_test_arrays = [
   [1, 2, 3, 0],
   [1, 2, 2, 1, 3, 0],
   [1, 1, 2, 2],
   [1, 2, 1],
   [1, 2],
   []
]

cucumber_test_arrays = [
   [3, 8, 12],
   [1, 3, 15],
   [3, 4, 12, 11]
]

odd_dominated_test_arrays = [
   [],
   [1],
   [2],
   [3, 5, 7, 2],
   [ 2, 1, 3, 4, 5, 6],
   [ 2, 4, 6, 10, 12, 14]
]


# hollow array
def is_hollow(a, length):
   if length < 3:
      return False
   
   no_of_elements_before_first_zero = 0
   zero_count_ended = False
   zero_count_ended_at_index = 0;

   first_zero_found = False
   no_of_zeros_found = 0

   for i in range(0, length):
      if a[i] != 0 and not first_zero_found:
         no_of_elements_before_first_zero += 1
      elif a[i] != 0 and (first_zero_found and not zero_count_ended):
         zero_count_ended = True
         zero_count_ended_at_index = i
      elif zero_count_ended and a[i] == 0:
         return False 
      elif a[i] == 0:
         if not first_zero_found:
            first_zero_found = True

         no_of_zeros_found += 1
   
   # no_of_elements_after_last_zero = (length - zero_count_ended_at_index) if zero_count_ended else 0
   no_of_elements_after_last_zero = 0
   if zero_count_ended:
      no_of_elements_after_last_zero = length - zero_count_ended_at_index

   return no_of_zeros_found >= 3 and no_of_elements_before_first_zero == no_of_elements_after_last_zero

# flip-flop array
def is_flip_flop(a, length):
   if length <= 1:
      return False

   first_is_even = (a[0] % 2 == 0)
   check_next_even = not first_is_even

   for i in range(1, length):
      if check_next_even and (a[i] % 2 != 0):
         return False
      elif (not check_next_even) and (a[i] % 2 == 0):
         return False
      
      check_next_even = not check_next_even
   
   return True

# balanced array
def is_balanced(a, length):
   if length == 0:
      return True

   first_is_even = (a[0] % 2 == 0)

   if not first_is_even:
      return False

   check_next_is_even = False
   for i in range(1, length):
      if check_next_is_even and (a[i] % 2 != 0):
         return False
      elif (not check_next_is_even) and (a[i] % 2 == 0):
         return False
      
      check_next_is_even = not check_next_is_even
   
   return True

# odd-heavy array
def is_odd_heavy(a, length):
   if length == 0:
      return False

   first_is_even = (a[0] % 2 == 0)
   if first_is_even:
      # if the first element is even
      return False
   elif (not first_is_even) and length == 1:
      # if the first element is odd and if it is the only element
      return True

   max_even = 0
   min_odd = a[0]

   for i in range(1, length):
      i_is_even = (a[i] % 2 == 0);
      if i_is_even and a[i] > max_even:
         max_even = a[i]
      elif (not i_is_even) and a[i] < min_odd:
         min_odd = a[i]
   
   return min_odd > max_even

# cumulative array
def is_cumulative(a, length):
   if length < 2:
      return False

   for i in range(1, length):
      all_previous_elements_sum = 0

      for j in range(0, i):
         all_previous_elements_sum += a[j];
   
      if all_previous_elements_sum != a[i]:
         return False
   
   return True

# centered array
def is_centered(a, length):
   if length % 2 == 0:
      # if number of elements is even (including 0), since there will be no middle element
      return False
   
   if length == 1:
      # satisfies the condition vacuously
      return True
   
   middle_element_index = math.floor(length / 2)
   middle_element = a[middle_element_index]
   
   # find the minimum element excluding the middle element
   min_element = a[0];
   for i in range(1, length):
      if i == middle_element_index:
         continue

      if a[i] < min_element:
         min_element = a[i]
   
   # note: strictly less than
   return middle_element < min_element
   
# layered array
def is_layered(a, length):
   if length < 4:
      # since each element should appear two or more times
      return False
   
   current_element = a[0]
   current_element_count = 1

   for i in range(1, length):
      if current_element_count < 2 and a[i] != current_element:
         return False
      elif a[i] == current_element:
         current_element_count += 1
      else:
         if a[i] < current_element:
            # since not in ascending order
            return False
         else:
            current_element = a[i]
            current_element_count = 1
   
   # check if the last element appeared two or more times
   # (if the code reached this part without returning)
   return current_element_count >= 2

# daphne array
def is_daphne(a, length):
   if length == 0:
      return False
   elif length == 1:
      return True
   
   first_is_positive = a[0] > 0;
   check_next_positive = not first_is_positive

   for i in range(1, length):
      if check_next_positive and a[i] < 0:
         return False
      elif not check_next_positive and a[i] > 0:
         return False
      
      check_next_positive = not check_next_positive

   return True

# dual array
def is_dual(a, length):
   if length % 2 != 0:
      # since array should have even number of elements
      return False

   if length == 0:
      return True
   
   first_pair_sum = a[0] + a[1]

   for i in range(2, length, 2):
      current_pair_sum = a[i] + a[i+1]
      if current_pair_sum != first_pair_sum:
         return False
   
   return True

# cucumber array
def is_cucumber(a, length):
   if length < 2:
      return False
   
   pair_found = False

   for i in range(0, length):
      for j in range(i+1, length):
         if (a[j] + a[i]) == 15:
            if pair_found:
               return False
            else:
               pair_found = True

   return pair_found

def is_odd_dominated(a, length):
   if length == 0:
      return False
   
   no_of_evens = 0
   no_of_odds = 0

   for i in range(0, length):
      if a[i] % 2 == 0:
         no_of_evens += 1
      else:
         no_of_odds += 1
   
   if no_of_odds > no_of_evens:
      return True
   else:
      return False


testing_types = [
   "hollow",
   "flip-flop",
   "balanced",
   "odd-heavy",
   "cumulative",
   "centered",
   "layered",
   "daphne",
   "dual",
   "cucumber",
   "odd-dominated"
]

## testing
def test(test_for_type):
   if test_for_type == "hollow":
      for test_array in hollow_test_arrays:
         print(is_hollow(test_array, len(test_array)))
   elif test_for_type == "flip-flop":
      for test_array in flip_flop_test_arrays:
         print(is_flip_flop(test_array, len(test_array)))
   elif test_for_type == "balanced":
      for test_array in balanced_test_arrays:
         print(is_balanced(test_array, len(test_array))) 
   elif test_for_type == "odd-heavy":
      for test_array in odd_heavy_test_arrays:
         print(is_odd_heavy(test_array, len(test_array)))        
   elif test_for_type == "cumulative":
      for test_array in cumulative_test_arrays:
         print(is_cumulative(test_array, len(test_array)))
   elif test_for_type == "centered":
      for test_array in centered_test_arrays:
         print(is_centered(test_array, len(test_array)))
   elif test_for_type == "layered":
      for test_array in layered_test_arrays:
         print(is_layered(test_array, len(test_array)))
   elif test_for_type == "daphne":
      for test_array in daphne_test_arrays:
         print(is_daphne(test_array, len(test_array)))
   elif test_for_type == "dual":
      for test_array in dual_test_arrays:
         print(is_dual(test_array, len(test_array)))
   elif test_for_type == "cucumber":
      for test_array in cucumber_test_arrays:
         print(is_cucumber(test_array, len(test_array)))   
   elif test_for_type == "odd-dominated":
      for test_array in odd_dominated_test_arrays:
         print(is_odd_dominated(test_array, len(test_array)))   
   else:
      print("incorrect testing type")

## run test for the last testing type
test(testing_types[-1]);