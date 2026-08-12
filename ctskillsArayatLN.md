Annex A
Computational Thinking Exercise: "Smart School Canteen Queue"

Section:9 Arayat Score:____________

C# / Name:_________________________________ Date: _____________


Scenario

The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

Some students take too long to decide what to order.
The cashier has to manually calculate totals and give change.
There is no system to track which food items are running out.
Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem

Main Problem: Long wait times in the canteen which lead to some students and teachers to not be able to eat.

Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. Students taking too long in deciding what to order
2. The canteen has no track of their inventory
3. The cashier has to manually calculate the change to give to the customer

Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

Sub-Problem:
Students taking too long in deciding what to order
CT Skill:
Algorithm design
Example Solution:
Students can submit their orders before lunch using an app. They will also input if whether they will pay digitally or in person, and if they pay in person the amount which they will pay with.

Sub-Problem:
The canteen has no track of their inventory
CT Skill:
Data representation, Algorithm design
Example Solution:
Using the same app students used to order their lunch, the canteen will be able to see their real time invetory with the data gathered from the orders of the students. 
The canteen will have to input the inventory beforehand. (Current Inventory = Initial Inventory - Amount ordered)

Sub-Problem:
The cashier has to manually calculate the change to give to the customer
CT Skill:
Data representation, Algorithm design
Example Solution:
Using the same app the students used to input the amount they will pay with (if they ordered in person), the cashier will be able to see the change needed before the order is picked up.
(Change = Amount payed - Price of order)

 Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem

Sub-Problem 1:
START
Student inputs order
Order gets sent to app
App calculates Order price
App asks Student if they will pay in person or digitally
IF Student will pay in person:
   Student inputs amount they will pay with
   App calculates change needed
   Return Change Needed
END IF
Return Order Price
END

Sub-Problem 2:
SETUP
Canteen Inputs their inventory
START
Retrieve Student Orders
Find Items Student Ordered
Subtract amount Student ordered with current inventory
Return Cafeteria Inventory
END

Sub-Problem 3:
START
Retrieve Change needed for Student order
Display Change needed for Student order number n
END

Rubrics For Grading
Total Points: 20pts

Criteria & Levels of Performance

Criteria

Excellent (4)

Good (3)

Fair (2)

N.I. (1)

Identification of Sub-Problems

Identifies 3+ clear, relevant sub-problems that directly connect to the scenario.

Identifies 2–3 mostly relevant sub-problems.

Identifies 1–2 vague or partially relevant sub-problems.

Struggles to identify sub-problems or lists unrelated issues.

Application of CT Strategies

Correctly applies appropriate CT strategies (abstraction, decomposition, pattern recognition, algorithm design) to each sub-problem with clear reasoning.

Applies CT strategies to most sub-problems, with minor errors or limited explanation.

Applies CT strategies inconsistently, with weak or unclear reasoning.

Rarely applies CT strategies or misuses them.

Flowchart / Pseudocode

X 2

Flowchart / Pseudocode is complete, logical, and easy to follow; shows clear steps and decision points.

Flowchart / Pseudocode is mostly complete and logical, with minor gaps or unclear steps.

Flowchart / Pseudo Code is partially complete, missing key steps or connections.

Flowchart / Pseudocode is incomplete, confusing, or missing entirely.

Reflection / Explanation

Provides thoughtful reflection on how decomposition helps problem-solving and identifies CT skills used with strong justification.

Provides adequate reflection with some justification of CT skills.

Provides limited reflection with weak or generic justification.

Provides minimal or no reflection.
