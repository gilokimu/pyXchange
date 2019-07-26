import marshmallow


class SchemaBase(marshmallow.Schema):
    """
        Base Schema class
    """

    data = {}

    def get(self, key):
        """
        :param key: in the dictionary
        :return: value associated with the key in the data dictionary
        """
        if key in self.data.keys():
            return self.data[key]

        return None
