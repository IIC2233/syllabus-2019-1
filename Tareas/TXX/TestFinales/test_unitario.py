from exceptions import NotFoundFile, InvalidTree, NotFoundValue
from os.path import join
import os
from json import load
from tree import AlgarroboTree
from main import search, build_and_save, route

VALUE_ROOT = 1
VALUE_LEFT = 2
VALUE_RIGHT = 3

def get_id():
    i = 1
    while True:
        yield i
        i += 1

ID_TEST = get_id()

def is_valid_tree():
    # Validando árbol
    try:
        tree = AlgarroboTree()
        tree.insert(VALUE_ROOT)

        if tree.root.value != VALUE_ROOT:
            return False

        tree.insert(VALUE_LEFT)
        tree.insert(VALUE_RIGHT)

        if tree.root.left_child.value != VALUE_LEFT:
            return False

        if tree.root.right_child.value != VALUE_RIGHT:
            return False

        for i in range(4, 33):
            tree.insert(i)
            tree.balance()
        
        if tree.root.left_child.left_child.left_child.left_child.value != 16:
            return False
        
        if tree.root.right_child.left_child.left_child.left_child.value != 24:
            return False

    except Exception:
        return False

    return True


def test_search(tree_path: str, value: int, result, my_exception):
    if my_exception is None:  # Revisar resultado
        try:
            return search(tree_path, value) == result
        except Exception as e:
            print(e)
            return False

    try:
        search(tree_path, value)
        return False
    except my_exception as e:
        if isinstance(my_exception, NotFoundValue):
            return tree_path == e.path
        elif isinstance(my_exception, InvalidTree):
            with open(tree_path) as file:
                tree = load(file)
            return tree["value"] == e.tree
        return True
    except Exception as e:
        print(e)
        return False


def print_test(name, result):
    text_number = "{:02d}".format(next(ID_TEST))
    print("| {:^7} | {:^30} | {:^10} |".format(text_number, name, result))


if __name__ == "__main__":
    
    print("| {:^7} | {:^30} | {:^10} |".format("Test", "Type Test", "Result"))
    print("| {:7} | {:30} | {:10} |".format("-"*7, "-"*30, "-"*10))

    total = [0, 0, 0]
    result = [0, 0, 0]

    text = []
    total[0] += 1
    if test_search("FOLDER NOT EXIST", 1, [], NotFoundFile):
        print_test("Invalid path", "Successful")
        result[0] += 1
        text.append(1)
    else:
        text.append(0)
        print_test("Invalid path", "Failed")

    total[0] += 1
    if test_search("FOLDER NOT EXIST GAMMA", 1, [], NotFoundFile):
        print_test("Invalid path", "Successful")
        result[0] += 1
        text.append(1)

    else:
        text.append(0)
        print_test("Invalid path", "Failed")

    total[0] += 1
    if test_search(join("test", "invalid_tree.json"), 2, [], InvalidTree):
        print_test("Invalid Tree", "Successful")
        text.append(1)
        result[0] += 1
    else:
        text.append(0)
        print_test("Invalid Tree", "Failed")

    total[0] += 1
    if test_search(join("test", "invalid_tree_2.json"), 2, [], InvalidTree):
        print_test("Invalid Tree 2", "Successful")
        text.append(1)
        result[0] += 1
    else:
        text.append(0)
        print_test("Invalid Tree 2", "Failed")

    total[0] += 1
    if test_search(join("test", "invalid_tree_3.json"), 2, [], InvalidTree):
        print_test("Invalid Tree 3", "Successful")
        text.append(1)
        result[0] += 1
    else:
        text.append(0)
        print_test("Invalid Tree 3", "Failed")

    total[0] += 1
    if test_search(join("test", "invalid_tree_4.json"), 2, [], InvalidTree):
        print_test("Invalid Tree 4", "Successful")
        text.append(1)
        result[0] += 1
    else:
        text.append(0)
        print_test("Invalid Tree 4", "Failed")


    total[0] += 1
    if test_search(join("test", "valid_tree.json"), 2, [], NotFoundValue):
        print_test("NotFoundValue", "Successful")
        text.append(1)
        result[0] += 1
    else:
        text.append(0)
        print_test("NotFoundValue", "Failed")


    total[0] += 1
    if test_search(join("test", "valid_tree.json"), 4, [4], None):
        print_test("Found route", "Successful")
        text.append(1)
        result[0] += 1
    else:
        text.append(0)
        print_test("Found route", "Failed")

    total[0] += 1
    if test_search(join("test", "valid_tree.json"), 10, [4, 7, 10], None):
        print_test("Found route", "Successful")
        text.append(1)
        result[0] += 1
    else:
        text.append(0)
        print_test("Found route", "Failed")

    total[0] += 1
    if test_search(join("test", "valid_tree_2.json"), 15, [1, 12, 15], None):
        print_test("Found route", "Successful")
        text.append(1)
        result[0] += 1
    else:
        text.append(0)
        print_test("Found route", "Failed")


    if not is_valid_tree():
        for i in range(20):
            text.append("árbol invalido")
        print("Tree not valid")

    else:
        with open(join("test", "trees_build_and_save.json")) as file:
            list_tree = load(file)

        N1 = 10  # Cantidad de test para la consulta 2
        for i in range(N1):
            total[1] += 1
            try:
                # Path para guardar
                output = join("student_solution", f"save_tree_{i+1}.json")

                # Path de la solución
                solution = join("test", f"solution_tree_{i+1}.json")

                # Ejecutar la función
                build_and_save(list_tree[i], output)

                # Cargar solución del alumno
                with open(output) as file:
                    student_answer = load(file)

            # Cargar solución de la consulta
                with open(solution) as file:
                    answer = load(file)

                # Comparar
                if student_answer == answer:
                    text.append(1)

                    print_test("Build AlgarroboTree", "Successful")
                    result[1] += 1
                else:
                    text.append(0)
                    print_test("Build AlgarroboTree", "Failed")

            except Exception as e:
                print_test("Build AlgarroboTree", "Failed")
                print(e)
                text.append("Error {}".format(e))
                pass

        with open(join("test", "trees_route.json")) as file:
            routes_data = load(file)

        N2 = 10  # Cantidad de test para la consulta 3
        for i in range(N2):
            total[2] += 1
            try:

                # Respuesta de la consulta
                answer = routes_data[i]["answer"]

                # Eliminar la respuesta del diccionario
                del routes_data[i]["answer"]

                # Ejecutar la consulta. Le entrego los argumentos con un kwargs
                student_answer = route(**routes_data[i])

                # Comparar
                if student_answer == answer:
                    result[2] += 1
                    print_test("Founding route", "Successful")
                    text.append(1)
                else:
                    text.append(0)
                    print_test("Founding route", "Failed")
                    
            except Exception as e:
                print_test("Founding route", "Failed")
                print(e)
                text.append("Error {}".format(e))

    decimas_array = []
    for i in range(3):
        if result[i] == 0 or total[i] == 0:
            decimas = 0
        else:
            decimas = round(result[i]/total[i], 1)
        decimas_array.append(decimas)
        text2 = """
        Function {}
        Total test:      {:3d}
        Successful test: {:3d}
        Bonus:             {:.1f}
        """.format(i+1, total[i], result[i], decimas)
        print(text2)
