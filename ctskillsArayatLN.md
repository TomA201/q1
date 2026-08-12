
Annex B
Computational Thinking Exercise: "Smart Vending Machine"

Section: 9 - Arayat         Score:____________

C# / Name: Angeles, Apostol, Aquino  (C.N 1,2,3) Date: _____________ 


Scenario
Your school installs a vending machine to provide snacks and drinks. However, students encounter several issues:

Sometimes the machine does not give the correct change.
Items run out, but the machine doesn’t notify anyone.
Students press the wrong buttons and get the wrong item.
The machine is slow when multiple students use it in succession.
Your task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem
Main Problem: The Vending Machine is ineffective, unreliable, and inconvenient

Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. Machine gives the incorrect amount of change.
2. Machine doesn't notify owner when a stock of a specific item is depleted.
3. Students press the wrong buttons and end up getting the wrong item.
4. Machine becomes slower when multiple students use it in succession.


Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

Sub-Problem:
Machine gives the incorrect amount of change.
CT Skill:
Algorithm Design
Example Solution:
First, the user inputs the amount they will pay with, next they will input the item they would like to buy and the quantity to be purchased.
The machine will then ask if the user will buy another item. If they do, the user will input another item and the quantity to be purchased.
If the user says no, the machine will then calculate the change needed and give it to the user.

Sub-Problem:
Machine doesn't notify owner when a stock of a specific item is depleted.
CT Skill:
Data Representation, Algorithm Design
Example Solution:
When the machine drops an item, it will subtract 1 from the stock of the item dropped before the purchase was made. 
After this, the machine will check if the stock of the item dropped is zero. If not, nothing will happen.
If the stock is zero, the machine will label the item as sold out and notify the owner or manager of the machine.

Sub-Problem:
Students press the wrong buttons and end up getting the wrong item.
CT Skill:
Algorithm Design
Example Solution:
If a student were to order an item, the machine would ask if they are sure that they would buy it.
If the student says yes, the machine will drop it. If no, the student will pick their desired item.

Sub-Problem:
Machine becomes slower when multiple students use it in succession.
CT Skill:
Algorithm Design
Example Solution:
After a user has received their order from the machine, the machine will then start a 10 second countdown before it takes another order.

Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem (Your group could use a separate sheet of paper)
Flowchart for Sub-Problem 1:
<img width="285" height="596" alt="Actual sub-problem 1 flowchart" src="https://github.com/user-attachments/assets/ac282959-307f-47cf-b7a3-ee43834eeb06" />


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


