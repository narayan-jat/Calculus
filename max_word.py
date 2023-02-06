'''
This module contains functions querySearch and main

Author Name: Narayan Jat 
Date:15 January,2023
'''

# Given two strings, and a query word, count which string contains the word more number of times. 
# Print “first” or “second” or “equal” as the answer.

# Defining a function 
def main(string1,string2, queryWord):
	'''
	Returns:'first' or 'second' or 'equal' phrases.

	If the queryWord appeared more number of times in string1 then first and if in string2 then second and equal if 
	appeared same number of times in both.

	Doc-test:
	>>> main('The name of this book is ramayan.','This is what?', 'book')
	'first'
	>>> main('The name of this book is ramayan.','This is so helpful to maintain relationship.', 'ram')
	'equal'
	>>> main('The name of this book is ramayan.', ' I am able maintain relatioship.', 'I')
	'second'
	>>> main('Her name is rekha, I met rekha', 'I met rekha because today is birthday of rekha and rekha is happy', 'rekha')
	'second'
	'''
	if querySearch(string1,queryWord) > querySearch(string2, queryWord) :
		return 'first'
	elif querySearch(string1,queryWord) < querySearch(string2, queryWord) :
		return 'second'
	else:
		return 'equal'

# defining a helper function
def querySearch(string1, queryWord):
	'''
	Returns: The counting of queryWord in string1.

	Imputed strings are assumed to general strings with following properties.
	String ends with punctuation (.) e.g., ‘ram eats apple daily.’
	String with use of comma(,) e.g., ‘ ram, lakhan, and sita went into exile.’
	String with exclamatory special character (!) e.g., ‘very good! You did well.’
	String with words in quotation(“” or ‘’) e.g.,  ‘My favorite book is ‘The art of happiness’.’
	String with braces((),{},[]) e.g., ‘ The natural numbers are integers(positive).’
	String having question mark (?) e.g., ‘ Where does it come from?’
	Any other special characters in the string are considered as part of the word of string.

	parameters string1: The inputed string to be searched for word.
	precondition: It must be a string type.

	parameters queryWord: It is which is to be searched in string1.
	precondition: It must be string type.

	Doctests:
	>>> querySearch('Do you know name(id) of this book? Yes, name of this "Holy" book is "ramayan".', 'book')
	2
	>>> querySearch('Do you know name(id) of this book? Yes, name of this "Holy" book is "ramayan".', 'Holy')
	1
	>>> querySearch('Do you know name(id) of this book? Yes, name of this "Holy" book is "ramayan".', 'ramayan')
	1
	>>> querySearch('Do you know name(id) of this book? Yes, name of this "Holy" book is "ramayan".', 'Yes')
	1
	>>> querySearch('Do you know name(id) of this book? Yes, name of this "Holy" book is "ramayan".', 'id')
	1
	>>> querySearch('Do you know name(id) of this book? Yes, name of this "Holy" book is "ramayan".', 'book?')
	1
	>>> querySearch('Do you know name(id) of this book? Yes, name of this "Holy" book is "ramayan".', 'ram')
	0
	'''
	# creating lisr of all words in string by using split.
	lst = string1.split()
	count = 0
	for x in lst :
		p = len(x)
		if x == queryWord :
			count = count + 1
		elif (x.find(',') != -1 or x.find('.') != -1 or x.find('!') != -1) and (x.find("'") != -1 or x.find('"') != -1):  # if element in list is in format ("ram".) then extracting (ram)
			if x[1 : p - 2] == queryWord :
				count = count + 1
		elif x.find(',') != -1 or x.find('.') != -1 or x.find('!') != -1 or x.find('?') != -1:  # if element in list has these delimiter then  they are separated.
			if x[ : p - 1] == queryWord :
				count = count + 1
		elif x[1 : p - 1] == queryWord :   # if element is type of ('ram') then extracting ram  
			count = count + 1
		elif x[x.find('(') + 1 : x.find(')')] == queryWord :   # if element of list is of type 'integer(positive)' then extracting positive from '(positive)' 
			count = count + 1
	return count
		
# Main program
string2 = input("Enter your string: ")
string1 = input("enter your string: ")
queryWord = input("Enter your word to be searched: ")
print(main(string1, string2, queryWord))

# This is to test function.
# if __name__ == '__main__':
# 	import doctest as t 
# 	t.testmod()
