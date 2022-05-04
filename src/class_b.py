"""
@file class_b.py
"""

from registry import registry_get_component_by_name


class ClassB:
    def __init__(self, name):
        self.name = name
        
    def print_a(self):
        cls_a = registry_get_component_by_name('a')
        cls_a.print_me("Hello from class B!")

    def print_me(self, msg: str):
        print(f"From class B - instance '{self.name}': {msg}")


