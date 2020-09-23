"""
This is a program that uses some functions to process user inputs for storing, listing, and searching for movies
in a list of dictionaries. The movies are user-defined and are not stored once the program exits.

As of September 23, 2020, I am still working on this one.
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
        movies = []
        def AddMovie():
            title = input("Enter the movie title: ")
            director = input("Enter the movie director: ")
            year = input("Enter the movie release year: ")
            movies.append({'title': title, 'director': director, 'year': year})
            print(f"You've added: ")
            print(f"""movie "{title}",""")
            print(f"""director "{director}",""")
            print(f"""released "{year}".""")
            print(movies)
        while True == True:
            MENU_PROMPT = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: ")
            if MENU_PROMPT == "q":
                print("Program will now exit.")
                quit()
            elif MENU_PROMPT == "a":
                AddMovie()
            elif MENU_PROMPT == "l":
                pass
            elif MENU_PROMPT == "f":
                pass
            else:
                print("Please choose a valid option.")
                continue