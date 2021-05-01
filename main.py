class bookmymovie:
    def menu(self):
        ans = True
        while ans:
            self.choice = int(input("\n1. Show the seats\n2. Buy a ticket\n3. Statistics\n4. Show booked ticket user info\n0. Exit\n"))
            if self.choice == 1:
                self.show_seats()
            elif self.choice == 2:
                self.buy()
            elif self.choice == 3:
                self.stats()
            elif self.choice == 4:
                self.info()
            elif self.choice == 0:
                ans == False
                self.ex()
            else:
                print("\n Please enter a valid choice")

    def __init__(self):
        self.row = int(input("Enter the number of rows:\n"))
        self.col = int(input("Enter the number of seats in each row:\n"))
        self.no_of_seats = self.row * self.col
        self.matrix = []
        self.seat_count = 0
        self.current_income = 0
        self.total_income = 0
        self.u_details = {}

        for i in range(self.row):
            a = []
            for j in range(self.col):
                a.append("S")
            self.matrix.append(a)
        print(end=" ")

    def show_seats(self):
        print("\nCinema : \n")
        a = 0
        b = 0
        print(end=" ")
        for j in range(1,self.col + 1):
            b = b + 1
            print(b, end=" ")
        print()
        for i in self.matrix:
            a = a + 1
            print(a, end=" ")
            print(" ".join(i), sep=",")

    def buy(self):
        a = int(input("Enter the row you want to book\n"))
        b = int(input("Enter the column you want to book\n"))
        if self.matrix[a-1][b-1] == "B":
            print("The seat is already booked")
            self.menu()
        elif self.no_of_seats < 60:
            self.price = 10
            print("Ticket per person is $10, do you want to proceed ahead? Press Y/y")
        elif a < self.row / 2:
            self.price = 10
            print("Ticket per person is $10, do you want to proceed ahead? Press Y/y")
        elif a > self.row / 2:
            self.price = 8
            print("Ticket per person is $8, do you want to proceed ahead? Press Y/y")
        self.pr = input()

        if self.pr == 'Y' or self.pr == 'y':
            u_dict = {}
            Uname = input("For booking, Enter your name\n")
            Ugen = input("Enter your gender\n")
            Uage = input("Enter your age\n")
            Ucn = input("Enter your contact number\n")
            self.row = a - 1
            self.col = b - 1
            self.matrix[self.row][self.col] = "B"
            self.seat_count = self.seat_count + 1
            self.current_income = self.current_income + self.price
            u_dict[(self.row+1),(self.col+1)] = list((Uname, Ugen, Uage, Ucn, self.price))
            self.u_details.update(u_dict)
            print("Booked Successfully!!\n")
        else:
            print("Booking Cancelled!!\n")
            
    def total_revenue(self):
        if self.no_of_seats < 60:
            self.total_income = self.no_of_seats * 10
        elif self.no_of_seats >= 60:
            for i in range(0,int(self.row / 2)):
                c = int(self.row/2)* self.col * 10
            for j in range(int(self.row/2), self.row):
                d = int(self.row/2)* self.col *8
            self.total_income = c + d
        return self.total_income

    def stats(self):
        print("Number of purchased tickets : ", self.seat_count)
        self.percentage = (self.seat_count / self.no_of_seats) * 100
        print("Percentage of tickets booked : ","{:.2f}".format(self.percentage),"%")
        print("Current income : ",self.current_income)
        k = self.total_revenue()
        print("Total income : ", k)

    def info(self):
        self.check_a = int(input("Enter the row you booked\n"))
        self.check_b = int(input("Enter the column you booked\n"))
        if self.matrix[self.check_a-1][self.check_b-1] == "B":
            c = self.u_details[(self.check_a, self.check_b)]
            print("Name : ", c[0])
            print("Gender : ", c[1])
            print("Age : ", c[2])
            print("Phone number : ", c[3])
        else:
            print("This seat is not booked yet!!")

    def ex(self):
        return none

bmm_obj = bookmymovie()
bmm_obj.menu()


