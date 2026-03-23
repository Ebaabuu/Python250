class Student():
    """Represents a student."""

    # Step 1
    def __init__(self, name = "", id = 0, classes = []):
        self.__name = name
        self.__id = id
        self.__classes = classes

    # Step 2
    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id
    
    # Step 3
    def addClass(self, className):
        notInList = False
        if className not in self.__classes:
            notInList = True
            self.__classes.append(className)
        return notInList
    
    # Step 4
    def removeClass(self, className):
        inList = False
        if className in self.__classes:
            inList = True
            self.__classes.remove(className)
        return inList

    # Step 5
    def getClasses(self):
        return self.__classes
  
    # Step 6
    def __str__(self):
        return f"{self.__name} ({self.__id}) - {len(self.__classes)}"
