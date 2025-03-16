
def Scores(name,score):
    file = open('text.txt', mode="a")
    
    if 80 <= score <= 100:
        print("Excellent")
        file.write(f"{name}, with score of {score} is Excellent\n")
    
    elif 60 <= score <= 79.9:
        print("very good")
        file.write(f"{name}, with score of {score} is very good\n")
    
    elif 40 <= score <= 59.9:
        print("good")
        file.write(f"{name}, with score of {score} is good\n")
    
    elif 20 <= score <= 39.9:
        print(" fair")
        file.write(f"{name}, with score of {score} is fair\n")
    
    else:
        print("poor")
        file.write(f"{name}, with score of {score} is poor\n")
    file.close()