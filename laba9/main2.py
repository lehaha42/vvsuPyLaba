from time import time


class Ticket:
    def __init__(self, title, description, ticket_id=None, status="Новая", timestamp=None):
        self.id = id(self)
        if ticket_id:
            self.id = ticket_id
        self.title = title
        self.description = description
        self.status = status
        self.timestamp = timestamp if timestamp else time()

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Заголовок: {self.title}\n"
                f"Описание: {self.description}\n"
                f"Статус: {self.status}\n"
                f"Метка времени: {self.timestamp}")


class TicketSystem:
    VALID_TRANSITIONS = {
        "Новая": ["В обработке", "Отложена"],
        "В обработке": ["Обработана", "Отложена"],
        "Отложена": ["В обработке"],
        "Обработана": []
    }

    def __init__(self):
        self.tickets = {}
        self.next_id = 1

    def add_ticket(self, title, description):
        ticket = Ticket(title, description, ticket_id=self.next_id)
        self.tickets[ticket.id] = ticket
        self.next_id += 1
        print(f"Заявка создана с ID: {ticket.id}")
        return ticket.id

    def edit_ticket(self, ticket_id, title=None, description=None):
        if ticket_id not in self.tickets:
            print("Заявка не найдена")
            return False

        ticket = self.tickets[ticket_id]
        if title:
            ticket.title = title
        if description:
            ticket.description = description
        print("Заявка отредактирована")
        return True

    def get_ticket(self, ticket_id):
        if ticket_id not in self.tickets:
            print("Заявка не найдена")
            return None
        return self.tickets[ticket_id]

    def list_tickets(self):
        sorted_tickets = sorted(self.tickets.values(), key=lambda t: t.timestamp)
        for ticket in sorted_tickets:
            print(f"ID: {ticket.id}, Заголовок: {ticket.title}, "
                  f"Дата: {ticket.timestamp.strftime('%Y-%m-%d %H:%M')}")

    def change_status(self, ticket_id, new_status):
        if ticket_id not in self.tickets:
            print("Заявка не найдена")
            return False

        ticket = self.tickets[ticket_id]
        if new_status not in self.VALID_TRANSITIONS.get(ticket.status, []):
            print(f"Недопустимый переход из '{ticket.status}' в '{new_status}'")
            return False

        ticket.status = new_status
        print(f"Статус изменён на: {new_status}")
        return True


if __name__ == '__main__':
    pass
