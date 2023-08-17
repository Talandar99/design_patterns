#!/usr/bin/env python


# RealSubject class
class RealSubject:
    def request(self):
        return "RealSubject: Handling request"


# Proxy class using composition
class Proxy:
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        # Additional logic before and after calling the real subject's request
        return f"Proxy: Logging request\n{self.real_subject.request()}\nProxy: Done logging"


def proxy_example():
    real_subject = RealSubject()
    proxy = Proxy(real_subject)

    result = proxy.request()
    print(result)


proxy_example()

