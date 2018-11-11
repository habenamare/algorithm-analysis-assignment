#! /usr/bin/python3

geez_one = "፩"
geez_two = "፪"
geez_three = "፫"
geez_four = "፬"
geez_five = "፭"
geez_six = "፮"
geez_seven = "፯"
geez_eight = "፰"
geez_nine = "፱"
geez_ten = "፲"
geez_twenty = "፳"
geez_thirty = "፴"
geez_forty = "፵"
geez_fifty = "፶"
geez_sixty = "፷"
geez_seventy = "፸"
geez_eighty = "፹"
geez_ninty = "፺"
geez_hundred = "፻"
geez_ten_thousand = "፼"

geez_numeral_characters = [
   geez_one,
   geez_two,
   geez_three,
   geez_four,
   geez_five,
   geez_six,
   geez_seven,
   geez_eight,
   geez_nine,
   geez_ten,
   geez_twenty,
   geez_thirty,
   geez_forty,
   geez_fifty,
   geez_sixty,
   geez_seventy,
   geez_eighty,
   geez_ninty,
   geez_hundred,
   geez_ten_thousand
]

arabic_numeral_characters = [
   "0",
   "1",
   "2",
   "3",
   "4",
   "5",
   "6",
   "7",
   "8",
   "9",
]

def one_digit_geez_numeral_to_arabic(one_digit_geez_numeral):
   if one_digit_geez_numeral == geez_one:
      return 1;
   elif one_digit_geez_numeral == geez_two:
      return 2;
   elif one_digit_geez_numeral == geez_three:
      return 3;
   elif one_digit_geez_numeral == geez_four:
      return 4;
   elif one_digit_geez_numeral == geez_five:
      return 5;
   elif one_digit_geez_numeral == geez_six:
      return 6;
   elif one_digit_geez_numeral == geez_seven:
      return 7;
   elif one_digit_geez_numeral == geez_eight:
      return 8;
   elif one_digit_geez_numeral == geez_nine:
      return 9;
   elif one_digit_geez_numeral == geez_ten:
      return 10;
   elif one_digit_geez_numeral == geez_twenty:
      return 20;
   elif one_digit_geez_numeral == geez_thirty:
      return 30;
   elif one_digit_geez_numeral == geez_forty:
      return 40;
   elif one_digit_geez_numeral == geez_fifty:
      return 50;
   elif one_digit_geez_numeral == geez_sixty:
      return 60;
   elif one_digit_geez_numeral == geez_seventy:
      return 70;
   elif one_digit_geez_numeral == geez_eighty:
      return 80;
   elif one_digit_geez_numeral == geez_ninty:
      return 90;
   elif one_digit_geez_numeral == geez_hundred:
      return 100;
   elif one_digit_geez_numeral == geez_ten_thousand:
      return 10000;

def arabic_to_one_digit_geez_numeral(arabic_number):

   if arabic_number == 1:
      return geez_one;
   elif arabic_number == 2:
      return geez_two;
   elif arabic_number == 3:
      return geez_three;
   elif arabic_number == 4:
      return geez_four;
   elif arabic_number == 5:
      return geez_five;
   elif arabic_number == 6:
      return geez_six;
   elif arabic_number == 7:
      return geez_seven;
   elif arabic_number == 8:
      return geez_eight;
   elif arabic_number == 9:
      return geez_nine;
   elif arabic_number == 10:
      return geez_ten;
   elif arabic_number == 20:
      return geez_twenty;
   elif arabic_number == 30:
      return geez_thirty;
   elif arabic_number == 40:
      return geez_forty;
   elif arabic_number == 50:
      return geez_fifty;
   elif arabic_number == 60:
      return geez_sixty;
   elif arabic_number == 70:
      return geez_seventy;
   elif arabic_number == 80:
      return geez_eighty;
   elif arabic_number == 90:
      return geez_ninty;
   elif arabic_number == 100:
      return geez_hundred;
   elif arabic_number == 10000:
      return geez_ten_thousand;

def arabic_to_simple_geez_numerals(arabic_number):
   if arabic_number <= 0 and arabic_number >= 101:
      # not expected value
      return ""

   if arabic_number >= 1 and arabic_number <= 9:
      return arabic_to_one_digit_geez_numeral(arabic_number)
   
   if arabic_number % 10 == 0:
      return arabic_to_one_digit_geez_numeral(arabic_number)
   else:
      tenth_number = arabic_number - (arabic_number % 10)
      ones_number = arabic_number % 10;

      return arabic_to_one_digit_geez_numeral(tenth_number) + arabic_to_one_digit_geez_numeral(ones_number)

def simple_geez_numerals_to_arabic(simple_number_in_geez):
   if geez_hundred in simple_number_in_geez or geez_ten_thousand in simple_number_in_geez:
      return "not simple number, simple number doesn't contain the hundred or the ten thousand characters"

   if len(simple_number_in_geez) != 2:
      if len(simple_number_in_geez) == 1:
         return one_digit_geez_numeral_to_arabic(simple_number_in_geez)
      else:
         return "not expected simple number, expecting simple number which is one or two digits not containing the hundred and ten thousand characters"  

   first_char = simple_number_in_geez[0]
   second_char = simple_number_in_geez[1]

   return one_digit_geez_numeral_to_arabic(first_char) + one_digit_geez_numeral_to_arabic(second_char)


