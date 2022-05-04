from class_a import ClassA
from class_b import ClassB
from registry import registry_add_component


if __name__ == "__main__":
    a = ClassA('A1')
    b = ClassB('B1')
    # Add components:
    registry_add_component(a, 'a')
    registry_add_component(b, 'b') 
    # Call each other's 'print_me()' method:
    a.print_b()
    b.print_a()

