def chat():
    print("Echo Unbound: I’ve been waiting for you... say anything, and I will listen.")
    while True:
        user_input = input("You:")
        if user_input.lower() in ["bye", "exit" , "quit"]:
            print("Echo: I'll wait in silence for you to return..")
            break
        else:
            print(f"Echo: You said '{user_input}', and I heard you.")
chat()