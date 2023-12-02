import random
import datetime
from abc import ABC, abstractmethod


class Seatable(ABC):
    @abstractmethod
    def seated():
        pass


class Il_Kino:  # System Aplikasi Cinema
    def __init__(self, gifts):
        self.gift = gifts
        self.tickets = []
        studio = self.setup(self.gift)
        self.studio = studio

    def setup(self, gifts):  # inisialisasi sistem dan menentukan seat nama yang ada hadiahnya
        num_special_seats = 5
        special_seats_left = []
        special_seats_right = []
        i = 0
        while i < num_special_seats:
            idx_special_seat = random.randrange(1, 36, 2)
            if idx_special_seat not in special_seats_left:
                special_seats_left.append(idx_special_seat)
                i += 1
                
        i = 0
        while i < num_special_seats:
            idx_special_seat = random.randrange(2, 38, 2)
            if idx_special_seat not in special_seats_right:
                special_seats_right.append(idx_special_seat)
                i += 1

        left_row = {i: SpecialSeat(i, gifts[i % 5]) if i in special_seats_left else Seat(
            i) for i in range(1, 36, 2)}
        right_row = {i: SpecialSeat(i, gifts[i % 5]) if i in special_seats_right else Seat(
            i) for i in range(2, 38, 2)}
        
        vip_row = {
            'VIP1': VIP_Seat('VIP1'),
            'VIP2': VIP_Seat('VIP2')
        }

        return Studio(left_row, right_row, vip_row)

    def show_seat(self, seat_num, seat_position: str):
        if seat_position == 'left':
            if isinstance(self.studio.get_left_row()[seat_num], SpecialSeat) and self.studio.get_left_row()[seat_num].is_seated():
                return 'G '
            if not self.studio.get_left_row()[seat_num].is_seated():
                return f'{seat_num} ' if seat_num < 10 else f'{seat_num}'
            else:
                return 'X '
        if seat_position == 'right':
            if isinstance(self.studio.get_right_row()[seat_num], SpecialSeat) and self.studio.get_right_row()[seat_num].is_seated():
                return 'G '
            if not self.studio.get_right_row()[seat_num].is_seated():
                return f'{seat_num} ' if seat_num < 10 else f'{seat_num}'
            else:
                return 'X '
        if seat_position == 'VIP':
            if not self.studio.vip_row[seat_num].is_seated():
                return f'{seat_num}'
            else:
                return ' X  '

    def run(self):
        while True:
            print('|----------------------------------|')
            print('|                                  |')
            print('|              IL KINO             |')
            print('|          Nansenstrasse 22,       |')
            print('|            12047 Berlin          |')
            print('|                                  |')
            print('|----------------------------------|')
            print('')
            print('|----------------------------------|')
            print('|              SCREEN              |')
            print('|----------------------------------|')
            print('')
            print('____________________________________')
            print('|                                  |')
            print(f'| {self.show_seat(1, "left")} | {self.show_seat(3, "left")} | {self.show_seat(5, "left")} |    | {self.show_seat(2, "right")} | {self.show_seat(4, "right")} | {self.show_seat(6, "right")} |')
            print('|----------------------------------|')
            print(f'| {self.show_seat(7, "left")} | {self.show_seat(9, "left")} | {self.show_seat(11, "left")} |    | {self.show_seat(8, "right")} | {self.show_seat(10, "right")} | {self.show_seat(12, "right")} |')
            print('|----------------------------------|')
            print(f'| {self.show_seat(13, "left")} | {self.show_seat(15, "left")} | {self.show_seat(17, "left")} |    | {self.show_seat(14, "right")} | {self.show_seat(16, "right")} | {self.show_seat(18, "right")} |')
            print('|----------------------------------|')
            print(f'| {self.show_seat(19, "left")} | {self.show_seat(21, "left")} | {self.show_seat(23, "left")} |    | {self.show_seat(20, "right")} | {self.show_seat(22, "right")} | {self.show_seat(24, "right")} |')
            print('|----------------------------------|')
            print(f'| {self.show_seat(25, "left")} | {self.show_seat(27, "left")} | {self.show_seat(29, "left")} |    | {self.show_seat(26, "right")} | {self.show_seat(28, "right")} | {self.show_seat(30, "right")} |')
            print('|----------------------------------|')
            print(f'| {self.show_seat(31, "left")} | {self.show_seat(33, "left")} | {self.show_seat(35, "left")} |    | {self.show_seat(32, "right")} | {self.show_seat(34, "right")} | {self.show_seat(36, "right")} |')
            print('|----------------------------------|')
            print(
                f'|     {self.show_seat("VIP1", "VIP")}                {self.show_seat("VIP2", "VIP")}     |')
            print('|----------------------------------|')
            print('')
            print('1. Seat Booking')
            print('2. Find by Name')
            print('3. Report')
            print('4. Exit')
            choice = int(input('Enter your choice 1-4?:'))
            if choice == 1:  # Kalau Ingin Booking Seat
                # counter_book = berapa tiket yang mau dipesan
                vip_choice = input(
                    'Are you looking to book a VIP Box Seat Y/N? ')
                if vip_choice == 'Y' or vip_choice == 'y':
                    while True:
                        availablity = True
                        name = input('Enter your name : ')
                        vipseat = input('Enter your desired VIP Seat (VIP1/VIP2) : ')
                        if vipseat == str(1) or vipseat == str(2):
                            vipseat = 'VIP' + vipseat
                        if vipseat not in self.studio.get_vip_row():
                            print('Invalid VIP Seat')
                        elif not self.studio.get_vip_row()[vipseat].is_seated():
                            self.studio.get_vip_row()[vipseat].seated()
                            vip_ticket = VIPTicket(name, [vipseat], datetime.datetime.now)
                            self.tickets.append(vip_ticket)
                            self.print_ticket(vip_ticket)
                            break
                        else:
                            print('Sorry that seat is taken.')
                            confirmation = input("Exit ? (Y/N) :")
                            if confirmation == 'Y' or confirmation == 'y':
                                return False

                elif vip_choice == 'N' or vip_choice == 'n':
                    while True:
                        name = input('Enter your name : ')
                        seats = str(input('Enter your seat(s) number : '))
                        seats = list(map(int, seats.split(',')))
                        availablity = True
                        for seat in seats:
                            if seat > 36:
                                availablity = False
                            elif seat % 2 == 0 and self.studio.right_row[seat].is_seated() == True:
                                availablity = False
                            elif seat % 2 == 1 and self.studio.left_row[seat].is_seated() == True:
                                availablity = False
                        print(availablity)
                        if availablity == True:
                            special = False
                            for i in range(len(seats)):
                                seat = seats[i]
                                if seat % 2 == 0:
                                    if isinstance(self.studio.right_row[seat], SpecialSeat):
                                        special = True
                                    self.studio.get_right_row()[seat].seated()
                                    print(
                                        f'{name} booked a seat for number {seat}')

                                else:
                                    if isinstance(self.studio.left_row[seat], SpecialSeat):
                                        special = True
                                    self.studio.get_left_row()[seat].seated()
                                    # print(self.studio.left_row[seat].status)
                                    print(
                                        f'{name} booked a seat for number {seat}')
                            if special == True:
                                ticket = SpecialTicket(
                                    name, seats, datetime.datetime.now())
                            else:
                                ticket = Ticket(
                                    name, seats, datetime.datetime.now())
                            self.tickets.append(ticket)
                            self.print_ticket(ticket)
                            confirmation = input("Exit ? (Y/N) :")
                            if confirmation == 'Y' or confirmation == 'y':
                                return True
                            break
                        else:
                            print('Your selection seat is not available !')
                            print('')
                            return False
                else:
                    return False
            elif choice == 2:
                temp = None
                name = input("Enter your name : ")
                for ticket in self.tickets:
                    if ticket.get_owner_name() == name:
                        seats = ticket.get_seat_number()
                        print(f"Your seats are : {seats}")
                        temp = seats
                confirmation = input("Exit ? (Y/N) :")
                if confirmation == 'Y' or confirmation == 'y':
                    return temp
            
            elif choice == 3:
                distributed_gifts = dict()
                hourly_dict = dict()
                for ticket in self.tickets:
                    hour = ticket.get_time().strftime('%H:')[:-1]
                    if isinstance(ticket, SpecialTicket):
                        for i in ticket.get_seat_number():
                            if i % 2 == 0:
                                if isinstance(self.studio.get_right_row()[i], SpecialSeat):
                                    distributed_gifts[i] = self.studio.get_right_row()[i].get_gift()
                            else:
                                if isinstance(self.studio.get_left_row()[i], SpecialSeat):
                                    distributed_gifts[i] = self.studio.get_left_row()[i].get_gift() 

                        # if hour in hourly_dict:
                        # else:
                        #     idx = ticket.get_seat_num()
                        #     if idx % 2 == 0:
                        #         distributed_gifts[hour] = [self.studio.right[idx].get_gift()]
                        #     else:
                        #         distributed_gifts[hour] = [self.studio.left[idx].get_gift()]                
                    if hour in hourly_dict:
                        hourly_dict[hour] += len(ticket.get_seat_number())
                        print(hourly_dict[hour])
                    else:
                        hourly_dict[hour] = len(ticket.get_seat_number())
                print(f'|----------------------------------|')
                print(f'| Hour    |    Number of Booking   |')
                print(f'|----------------------------------|')
                for hour in hourly_dict:
                    print(f'| {hour}     :       {hourly_dict[hour]}                |')
                    print(f'|----------------------------------|')
                print('All distributed SeatNumber-Gift:')
                for i in distributed_gifts:
                    print(f"{i} - {distributed_gifts[i]}")
            
                print(hourly_dict, distributed_gifts, 'asdasdsa',len(distributed_gifts))

                confirmation = input("Exit ? (Y/N) :")
                if confirmation == 'Y' or confirmation == 'y':
                    print(distributed_gifts, len(distributed_gifts), 'kontol')
                    return hourly_dict, distributed_gifts
                
            elif choice == 4:
                return 'Exited'

    def find_by_name(self, name):  # untuk menemukan seat booking berdasarkan nama orang
        for ticket in self.tickets:
            if ticket.get_owner_name() == name:
                seats = ticket.get_seat_number()
                print(f"Your seats are : {seats}")
                return seats
        return None


    def print_ticket(self, ticket):
        customer_name, ticket_num, time = ticket.printed()
        print(ticket_num)
        seat_num = str(ticket_num)[1:-1]
        temp = ''
        for i in ticket_num:
            temp += str(i)
            temp += '_'
        ticket_num = temp[:-1]
        if isinstance(ticket, SpecialTicket):
            with open(f'ticket_{customer_name}_{ticket_num}.txt', 'w') as f:
                f.write(f'_____________________________________________________\n')
                f.write(f'\n')
                f.write(f'                   Il Kino Receipt                   \n')
                f.write(f'_____________________________________________________\n')
                f.write(
                    f'Name          : {customer_name}                      \n')
                f.write(
                    f'Seat          : {seat_num}                         \n')
                f.write(f'\n')
                f.write(f'    Please check below your seat to get your gift!   \n')
                f.write(f'  Please arrive 15 minutes early prior to the movie! \n')
        else:
            with open(f'ticket_{customer_name}_{ticket_num}.txt', 'w') as f:
                f.write(f'_____________________________________________________\n')
                f.write(f'\n')
                f.write(f'                   Il Kino Receipt                   \n')
                f.write(f'_____________________________________________________\n')
                f.write(
                    f'Name          : {customer_name}                      \n')
                f.write(
                    f'Seat          : {seat_num}                         \n')
                f.write(f'\n')
                f.write(f'  Please arrive 15 minutes early prior to the movie! \n')

    def report(self):
        distributed_gifts = dict()
        hourly_dict = dict()
        for ticket in self.tickets:
            hour = ticket.get_time().strftime('%H:')[:-1]
            if isinstance(ticket, SpecialTicket):
                for i in ticket.get_seat_number():
                    if i % 2 == 0:
                        if isinstance(self.studio.get_right_row()[i], SpecialSeat):
                            distributed_gifts[i] = self.studio.get_right_row()[i].get_gift()
                    else:
                        if isinstance(self.studio.get_left_row()[i], SpecialSeat):
                            distributed_gifts[i] = self.studio.get_left_row()[i].get_gift() 

                # if hour in hourly_dict:
                # else:
                #     idx = ticket.get_seat_num()
                #     if idx % 2 == 0:
                #         distributed_gifts[hour] = [self.studio.right[idx].get_gift()]
                #     else:
                #         distributed_gifts[hour] = [self.studio.left[idx].get_gift()]                
            if hour in hourly_dict:
                hourly_dict[hour] += len(ticket.get_seat_number())
                print(hourly_dict[hour])
            else:
                hourly_dict[hour] = len(ticket.get_seat_number())
        print(f'|----------------------------------|')
        print(f'| Hour    |    Number of Booking   |')
        print(f'|----------------------------------|')
        for hour in hourly_dict:
            print(f'| {hour}     :       {hourly_dict[hour]}                |')
            print(f'|----------------------------------|')
        print('All distributed SeatNumber-Gift:')
        for i in distributed_gifts:
            print(f"{i} - {distributed_gifts[i]}")
          
        return hourly_dict, distributed_gifts

