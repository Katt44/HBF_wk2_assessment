"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Object orientation can provide abstraction,encapsulation and polymorphism.
Abstraction is used to hide specific details we dont need to know but just be able to use.
Encapsulation allows us to group things together and use them more efficiently.
Polymorphism allows for interchangeability and flexiblity  because it means we could use a method in multiple instances.


 Encapsulation, polymorphism.

2. What is a class?
	a class is a way of grouping instructions that makes allowing for variance easier and provides a flexiable structure.

3. What is an instance attribute?
 An instance attribute refers to a particular occurance of an object that later could be diferent or have a diffent instance.
The way I think about is in a class of people joe is one person with the same basic anatomy but there could slight variances for him like he might have a beard but another person wouldnt.
4. What is a method?
 A method is like a function but made especially for classes where usually the first arguement they take is self.
5. What is an instance in object orientation?
	It is a particular version  with a series of characteristics that can change or remain the same based upon the version.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   I imagine class attributes like defaults, everyone has 2 arms 2 legs but it can be over written with an instance attribute.



"""


# Parts 2 through 5:
# Create your classes and class methods


class Exam(object):
	""" """

	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.questions = []

	def add_question(self,question):
		 self.questions.append(question)


class Question(Exam):

	def ask_and_evaluate(self):
		raw_input(question)