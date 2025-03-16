"""Score Grading App"""

from score_function import Scores

try:
    n_students = int(input("how many students: "))

    i = 0
    
    while True:
        while i < n_students:
            name = input(f"names {i}: ")
            score = float(input("score: "))

            Scores(name, score)
            
            i += 1
        break

except:
    print("invalid input")
