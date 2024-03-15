import sqlite3

def buyTickets():
    con = sqlite3.connect("trondelagTeater.db")
    cursor = con.cursor()

	con.execute("SELECT NAME")
    shows = ["Forestilling 1", "Forestilling 2", "Forestilling 3"]
    print("Forestillinger")
    for i in range(len(shows)):
        print(f"{i}: {shows[i]}")

    show = input("Hvilken forestilling vil du på? ")

    ticketTypes = ["Ordinær", "Honnør", "Student"]
    tickets = [0] * len(ticketTypes)

    while True:
        print("Type billetter:")
        for i in range(len(ticketTypes)):
            print(f"{i+1}: {ticketTypes[i]}")
        ticketType = int(input("Hvilken type billett vil du kjøpe? ")) - 1

        ticketCount = int(input(f"Hvor mange billetter vil du kjøpe av type {ticketTypes[ticketType]}?: "))
        tickets[ticketType] += ticketCount

        if input("Vil du kjøpe flere billetter (j/n)? ") != 'j':
            break

    for ticket in tickets:
        cursor.execute("INSERT INTO Billett VALUES (?)", ticket)


buyTickets()
