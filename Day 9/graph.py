class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():

            # remove this vertex from other vertices list
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)

            # delete the vertex
            del self.adjacency_list[vertex]
            return True

        return False

    def print_graph(self):
        for vertex in self.adjacency_list.keys():
            print(vertex, ":", self.adjacency_list[vertex])


my_graph = Graph()

my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")

my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "E")
my_graph.add_edge("C", "D")
my_graph.add_edge("D", "E")

print("Before removing vertex:")
my_graph.print_graph()

my_graph.remove_vertex("D")

print("\nAfter removing vertex D:")
my_graph.print_graph()

class Student:

    # Static method
    @staticmethod
    def get_personal_detail(firstname, lastname):
        print("Your personal detail =", firstname, lastname)

    # Static method
    @staticmethod
    def contact_detail(mobile_no, rollno):
        print("Your contact detail =", mobile_no, rollno)


# Calling static methods using class name
Student.get_personal_detail("Prashant", "Jha")
Student.contact_detail(5456454646, 1001)

# Multiple Inheritance Example

class SubjMarks:   # Parent class 1
    math = int(input("Enter paper marks of Math: "))
    DE = int(input("Enter paper marks of Design Engineering: "))
    c = int(input("Enter paper marks of C Language: "))
    english = int(input("Enter paper marks of English: "))


class PractMarks:  # Parent class 2
    cpract = int(input("Enter practical marks of C Language: "))


class Result(SubjMarks, PractMarks):  # Child class
    def total(self):
        if (self.math >= 40 and
            self.DE >= 40 and
            self.c >= 40 and
            self.english >= 40 and
            self.cpract >= 20):
            print("Pass")
        else:
            print("Fail")


# Object creation
student = Result()

# Calling total method
student.total()