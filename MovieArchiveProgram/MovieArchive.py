"""
This is a program that uses some functions to process user inputs for storing, listing, and searching for movies
in a list of dictionaries. The movies are user-defined and are not stored once the program exits.

As of September 22, 2020, I am still working on this one.
"""



while True == True:
    StartProgram = input("Do you want to run this program? Enter yes or no: ")
    StartProgramLower = StartProgram.lower()
    if StartProgramLower == "no":
        print("Program will now exit.")
        quit()
    elif StartProgramLower != "yes":
        print("please type a valid option")
        continue
    else:
        while True == True:
            MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
            if MENU_PROMPT == "q":
                quit()
            else:
                movies = []

                title = input("Enter the movie title: ")
                director = input("Enter the movie director: ")
                year = input("Enter the movie release year: ")

                movies.append({'title': title, 'director': director, 'year': year})

                print(movies)
            continue