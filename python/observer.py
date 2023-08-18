#!/usr/bin/env python

class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received message: {message}")


class Newsletter:
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def send_news(self, news):
        for subscriber in self.subscribers:
            subscriber.update(news)


def observer():
    subscriber1 = Subscriber("Subscriber 1")
    subscriber2 = Subscriber("Subscriber 2")

    newsletter = Newsletter()
    newsletter.add_subscriber(subscriber1)
    newsletter.add_subscriber(subscriber2)

    newsletter.send_news("Exciting news!")


observer()

