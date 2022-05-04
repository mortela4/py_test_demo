"""
@file class_a.py
"""

from registry import registry_get_component_by_name


class ClassA:
    def __init__(self, name):
        self.name = name

    def print_b(self):
        cls_b = registry_get_component_by_name('b')
        cls_b.print_me("Hello from class A!")

    def print_me(self, msg: str):
        print(f"From class A - instance '{self.name}': {msg}")



