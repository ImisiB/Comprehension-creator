print("WELCOME TO A COMPREHENSION CREATOR")
print("I AM GOING TO ASK SOME QUESTIONS AND YOU WILL HAVE TO ANSWER THEM.")
print()

def main():
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
    
    print("THOSE ARE ALL THE QUESTIONS, LOOK AT THE COMPREHENSION BELOW;")
    
    if user_works == "no".lower():
        print("My name is",user_name,"I come from",user_info,". My favorite color is",user_favorite_color,".My favorite food is ",user_favorite_food,"I do",user_work," for a living." )
    
    elif user_works == "yes":
        print("My name is",user_name,"I come from",user_info,". My favorite color is",user_favorite_color,".My favorite food is ",user_favorite_food,"I do",user_work," for a living. I am a",user_worked, "web developer. I am a",user_working," in",user_worked)
    replace = input("If you want to replace a word, type; '1', but if you don't want to replace a word, type; '0'")
    
    if replace == "1":
        string = "My name is",user_name,"I come from",user_info,". My favorite color is",user_favorite_color,".My favorite food is ",user_favorite_food,"I do",user_work," for a living."
        print(str(string))
        print()
        word_to_replace = input(str("Enter a word to replace: "))
        word_replacement = input(str("Enter the word replacement: "))
        print()
        
    if replace == "0":
        if user_works == "yes":
            print()
            storage = ("My name is",user_name,". I come from",user_info,". My favorite color is",user_favorite_color,".My favorite food is",user_favorite_food,"I do",user_work," for a living. I am a web developer, i am a",user_worked, " web developer. I am a",user_working," in",user_worked) 
            print(str(storage))
        # else:
            print("My name is",user_name,"I come from",user_info,". My favorite color is",user_favorite_color,".My favorite food is ",user_favorite_food,"I do",user_work," for a living. I am a",user_worked, "web developer. I am a",user_working," in",user_worked)
    elif word_to_replace in string: 
            word = str(string).replace(word_to_replace, word_replacement)
            print(word)
            # print("My name is",user_name,"I come from",user_info,". My favorite color is",user_favorite_color,".My favorite food is ",user_favorite_food,"I do",user_work," for a living. I am a",user_worked, "web developer. I am a",user_working," in",user_worked)
            
    elif word_to_replace not in string:
        print("       unknown word", string, "does not include", word_to_replace)
    
    # print("My name is",user_name,"I come from",user_info,". My favorite color is",user_favorite_color,".My favorite food is",user_favorite_food,"I do",user_work," for a living. I am a web developer, i am a",user_worked, " web developer. I am a",user_working," in",user_worked)

main()
