                    #================================================================
                    #============== Lesson 3: Assignments | Sets ====================
                    #================================================================

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 1. Python Sets Adventure ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Objective:
    # The aim of this assignment is to deepen your understanding and application of Python sets in various scenarios, ranging from basic operations to advanced manipulations and best practices. You will correct given codes, use sets in everyday contexts, and tackle challenges that require creative thinking and problem-solving.

# Task 1: Flight Route Comparison
    # Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

            # Destinations that both airlines fly to.
            # Destinations unique to your airline.
            # Whether there are any destinations that neither airline shares.


    # Example Code:
            # our_routes = {"LAX", "JFK", "CDG", "DXB"}
            # competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

#================================================================================================
#=====================================Begin Code=================================================
#================================================================================================

print("\n"*10,"="*125, "\n", "\n","="*125)
txt = "1. Python Sets Adventure"
x = txt.center(125)
print (x, "\n")


our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_destinations = our_routes.intersection(competitor_routes)
unique_destinations = our_routes.difference(competitor_routes)
non_shared_destinations = our_routes.symmetric_difference(competitor_routes)

print("Destinations that both airlines fly to:")
for destination in common_destinations:
    print("- " + destination)

print("\nDestinations unique to our airline:")
for destination in unique_destinations:
    print("- " + destination)

print("\nDestinations that neither airline shares:")
for destination in non_shared_destinations:
    print("- " + destination)

                                #======= END OF CODE =========




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2. Set Operations in Data Analysis ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Objective: 
    # The aim of this assignment is to enhance your skills in using Python sets for data analysis tasks. You will apply various set operations to handle real-world data scenarios, focusing on their practical application and efficiency.

# Task 1: 
    # Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. Write a Python function to remove duplicates and display the unique customer IDs.

    # Example Code:
         # customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

         # Expected Outcome: A set of unique customer IDs, ensuring no duplicates. For instance, {'C001', 'C002', 'C003', 'C004'}.

#================================================================================================
#=====================================Begin Code=================================================
#================================================================================================

print("\n","="*125, "\n")
txt2 = "2. Set Operations in Data Analysis"
x = txt2.center(125)
print ("\n"*2, x, "\n")

def remove_duplicates(customer_ids):
    unique_customer_ids = set(customer_ids)
    return unique_customer_ids

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
unique_ids = remove_duplicates(customer_ids)

print("Unique customer IDs:")
for customer_id in unique_ids:
    print("- " + customer_id)
print("\n","="*125, "\n", "\n","="*125)

                                    #======= END OF CODE =========


# Author Roger Block