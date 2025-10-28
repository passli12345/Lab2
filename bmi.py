def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    bmi = weight / (height * height)
    print("BMI = {:.2f}".format(bmi))
    
    if bmi < 18.5:
        print("Classification: Under Weight")
    elif bmi <= 25.0:
        print("Classification: Normal Weight")
    else:
        print("Classification: Over Weight")

calculate_bmi(weight=57, height=1.73)
