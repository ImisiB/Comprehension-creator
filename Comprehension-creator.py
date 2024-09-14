print("WELCOME TO A COMPREHENSION CREATOR")
print("I AM GOING TO ASK SOME QUESTIONS AND YOU WILL HAVE TO ANSWER THEM.")
print()

def main():
    user_name = input("What is your name: ")
    user_info = input("Where do you come from? : ")
    user_favorite_color = input("What is your favorite color? : ")
    user_favorite_food = input("What is your favorite food? : ")
    user_work = input("What do you do for a living? :")
    user_works = input("Are you a web developer? ")
    
    if user_works == "yes" :
        user_worked = input("What programming language are you learning ")
        user_working = input("What level of programming are you?, are you a beginner, professional... ")
    
    print()
    
    print("THOSE ARE ALL THE QUESTIONS, LOOK AT THE COMPREHENSION BELOW;")
    if user_works == "yes":
        print("My name is",user_name,".I come from",user_info,".My favorite color is",user_favorite_color,".My favorite food is",user_favorite_food,".I do",user_work,"for a living. I am a",user_worked, "web developer. I am a",user_working,"in",user_worked)
        print()
        question = input("Is that the way you want your comprehension to be? (yes/no)? ")
        if question == "yes":
            question2 = input("Are you sure? (yes/no)")
            if question2 == "yes":
                if user_works == "yes":
                    print()
                    print("My name is",user_name,"I come from",user_info,".My favorite color is",user_favorite_color,".My favorite food is",user_favorite_food,".I do",user_work,"for a living. I am a",user_worked, "web developer. I am a",user_working,"in",user_worked)
                if user_works == "no":
                    print()
                    print("My name is",user_name,"I come from",user_info,".My favorite color is",user_favorite_color,".My favorite food is",user_favorite_food,".I do",user_work,"for a living." )
            else:           
                    user_name = input("What is your name? : ")
                    user_info = input("Where do you come from? : ")
                    user_favorite_color = input("What is your favorite color? : ")
                    user_favorite_food = input("What is your favorite food? : ")
                    user_work = input("What do you do for a living? :")
                    user_works = input("Are you a web developer? ")
                    if user_works == "yes" :
                        user_worked = input("What programming language are you learning ")
                        user_working = input("What level of programming are you?, are you a beginner, professional... ")
                        print()
                        print("My name is",user_name,"I come from",user_info,".My favorite color is",user_favorite_color,".My favorite food is",user_favorite_food,"I do",user_work,"for a living.I am a",user_worked, "web developer. I am a",user_working,"in",user_worked )
                    else:
                        print()
                        print("My name is",user_name,"I come from",user_info,".My favorite color is",user_favorite_color,".My favorite food is",user_favorite_food,"I do",user_work,"for a living." )
        else:
            user_name = input("What is your name: ")
            user_info = input("Where do you come from? : ")
            user_favorite_color = input("What is your favorite color? : ")
            user_favorite_food = input("What is your favorite food? : ")
            user_work = input("What do you do for a living? :")
            user_works = input("Are you a web developer? ")
            if user_works == "yes" :
                user_worked = input("What programming language are you learning? ")
                user_working = input("What level of programming are you?, are you a beginner, professional... ")
            if user_works == "yes":
                print()
                print("My name is",user_name,"I come from",user_info,".My favorite color is",user_favorite_color,".My favorite food is",user_favorite_food,"I do",user_work,"for a living.I am a",user_worked,"web developer. I am a",user_working," in",user_worked )
            else:
                print()
                print("My name is",user_name,"I come from",user_info,".My favorite color is",user_favorite_color,".My favorite food is",user_favorite_food,"I do",user_work,"for a living." )
    else:
        print("My name is",user_name,"I come from",user_info,".My favorite color is",user_favorite_color,".My favorite food is",user_favorite_food,".I do",user_work,"for a living.")
        print()
        question = input("Is that the way you want your comprehension to be? (yes/no)? ")
        if question == "yes":
            question2 = input("Are you sure? (yes/no)")
            if question2 == "yes":
                if user_works == "yes":
                    print()
                    print("My name is",user_name,"I come from",user_info,".My favorite color is",user_favorite_color,".My favorite food is",user_favorite_food,".I do",user_work,"for a living. I am a",user_worked, "web developer. I am a",user_working,"in",user_worked)
                if user_works == "no":
                    print()
                    print("My name is",user_name,"I come from",user_info,".My favorite color is",user_favorite_color,".My favorite food is",user_favorite_food,".I do",user_work,"for a living." )
            else:           
                    user_name = input("Enter your name: ")
                    user_info = input("Where do you come from: ")
                    user_favorite_color = input("What is your favorite color: ")
                    user_favorite_food = input("What is your favorite food: ")
                    user_work = input("What do you do for a living? :")
                    user_works = input("Are you a web developer? ")
                    if user_works == "yes" :
                        user_worked = input("What programming language are you learning ")
                        user_working = input("What level of programming are you?, are you a beginner, professional... ")
                        print()
                        print("My name is",user_name,"I come from",user_info,".My favorite color is",user_favorite_color,".My favorite food is",user_favorite_food,"I do",user_work,"for a living.I am a",user_worked, "web developer. I am a",user_working,"in",user_worked )
                    else:
                        print()
                        print("My name is",user_name,"I come from",user_info,".My favorite color is",user_favorite_color,".My favorite food is",user_favorite_food,"I do",user_work,"for a living." )
        else:
            user_name = input("Enter your name: ")
            user_info = input("Where do you come from: ")
            user_favorite_color = input("What is your favorite color: ")
            user_favorite_food = input("What is your favorite food: ")
            user_work = input("What do you do for a living? :")
            user_works = input("Are you a web developer? ")
            if user_works == "yes" :
                user_worked = input("What programming language are you learning? ")
                user_working = input("What level of programming are you?, are you a beginner, professional... ")
            if user_works == "yes":
                print()
                print("My name is",user_name,"I come from",user_info,".My favorite color is",user_favorite_color,".My favorite food is",user_favorite_food,"I do",user_work,"for a living.I am a",user_worked,"web developer. I am a",user_working," in",user_worked )
            else:
                print()
                print("My name is",user_name,"I come from",user_info,".My favorite color is",user_favorite_color,".My favorite food is",user_favorite_food,"I do",user_work,"for a living." )

main()
