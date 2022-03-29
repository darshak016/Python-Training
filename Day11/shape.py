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