def calculate_ticket_cost(num_tickets, room_type, hour, cinema_card, reservation):
    room_rates = {"Dinamix": 18800, "3D": 15500, "2D": 11300}
    basic_rate = room_rates[room_type]
    costo = basic_rate
    
    if hour:
        if room_type in ["3D", "2D"]:
            costo *= 1.25
        elif room_type == "Dinamix":
            costo *= 1.5

    if not hour:
        costo *= 0.9

    if num_tickets >= 3:
        costo -= 500 * (num_tickets - 2)

    if cinema_card:
        costo *= 0.95

    if reservation:
        costo += 2000 * num_tickets

    return int(costo * num_tickets)

costo = calculate_ticket_cost(3, "2D", True, True, False)
print(costo)  



