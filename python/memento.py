#!/usr/bin/env python

class EditorMemento:
    def __init__(self, content):
        self.content = content


class Editor:
    def __init__(self):
        self.content = ""
        self.history = []

    def type(self, words):
        self.content += words

    def save(self):
        self.history.append(EditorMemento(self.content))

    def undo(self):
        if self.history:
            last_state = self.history.pop()
            self.content = last_state.content

    def show_content(self):
        print("Current Content:", self.content)


def memento():

    editor = Editor()

    editor.type("Hello, ")
    editor.show_content()
    editor.save()
    print("[save]")

    editor.type("there ")
    editor.type("General ")
    editor.type("Kenobi")
    editor.show_content()
    editor.save()
    print("[save]")

    editor.type("zxcfasdcdc ")

    editor.show_content()
    editor.undo()
    print("[undo]")

    editor.show_content()
    editor.undo()
    print("[undo]")

    editor.show_content()


memento()
