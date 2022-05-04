"""
A simple object registry (or, repository?), 
implemented as a dictionary.
"""

component_registry = {}


def registry_add_component(obj: object, name: str):
    # First check - object by same name exists?
    if name in component_registry.keys():
        print("ERROR: cannot add component - component already registered with same name!")
        return
    # Second check - same object already registered?
    for val in component_registry.values():
        if val is obj: 
            print("ERROR: cannot add component - same component object already in registry!")
            return
    # Checks OK - register object:
    component_registry[name] = obj
    print("Component successfully registered!:-)")


def registry_get_component_by_name(name: str):
    if name in component_registry.keys():
        return component_registry[name]
    else:
        print(f"No component named '{name}' in registry!")
        return None


def registry_get_component_by_type(objtype: type):
    found_obj = None
    found_name = ''
    for name, val in component_registry.items():
        val_type = type(val)
        # print(f"Checking type: {val_type} against {objtype} ...")
        if val_type == objtype:
            print("Gotcha!")
            if found_obj is None:
                found_obj = val
                found_name = name
            else:
                print(f"WARNING: more than 1 object of given type found in registry - returning first match named '{found_name}' !")
    if found_obj is None:
        print(f"WARN: no component with type='{objtype}' in registry!")
    #
    return found_obj


def registry_search(name: str, objtype: type) -> object:
    component = registry_get_component_by_name(name)
    if component:
        # Check if type corresponds to requested object's type:
        if objtype == type(component):
            return component
        else:
            print(f"ERROR: component by name '{name}' is not of object type '{objtype}'!")
            return None
    print(f"Warning - no component by name {name} found in registry - trying type ...")
    component = registry_get_component_by_type(objtype)
    if component:
        return component
    print(f"Warning - no component by type {objtype} found in registry - giving up ...")
    return None



# ******************* TEST ***********************
if __name__ == "__main__":
    from class_a import ClassA
    from class_b import ClassB
    from pprint import pprint

    class ClassC:
        pass

    a = ClassA('A1')
    b = ClassB('B1')
    registry_add_component(a, 'a')
    registry_add_component(b, 'a')   # First failing test ...
    registry_add_component(b, 'b')
    registry_add_component(a, 'c')   # Second failing test ...
    pprint(component_registry)
    aref = registry_get_component_by_name('a')
    aref.print_me('hellu')
    bref = registry_get_component_by_name('b')
    bref.print_me('halla')
    cref = registry_get_component_by_name('c')   # Fail ...
    b2 = ClassB('B2')
    registry_add_component(b2, 'b2')
    oref = registry_get_component_by_type(ClassA)
    if oref:
        oref.print_me('japp')
    oref = registry_get_component_by_type(ClassC)  # Fail ...
    if oref:
        oref.print_me('jappa!')
    oref = registry_get_component_by_type(ClassB)  # Warn ...
    if oref:
        oref.print_me('jazzoo')
    #
    oref = registry_search('a3', ClassA)
    if oref:
        oref.print_me('jabba ...')
    oref = registry_search('b2', ClassA)
    if oref:
        oref.print_me('Hmmmm ...')         # Should NOT be taken!
    

    


