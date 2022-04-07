global seats

Number_of_Seats_Per_Screen = 15
row = 3
column = 5

# 10 Most Popular Movies Right Now based on google
movie_list = ["The Lost City", "The Batman", "Deep Water", "The Power of the Dog", "Turning Red", "The Adam Project", "Nightmare Alley", "CODA", "Jujutsu Kaisen 0: The Movie", "Spider-Man: No Way Home"]

# Available session times
session_times = ["Morning","Afternoon","Evening"]
# Numbering All the Seats

for Number_of_Movie in range(len(movie_list)):
    for time in range(len(session_times)):
        for Seat_Number in range(Number_of_Seats_Per_Screen):
            seats = [[[Seat_Number+1 for Seat_Number in range(Number_of_Seats_Per_Screen)]for Time in range(len(session_times))] for Number_of_Movie in range(len(movie_list))]

#Main function

def Booking():

    #Gets the user phone number and validates
    def get_User_Phone_Number():

        try:
            number = int(input("Enter your phone number here: "))
            digits = [int(digit) for digit in str(number)]
            
            #Checks if it is an Mongolian number(8 digit)
            if(len(digits) == 8):
                return number
            
            else:
                x = input("That is not an 8 digit number(Mongolian number). Do you still want to proceed with the number you've entered? (y/n) ")
                
                if(x.lower() == 'y' or x.lower() == 'yes'):
                    return number
                
                else:
                    return get_User_Phone_Number()

        except ValueError:
        
            print("Invalid Input, try again!")
            return get_User_Phone_Number()

    #Selects movies from the menu and validates the input

    def Movie_Selection():

        movie_index = input("Please enter the number beside the movie you want to select: ")

        try:
            if(type(int(movie_index))==int and int(movie_index) <= len(movie_list)):    
                return int(movie_index)
             
        except ValueError:
            print("Select a valid option please!")
            return Movie_Selection()

        print(f"Choose number between 1 and {len(movie_list)}, try again!")
        return Movie_Selection()

    #Selecting the Time of the Movie and validates the input

    def Time_Selection():
        
        for i in range(len(session_times)):
            print(f"{i+1}. {session_times[i]}")

        chosen_time = int(input("Enter the number beside the time you want to select from: "))
        if(not chosen_time in range(1,len(session_times) + 1)):
            print("Invalid Input. Try again.")
            return Time_Selection()
        
        return chosen_time - 1

    #Shows the available seats for the movie and validates the input
    def Show_Available_Seats():
        i = 0
        for i in range(Number_of_Seats_Per_Screen):
            print("[" + str(seats[movie_index-1][time_chosen][i]) + "]", end=" ")
            #New Line Every 5 seats
            if((i+1) % 5 == 0):
                print(end="\n")

#Selecting Movie Seats

    def Seat_Selection():

        Selected_Seat = input("Enter a seat number to select.(Taken seats are marked as X) -> ")

        try:
            if(type(int(Selected_Seat)) == int):
                if int(Selected_Seat) >= 1 and int(Selected_Seat) <= 15 and seats[movie_index-1][time_chosen][int(Selected_Seat)-1] != "X":
                    try:
                        if seats[movie_index-1][time_chosen][int(Selected_Seat)-1] == "X":
                            print("The seat is already taken, choose a different seat.")
                            return Seat_Selection()
                    except IndexError:
                        print("Invalid number, Try again!")
                        return Seat_Selection()
                    return int(Selected_Seat)
                else:
                    print("Invalid number, Try again!")
                    return Seat_Selection()

        except ValueError:
            print("Invalid input, try again!")
            return Seat_Selection()

    #Confirming the booking information

    def Confirmation():

        print(f"Name: {name}")
        print(f"Phone Number: {phone_number}")
        print(f"Movie: {movie_list[movie_index-1]}")
        print(f"Time: {session_times[time_chosen]}")
        print(f"Seat: {selected_seat}")


        confirm = input("Do you want to confirm your booking? (Yes/No) >> ")
        confirm = confirm.lower()

        if (confirm == 'y' or confirm == 'yes'):
                print("Thanks for choosing Iveel's Movie World! <3")
                seats[movie_index-1][time_chosen][selected_seat-1] = "X"
                return True

        if (confirm == 'n' or confirm == 'no'):
            return False

        print("Invalid answer, confirm again!")

        Show_Available_Seats()

        return Confirmation()
            
    
    #main program
    #runs all the functions
    print("Welcome!")

    name = input("Enter your name here: ")

    phone_number = get_User_Phone_Number()

    # Shows the User the list of movies.

    print("Here are the list of movies:")
    for i in range(len(movie_list)):
        print(f"{i+1}. {movie_list[i]}")

    movie_index = Movie_Selection()

    time_chosen = Time_Selection()
    

    Show_Available_Seats()
    selected_seat = Seat_Selection()
    Confirmation()

    x = input("Would you like to book another ticket? (y/n) ").lower()

    
    while (x != "y" and x != "yes" and x != "n" and x != "no"):
        print("Invalid Input.")
        x = input("Would you like to book another ticket? (y/n) ").lower()
    
    match x:
        case "y":
            return Booking()
        case "yes":
            return Booking()
        case "n":
            print("Finished Booking.")
        case "no":
            print("Finished Booking.")


Booking()

    