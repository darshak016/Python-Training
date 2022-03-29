"""Create a class Shape with __init__, __repr__, __eq__, __gt__, __lt__ functions. 
These functions should raise NotImplementedError when called with an object of Shape class. 
Add valid docstrings containing description, and usage, parameter and return details as applicable.
"""


class Shape:
    def __init__(self):
        """[description]
            this function is called when object of shape class is created
        Raises:
            NotImplementedError:
        """
        raise NotImplementedError()

    def __repr__(self):
        """[summary]
            Represent object as a string
        Raises:
            NotImplementedError: [description]
        """
        raise NotImplementedError()

    def __eq__(self, other):
        """[summary]

        Args:
            other ([type]): [description]

        Raises:
            NotImplementedError: [description]
        """
        return NotImplementedError()
    

    def __gt__(self, other):
        """[summary]

        Args:
            other ([type]): [description]

        Raises:
            NotImplementedError: [description]
        """
        return NotImplementedError()

    def __lt__(self, other):
        """[summary]

        Args:
            other ([type]): [description]

        Raises:
            NotImplementedError: [description]
        """
        return NotImplementedError()


def main():
    obj_shape = Shape()
    print(obj_shape.__repr__())


if __name__ == "__main__":
    main()
