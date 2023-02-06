from _2_Ticket_Booking import movie_ticket


class main:

    def execute(self, choice):

        if choice == 1:
            movie_ticket_obj.show_the_seats()

        if choice == 2:
            movie_ticket_obj.buy_ticket()

        if choice == 3:
            movie_ticket_obj.statistics()

        if choice == 4:
            movie_ticket_obj.user_Details()

        if choice == 0:
            quit()


if __name__ == '__main__':
    rows = int(input("Enter the number of rows : "))
    columns = int(input("Enter the number of seats in each row : "))

    movie_ticket_obj = movie_ticket(rows,columns)
    obj = main()

    while True:
        try:
            choice = int(input("\n1. Show the seats \n2. Buy a ticket \n3. Statistics \n4. Show booked tickets user info \n0. Exit \nYour choice is : "))
   
            obj.execute(choice)
        except Exception as ex:
            print("Invalid Option, Try Again", ex)
