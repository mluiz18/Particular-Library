class Book:

    def __init__(self):
        self.__id = None
        self.__name = None
        self.__author = None
        self.__publisher = None
        self.__totalpages = None
        self.__readedpages = None

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAuthor(self, author):
        self.__author = author

    def getAuthor(self):
        return self.__author

    def setPublisher(self, publisher):
        self.__publisher = publisher

    def getPublisher(self):
        return self.__publisher

    def setTotalPages(self, totalpages):
        self.__totalpages = totalpages

    def getTotalPages(self):
        return self.__totalpages

    def setReadedPages(self, readedpages):
        self.__readedpages = readedpages

    def getReadedPages(self):
        return self.__readedpages