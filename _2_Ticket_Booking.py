class movie_ticket:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.user_info = {}

    def show_the_seats(self):
            print("\n**  SHOW THE SEATS  **")
            for i in range(self.rows+1):
                for j in range(self.columns+1):
                    if i==0:                                # i = row
                        if j==0:                            # j = column
                            print(" ",end = " ")
                        else:
                            print(j,end = " ")
                    elif j == 0:
                        print(i, end = " ")
                    else:
                        if self.is_seat_booked(i,j):
                            print("B",end = " ")
                        else:
                            print("S",end = " ")
                print()

                
    def buy_ticket(self):
        print("\n**  BUY THE TICKET  **")
        try:
            row = int(input("Please select your row : "))
            column = int(input("Please select your seat : "))

            total_seats = self.rows * self.columns
            if total_seats <=60:
                ticket_price = 10
            else:
                if row < self.rows//2:
                    ticket_price = 10
                else:
                    ticket_price = 8

            print(f"\nYour row number is : {row} \nSeat number is : {column} \nAmount for the ticket is ${ticket_price}")
            option = int(input(("\nTo book the ticket enter 1 or to exit enter 2 \nyour choice is :  ")))
            if option == 1:
                name = input("please enter your name : ")
                age = int(input("please enter your age : "))
                gender = input("please enter your gender : ")
                mobile_no = int(input("please enter your mobile number : "))
                seat_no = str(row) + str(column)
                self.user_info[seat_no] = [name, age, gender, mobile_no, ticket_price]
                print("Ticket booked successfully")
            else:
                print("**  No Problem! Thank You for connecting with us  **")
        except Exception as ex:
            print("Invalid option, Try again", ex)


    def statistics(self):
        print("\n**  STATISTICS  **")
        total_seats = self.rows * self.columns
        no_of_purchased_tickets = len(self.user_info)
        percentage_of_tickets_booked = no_of_purchased_tickets / total_seats * 100
        price_list = []
        for k,v in self.user_info.items():
            price_list.append(v[4])
        current_income = sum(price_list)
        if total_seats <= 60:
            total_income = total_seats * 10
        else:
            front_seat_price = 10
            back_seat_price = 8
            front_seats = (self.rows//2)*self.columns
            total_income = (front_seat_price * front_seats) + ((total_seats - front_seats) * back_seat_price)

        print(f"\n1.NUMBER OF PURCHASED TICKETS : {no_of_purchased_tickets} \n2.PERCENTAGE OF TICKETS BOOKED : {percentage_of_tickets_booked} \n3.CURRENT INCOME : {current_income} \n4.TOTAL INCOME : {total_income}")



    def user_Details(self):
        print("**  SEAT USER DETAILS  **")
        try:
            row = int(input("Please enter row number : "))
            column = int(input("Please enter seat number : "))
        except Exception as ex:
            print("Invalid option, Please try again", ex)
        seat_no = str(row) + str(column)
        user_data = self.user_info.get(seat_no,None)
        if user_data:
            print(f"\nSeat number : {seat_no} \nName : {user_data[0]} \nGender : {user_data[2]} \nAge : {user_data[1]} \nTicket_price : {user_data[4]} \nPhone no : {user_data[3]}")
        else:
            print(f"**  seat is empty for the row no. {row} and seat no. {column} **")        



    def is_seat_booked(self,row,column):
        seat_no = str(row) + str(column)
        if seat_no in self.user_info.keys():
            return True
        return False

        






