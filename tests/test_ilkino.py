from ilkino.cinema import Il_Kino
from ilkino.cinema import Ticket
from ilkino.cinema import SpecialSeat
from ilkino.cinema import Seat
# from ilkino import Ticket
from ilkino.cinema import Seatable
from ilkino.cinema import *
import datetime

def test_book_unbooked_seat(monkeypatch):
    inputs = iter([1,'n','jessica',12,'y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    ilkino = Il_Kino(['mobil','payung','pen','laptop','motor'])
    result = ilkino.run()
    assert result == True
    print('test_book_unbooked_seat PASSED!')
    
# def test_book_unbooked_double_seats(monkeypatch):
#     inputs = iter([1,'n','gamaliel',12,'y'    +])
#     monkeypatch.setattr('builtins.input', lambda _: next(inputs))
#     ilkino = Il_Kino(['mobil','payung','pen','laptop','motor'])
#     result = ilkino.run()
#     assert result == True
#     print('test_book_unbooked_seat PASSED!')


def test_book_unknown_seat(monkeypatch):
    inputs = iter([1,'n','dep',37])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    ilkino = Il_Kino(['mobil','payung','pen','laptop','motor'])
    result = ilkino.run()
    assert result == False
    print('test_book_unknown_seat PASSED')
    

def test_book_booked_seat(monkeypatch):
    inputs = iter([1,'n','dep',12,'n',1,'n','gam',12])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    ilkino = Il_Kino(['mobil','payung','pen','laptop','motor'])
    result = ilkino.run()
    assert result == False
    print('test_book_booked_seat PASSED')


def test_book_seat_with_gift(monkeypatch):
    ilkino = Il_Kino(['mobil', 'payung', 'pen', 'laptop', 'motor'])
    special_seat = None
    for seat in ilkino.studio.left_row.values():
        if isinstance(seat, SpecialSeat):
            idx = seat
            break
    inputs = iter([1, 'n', 'gama',12,'y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = ilkino.run()
    assert result == True


def test_get_book_by_hour(monkeypatch):
    inputs = iter([1,'n','Dodi',12,'n',3,'y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    ilkino = Il_Kino(['mobil','payung','pen','laptop','motor'])
    result = ilkino.run()
    current_time = datetime.datetime.now().strftime('%H')
    if current_time in result[0] and result[0][current_time] == 1:
        final_result = True
    else:
        final_result = False 
    expect = True
    assert final_result == expect 
    print('test_book_seat_with_gift PASSED!')


def test_get_all_distributed_gifts(monkeypatch):
    list_gift = ['mobil','payung','pen','laptop','motor']
    ilkino = Il_Kino(list_gift)
    inputs = iter([1, 'n', 'Alice', '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36', 'n', 3, 'y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = ilkino.run()
    status = False
    if len(result[1]) == 10:
        status = True
    assert status == True


def test_search_booked_name(monkeypatch, capsys):
    inputs = iter([1, 'n', 'Alice', 12, 'n', 2, 'Alice', 'y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    ilkino = Il_Kino(['mobil', 'payung', 'pen', 'laptop', 'motor'])
    result = ilkino.run()
    assert result == [12]

    
def test_search_unbooked_name(monkeypatch):
    inputs = iter([2, 'Bob', 'y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    ilkino = Il_Kino(['mobil', 'payung', 'pen', 'laptop', 'motor'])
    result = ilkino.run()
    assert result == None


def test_gift_randomly_assigned_left():
    ilkino1 = Il_Kino(['mobil', 'payung', 'pen', 'laptop', 'motor'])
    ilkino2 = Il_Kino(['kucing', 'anjing', 'topeng', 'mobil', 'CPU'])
    gifts1 = []
    gifts2 = []
    for seat in ilkino1.studio.left_row:
        if isinstance(ilkino1.studio.left_row[seat],SpecialSeat):
            gifts1.append(seat)
    for seat in ilkino2.studio.left_row:
        if isinstance(ilkino2.studio.left_row[seat],SpecialSeat):
            gifts2.append(seat)
    result = gifts1 == gifts2
    expect = False    
    assert result == expect  

def test_gift_randomly_assigned_right():
    ilkino1 = Il_Kino(['mobil', 'payung', 'pen', 'laptop', 'motor'])
    ilkino2 = Il_Kino(['kucing', 'anjing', 'topeng', 'mobil', 'CPU'])
    gifts1 = []
    gifts2 = []
    for seat in ilkino1.studio.right_row:
        if isinstance(ilkino1.studio.right_row[seat],SpecialSeat):
            gifts1.append(seat)
    for seat in ilkino2.studio.right_row:
        if isinstance(ilkino2.studio.right_row[seat],SpecialSeat):
            gifts2.append(seat)
    result = gifts1 == gifts2
    expect = False    
    assert result == expect


def test_should_exit_program(monkeypatch):
    inputs = iter([4])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    Il_Kinoku = Il_Kino(['mobil', 'payung', 'pen', 'laptop', 'motor'])
    result = Il_Kinoku.run()
    assert result == 'Exited'

def test_booked_vip_seat(monkeypatch):
    inputs = iter([1,'y','dep','VIP1',1,'y','gam','VIP1','y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    ilkino = Il_Kino(['mobil','payung','pen','laptop','motor'])
    result = ilkino.run()
    assert result == False
    print('test_book_booked_seat PASSED')



