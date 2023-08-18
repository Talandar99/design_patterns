#!/usr/bin/env python

class ChatRoomMediator:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive_message(message)


class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(message, self)

    def receive_message(self, message):
        print(f"{self.name} receives: {message}")


def mediator():
    chat_mediator = ChatRoomMediator()

    user1 = User("Alice", chat_mediator)
    user2 = User("Bob", chat_mediator)
    user3 = User("Charlie", chat_mediator)

    chat_mediator.add_user(user1)
    chat_mediator.add_user(user2)
    chat_mediator.add_user(user3)
    user1.send("Hello everyone!")
    print("")
    user2.send("Hey Alice!")
    print("")
    user3.send("Hi there!")


mediator()
