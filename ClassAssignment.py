class Multiprogram():
    def Subfields():
        fields = ['Machine Learning','Neural Networks','Vision',
                  'Robotics','Speech processing','Natural Language Processing']
        return fields

print("Sub-fields in AI are:")
for field in SubfieldsInAI.Subfields():
    print(field)

    def oddeven():
        num=int(input("Enter the number:"))
        if((num%2)==0):
            print(num," is Even Number")
            message=num," is Even Number"
        else:
            print(num," is Odd Number")
            message=num," is Odd Number"
            return message

    def Eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(age<21):
            print("NOT ELIGIBLE")
            message="NOT ELIGIBLE"
        else:
            print("ELIGIBLE")
            message="ELIGIBLE"
        gender=input("Your Gender")
        age=int(input("Your Age:"))
        if(age<18):
            print("NOT ELIGIBLE")
            message="NOT ELIGIBLE"
        else:
            print("ELIGIBLE") 
            message="ELIGIBLE"
            return message

    def percentage():
        sub1 = float(input("Subject1: "))
        sub2 = float(input("Subject2: "))
        sub3 = float(input("Subject3: "))
        sub4 = float(input("Subject4: "))
        sub5 = float(input("Subject5: "))

        total = sub1 + sub2 + sub3 + sub4 + sub5
        percentage = total / 5

        return total, percentage

total_marks, percent = FindPercent.percentage()
print("Total:", total_marks)
print("Percentage:", percent)

    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        area=(height*breadth)/2
        print("Area formul=(Height*Breadth)/2")
        message="Area formul=(Height*Breadth)/2"
        print("Area of Triangle:",area)
        message="Area of Triangle:",area
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        perimeter=height1+height2+breadth  
        print("Perimeter formla=Height1+Height2+Breadth")
        message="Perimeter formla=Height1+Height2+Breadth"
        print("Perimeter of Triangle:",perimeter) 
        message="Perimeter of Triangle:",perimeter
        return message
    area=triangle()  