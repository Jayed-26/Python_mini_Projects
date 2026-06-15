# This is a cgpa calculator

print('''********CGPA LIST********
      
      F (less than 40)
      D (40 - 44)
      C (45 - 49)
      C+ (50 - 54)
      B- (55 - 59)
      B  (60 - 64)
      B+ (65 - 69)
      A- (70 - 74)
      A  (75 - 79)
      A+ (80 or more than 80)''')

def get_grade_point(marks):
      if marks >= 80:
            return 4.00
      elif marks >= 75:
            return 3.75
      elif marks >= 70:
            return 3.50
      elif marks >= 65:
            return 3.25
      elif marks >= 60:
            return 3.00
      elif marks >= 55:
            return 2.75
      elif marks >= 50:
            return 2.50
      elif marks >= 45:
            return 2.25
      elif marks >= 40:
            return 2.00
      else:
            return 0.00

m_a = int(input("Enter Mark For Chemistry :"))
m_aa = int(input("Enter Mark For Chemistry_Lab :"))
m_b = int(input("Enter Mark For DLD :"))
m_bb = int(input("Enter Mark For DLD_Lab :"))
m_c = int(input("Enter Mark For OOP :"))
m_cc = int(input("Enter Mark For OOP_Lab :"))
m_d = int(input("Enter Mark For Math_II :"))
m_e = int(input("Enter Mark For DM :"))

a = get_grade_point(m_a)
aa = get_grade_point(m_aa)
b = get_grade_point(m_b)
bb = get_grade_point(m_bb)
c = get_grade_point(m_c)
cc = get_grade_point(m_cc)
d = get_grade_point(m_d)
e = get_grade_point(m_e)


total_credits = 18.75
total_points = (a*3)+(aa*0.75)+(b*3)+(bb*1.5)+(c*3)+(cc*1.5)+(d*3)+(e*3)
cgpa = total_points / total_credits

print("\n--- YOUR RESULT ---")
print("Your CGPA is :", cgpa)

g = str(cgpa)    # cgpa is type float and engine can't read float so i converted the cgpa to str(string).

import pyttsx3
engine = pyttsx3.init()
engine.say("Your CGPA is " + g)
engine.runAndWait()

