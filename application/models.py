from application import db

# class Data inherent from db.Model which is a declarative base
# The baseclass for all your models is called db.Model
class Data(db.Model):
    # defining the columns in this table with db.Column() object instantiation
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(128), index=True, unique=False)
    
    # When a class defines an __init__() method,
    # class instantiation automatically invokes __init__() for the newly-created class instance
    # e.g. when: x = MyClass() 
    # note: self is always the first and must-have parameter for class methods
    # The second one positionally is the first one when initializing the instance.
    def __init__(self, notes):
        # self.notes refers to the instance notes created just now.
        # ?? would this overright the initial notes declared above?
        self.notes = notes

    # __repr__ is a method for class Data to have a printable self
    # This is generally a great practice for easier debugging
    # In this case the __repr__ method is just self.notes 
    def __repr__(self):
        return '<Data %r>' % self.notes
