class TicketService:
    def __init__(self):
        self.tickets = []

    def create_ticket(self, ticket):
        ticket_data = ticket.model_dump()
        ticket_data["id"] = len(self.tickets) + 1
        ticket_data["status"] = "open"

        self.tickets.append(ticket_data)

        return ticket_data

    def get_tickets(self):
        return self.tickets
