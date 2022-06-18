print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower_case = name1.lower()
name2_lower_case = name2.lower()

count_t_1 = int(name1_lower_case.count("t")) 
count_r_1 = int(name1_lower_case.count("r")) 
count_u_1 = int(name1_lower_case.count("u")) 
count_e_1 = int(name1_lower_case.count("e")) 

count_t_2 = int(name2_lower_case.count("t"))
count_r_2 = int(name2_lower_case.count("r"))
count_u_2 = int(name2_lower_case.count("u"))
count_e_2 = int(name2_lower_case.count("e"))

total_count_true = count_t_1 + count_r_1 + count_u_1 + count_e_1 + count_t_2 + count_r_2 + count_u_2 + count_e_2


count_l_1 = int(name1_lower_case.count("l")) 
count_o_1 = int(name1_lower_case.count("o")) 
count_v_1 = int(name1_lower_case.count("v")) 
count_ee_1 = int(name1_lower_case.count("e")) 

count_l_2 = int(name2_lower_case.count("l"))
count_o_2 = int(name2_lower_case.count("o"))
count_v_2 = int(name2_lower_case.count("v"))
count_ee_2 = int(name2_lower_case.count("e")) 

total_count_love = count_l_1 + count_o_1 + count_v_1 + count_ee_1 + count_l_2 + count_o_2 + count_v_2 + count_ee_2

score = str(total_count_true) + str(total_count_love)
score_int = int(score)

if score_int < 10 or score_int > 90:
 print(f"Your score is {score}, you go together like coke and mentos.")
elif score_int >= 40 and score_int <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


