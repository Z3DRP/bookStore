class Book:
    """book object"""
    def __init__(self, name, author, has_read=False):
        self.Name = name
        self.Author = author
        self.Has_Read = has_read
        self.validate_data()

    def __repr__(self):
        return f"<Book: {self.Name, self.Author, self.Has_Read}>"

    def __str__(self):
        return f"{self.Name}: Author - {self.Author}, Read: {self.Has_Read}"

    def validate_data(self):
        try:
            if not isinstance(self.Name, str):
                raise ValueError("Error, book name cannot be numeric")
            elif not isinstance(self.Author, str):
                raise ValueError("Error, book author cannot be numeric")
            elif not isinstance(self.Has_Read, bool):
                raise ValueError("Error, has read must be a bool")
        except Exception:
            raise Exception("An error has occurred for some reason")