def is_hundred(digit_character):
   return digit_character == geez_hundred

def is_ten_thousand(digit_character):
   return digit_character == geez_ten_thousand

# def multiply_hundreds_and_ten_thousands(sequential_hundreds_and_ten_thousands):
#    multiplied_value = 1
#    for digit in sequential_hundreds_and_ten_thousands:
#       if is_hundred(digit):
#          multiplied_value *= 100
#       elif is_ten_thousand(digit):
#          multiplied_value *= 10000

#    return multiplied_value

def add_to_pair(thePair, digit, powerOfTenThousand, powerOfHundred, sequential_ten_thousand = False):
   multiplier = 0

   if powerOfTenThousand == 0 and powerOfHundred == 0:
      multiplier = 1
   elif powerOfTenThousand == 0 and powerOfHundred == 1:
      multiplier = 100
   elif powerOfTenThousand > 0 and powerOfHundred == 0:
      if sequential_ten_thousand:
         multiplier = (10000 ** powerOfTenThousand) * 100
      else:
         multiplier = (10000 ** powerOfTenThousand)
   elif powerOfTenThousand > 0 and powerOfHundred > 0:
      multiplier = (10000 ** powerOfTenThousand) * (100 ** powerOfHundred)

   thePair.append([digit, multiplier])

def geez_numerals_to_arabic(number_in_geez):

   if number_in_geez == geez_ten_thousand:
      return 10000

   digit_multiply_by_pair = []

   current_digits = ""
   sequential_hundreds_and_ten_thousands = ""

   # note, here by power if it is 0 we mean 0 not 1
   power_of_ten_thousand = 0
   power_of_hundred = 0

   last_digit_was_ten_thousand = False
   # enumerate from the end of the string
   for i, digit in enumerate(reversed(number_in_geez)):
      if not is_hundred(digit) and not is_ten_thousand(digit):
         current_digits += digit
         last_digit_was_ten_thousand = False
      else:
         is_last_item = (i + 1) == len(number_in_geez)


         if is_last_item and is_hundred(digit):
            add_to_pair(digit_multiply_by_pair, "last_is_hundred", power_of_ten_thousand, power_of_hundred)
         elif is_last_item and is_ten_thousand(digit):
            last_digit_was_ten_thousand = True

            if len(number_in_geez) == 1:
               # special case of being "፼"
               add_to_pair(digit_multiply_by_pair, "last_is_ten_thousand", power_of_ten_thousand, power_of_hundred, last_digit_was_ten_thousand)
            else:
               add_to_pair(digit_multiply_by_pair, "last_is_ten_thousand", power_of_ten_thousand, power_of_hundred, last_digit_was_ten_thousand)
         elif is_hundred(digit):
            if len(current_digits) > 0 and not is_hundred(current_digits[-1]) and not is_ten_thousand(current_digits[-1]):
               # make sure previous digit was not a hundred or thousand
               reversed_current_digit = current_digits[::-1]
               add_to_pair(digit_multiply_by_pair, reversed_current_digit, power_of_ten_thousand, power_of_hundred)
               print("length", len(digit_multiply_by_pair))
               current_digits = ""

            if power_of_ten_thousand == 0 and power_of_hundred == 0:
               power_of_hundred = 1
            elif power_of_ten_thousand > 0:
               # if power of ten thousand is greater than 0
               power_of_hundred = 1
         elif is_ten_thousand(digit):
            last_digit_was_ten_thousand = True

            if len(current_digits) > 0 and not is_hundred(current_digits[-1]) and not is_ten_thousand(current_digits[-1]):
               reversed_current_digit = current_digits[::-1]
               add_to_pair(digit_multiply_by_pair, reversed_current_digit, power_of_ten_thousand, power_of_hundred)
               current_digits = ""

            power_of_ten_thousand += 1
            power_of_hundred = 0

      print(i, "->", digit)


   if current_digits != "":
      
      #power_of_hundred -= 1 # this made it work for above billion but does not work for under billion


      reversed_current_digit = current_digits[::-1]
      print("last power of ten", power_of_ten_thousand, "last power of hund", power_of_hundred)
      add_to_pair(digit_multiply_by_pair, reversed_current_digit, power_of_ten_thousand, power_of_hundred)


   final_number = 0
   for pair in digit_multiply_by_pair:
      print(pair)
      digit = pair[0]
      digit_number = 0

      multiply_by = pair[1]

      if digit == "":
         digit_number = 0
      elif digit == "last_is_hundred" or digit == "last_is_ten_thousand":
         digit_number = 1
         multiply_by *= 100
      else:
         digit_number = simple_geez_numerals_to_arabic(digit)
      
      final_number += digit_number * multiply_by
   
   return final_number

