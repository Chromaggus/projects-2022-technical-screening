"""
Inside conditions.json, you will see a subset of UNSW courses mapped to their 
corresponding text conditions. We have slightly modified the text conditions
to make them simpler compared to their original versions.

Your task is to complete the is_unlocked function which helps students determine 
if their course can be taken or not. 

We will run our hidden tests on your submission and look at your success rate.
We will only test for courses inside conditions.json. We will also look over the 
code by eye.

NOTE: This challenge is EXTREMELY hard and we are not expecting anyone to pass all
our tests. In fact, we are not expecting many people to even attempt this.
For complete transparency, this is worth more than the easy challenge. 
A good solution is favourable but does not guarantee a spot in Projects because
we will also consider many other criteria.
"""
import json
import string

# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()

# These courses either have only one prereq, or contain only ORs in the prerequisites. 
simple_courses = [
    'COMP1521', 'COMP1531', 'COMP2041', 'COMP2521', 'COMP3121', 'COMP3131', 'COMP3141', 'COMP3153', 
    'COMP3161', 'COMP3211', 'COMP4121', 'COMP4336', 'COMP4418', 'COMP9418', 'COMP9444', 'COMP9447'
]

# These courses only have a UOC pre-requisite
simple_uoc = [
    'COMP4161', 'COMP4951'
]

def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """

    # Get the prerequisites data for the course
    prereq = CONDITIONS[target_course]
    # Also get rid of any unnecessary punctuation
    prereq = prereq.translate(str.maketrans('', '', string.punctuation))
    
    # COMP1511
    if target_course == 'COMP1511':
        return True
    
    # Courses with only 1 course as prereq or only uses 'or'
    elif target_course in simple_courses:

        # Split up the words in the prerequisites into a list
        prereq_list = prereq.split()

        # Keep only the words that are 8 letters long. These are the actual courses
        prereq_list = list(filter(lambda s: len(s) == 8, prereq_list))
        for course in prereq_list:
            if course in courses_list:
                return True

    # COMP4952 and COMP4953
    elif len(prereq) == 4:
        if 'COMP' + prereq in courses_list:
            return True

    # Courses with simple UOC pre-requisites
    elif target_course in simple_uoc:

        # Split up the words in the prerequisites into a list
        prereq_list = prereq.split()

        # Find the number of units required by finding the number before 'units'
        for i in range(len(prereq_list)):
            if prereq_list[i] == 'units':
                num_units = int(prereq_list[i - 1])
                break
        
        # Check if there are enough courses completed
        if len(courses_list) >= num_units // 6:
            return True

    return False
