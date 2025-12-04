from models.Book import Book

b1 = Book()
b1.setId("1")
b1.setName("1984")
b1.setAuthor("George Orwell")
b1.setPublisher("Panini")
b1.setTotalPages("433")
b1.setReadedPages("233")

print(b1.getId())
print(b1.getName())
print(b1.getAuthor())
print(b1.getPublisher())
print(b1.getTotalPages())
print(b1.getReadedPages())