def arabic_to_geez_numerals(arabic_number):
   final_geez_numerals = ""

   arabic_number_string = str(arabic_number)

   # split arabic number string from the left, so that each split contains two characters
   # note: if the length of the string is odd the first split will be a single character
   arabic_number_split = []
   print(arabic_number_split)
   start_loop_from = 0

   if len(arabic_number_string) % 2 != 0:
      # length of string is odd
      arabic_number_split.append(arabic_number_string[0])
      start_loop_from = 1

   for i in range(start_loop_from, len(arabic_number_string), 2):
      if (i + 1) == len(arabic_number_string):
         # if this is the last index
         digit = arabic_number_string[i]
         arabic_number_split.append(digit)
      else:
         digit = arabic_number_string[i] + arabic_number_string[i + 1]
         arabic_number_split.append(digit)

   print("the split", arabic_number_split)
   
   if len(arabic_number_split) == 1:
      arabic_number_int = int(arabic_number_split[0])
      final_geez_numerals += arabic_to_simple_geez_numerals(arabic_number_int)
   else:
      next_to_be_added_is_hundred = False

      if len(arabic_number_split) % 2 == 0:
         next_to_be_added_is_hundred = True
      else:
         next_to_be_added_is_hundred = False


      last_geez_digit_was_zero = False

      for i in range(0, len(arabic_number_split)):
         arabic_number_int = int(arabic_number_split[i])
 
         geez_digit = ""
         if i == 0 and arabic_number_int == 1:
            # if this is the first index and it contains only '1'
            # i.e. special case for numbers that start with 1
            geez_digit = ""
            last_geez_digit_was_zero = False
         elif arabic_number_int == 0:
            geez_digit = ""
            last_geez_digit_was_zero = True
         else:
            geez_digit = arabic_to_simple_geez_numerals(arabic_number_int)
            last_geez_digit_was_zero = False
         
         # WORKING on Nov 11, 2018
         # geez_digit = arabic_to_simple_geez_numerals(arabic_number_int)
         # if i == 0 and arabic_number_int == 1:
         #    # if this is the first index and it contains only '1'
         #    # i.e. special case for numbers that start with 1
         #    geez_digit = ""
         #    last_geez_digit_was_zero = False
         # elif arabic_number_int == 0:
         #    geez_digit = ""
         #    last_geez_digit_was_zero = True

         print("geez dig at", i, geez_digit)

         if next_to_be_added_is_hundred:
            if not last_geez_digit_was_zero:
               final_geez_numerals += (geez_digit + geez_hundred)
               next_to_be_added_is_hundred = False
            else:
               next_to_be_added_is_hundred = False
         else:
            if (i + 1) == len(arabic_number_split):
               # if this is the last index
               #   1. dont't append ten thousand
               #   2. if the split was '00', don't append anything
               if arabic_number_split[i] != "00":
                  final_geez_numerals += geez_digit
               
               
               continue

            final_geez_numerals += (geez_digit + geez_ten_thousand)

            next_to_be_added_is_hundred = True

   return final_geez_numerals

# returns either 'arabic' or 'geez'
def numerals_are_in(number_in_geez_or_arabic):
   if len(number_in_geez_or_arabic) == 0:
      return "invalid"

   first_character = number_in_geez_or_arabic[0]

   first_character_is = ""

   if first_character in arabic_numeral_characters:
      first_character_is = "arabic"
   elif first_character in geez_numeral_characters:
      first_character_is = "geez"
   else:
      return "invalid"


   for i in range(1, len(number_in_geez_or_arabic)):
      character = number_in_geez_or_arabic[i]

      if first_character_is == "arabic" and (not character in arabic_numeral_characters):
         return "invalid"
      elif first_character_is == "geez" and (not character in geez_numeral_characters):
         return "invalid"

   # if a return did not happen in the loop
   if len(number_in_geez_or_arabic) == 1 and first_character_is == "arabic" and first_character == "0":
      return "invalid"

    # if reached here without returning 
   return first_character_is

#geez_numerals_to_arabic("፼፻")
# at 00:10 not working for '999999999'
#geez_numerals_to_arabic("፼፲፩፻፲፩፼፲፩፻፲፩")  # 111111  1111111

#print(arabic_to_geez_numerals(11111110)) # expected: ፲፩፻፲፩፼፲፩፻፲  actual: ፲፩፻፲፩፼፲፩፻፲

#print(simple_geez_numerals_to_arabic("፺፱"))

def geez_arabic_converter(number_in_geez_or_arabic):
   numerals_in = numerals_are_in(number_in_geez_or_arabic)

   if numerals_in == "invalid":
      return "invalid argument"
   
   if numerals_in == "arabic":
      return arabic_to_geez_numerals(number_in_geez_or_arabic)
   elif numerals_in == "geez":
      return geez_numerals_to_arabic(number_in_geez_or_arabic)

print(geez_arabic_converter("100000000")) # expected: 100000000 actual: 100000000