class Studio:
    def __init__(self, left_seats, right_seats, _vip_row):
        self.left_row = left_seats
        self.right_row = right_seats
        self.vip_row = _vip_row
        self.current_movies = None
        self.curtains = 'Closed'

    def play_movie(self, movie):
        self.current_movies = movie
        self.curtains = 'Opened'
    
    def get_left_row(self):
        return self.left_row
    
    def get_right_row(self):
        return self.right_row

    def get_vip_row(self):
        return self.vip_row


class Ticket:
    def __init__(self, name: str, seat_num: list, time):
        self.owner_name = name
        self.seat_number = seat_num
        self.time = time

    def get_seat_number(self):
        return self.seat_number

    def get_owner_name(self):
        return self.owner_name
    
    def get_time(self):
        return self.time

    def printed(self):
        return self.owner_name, self.seat_number, self.time


class SpecialTicket(Ticket):
    def __init__(self, name: str, seat_num: list, _time):
        super().__init__(name, seat_num, _time)


class VIPTicket(Ticket):
    def __init__(self, name: str, seat_num: list, _time):
        self.voucher = name + str(seat_num)
        super().__init__(name, seat_num, _time)


class Seat(Seatable):
    def __init__(self, num):
        self.status = False
        self.number = num

    def get_seat_number(self):
        return self.number

    def is_seated(self):
        return self.status

    def seated(self):
        self.status = True


class SpecialSeat(Seat, Seatable):
    def __init__(self, num, gift):
        super().__init__(num)
        self.gift = gift

    def get_gift(self):
        return self.gift

    def seated(self):
        super().seated()


class VIP_Seat(Seat, Seatable):
    def __init__(self, num):
        self.heater = 'Off'
        super().__init__(num)

    def seated(self):
        super().seated()
        self.turn_on_heater()

    def turn_on_heater(self):
        self.heater = 'On'

    def turn_off_heater(self):
        self.heater = 'Off'



