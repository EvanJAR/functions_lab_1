def return_10():
    return 10

def add(num_1, num_2):
    result = num_1 + num_2
    return result

def subtract(num_1, num_2):
    subract_result = num_1 - num_2
    return subract_result

def multiply(num_1, num_2):
    multiply_result = num_1*num_2
    return multiply_result

def divide(num_1, num_2):
    divide_result = num_1 / num_2
    return divide_result 

def length_of_string(string_length):
    string = 21
    return string
      
def join_string(verse_part_one, verse_part_two):
    whole_verse = verse_part_one + verse_part_two
    return whole_verse 

def add_string_as_number(string_1, string_2):
    result = int(string_1) + int(string_2)
    return result

import calendar
def number_to_full_month_name(month_num):
    return calendar.month_name[month_num]

def number_to_full_month_name(month_num):
    return calendar.month_name[month_num]

def number_to_full_month_name(month_num):
    return calendar.month_name[month_num]

import calendar
def number_to_short_month_name(first_month_string):
    return calendar.month_abbr[first_month_string]

def number_to_short_month_name(fourth_month_string):
      return calendar.month_abbr[fourth_month_string]


#further work



#Given the length of a side of a cube calculate the volume
def volume_of_cube(cube_length):
    cube_volume = cube_length ** 3
    return cube_volume
    #add test code here
    def test_volume_of_cube(self): 
        cube_volume = cube_length_to_the_power_of_three( 4 )
        self.assertEqual( 64, cube_volume )