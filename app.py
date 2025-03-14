name = input('what is your name?')
score = float(input('what is your score?'))

if 80 <= score <= 100:
    print("Excellent")
elif 60 <= score <= 79.9:
    print("very good")
elif 40 <= score <= 59.9:
    print("good")
elif 20 <= score <= 39.9:
    print(" fair")
else:
    print("poor")
