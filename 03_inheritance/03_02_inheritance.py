# CLASSES AND INHERITANCE
# =======================
# 1) Define an empty `Movie()` class.
# 2) Add a dunder init method that takes two arguments `year` and `title`
# 3) Create a sub-class called `RomCom()` that inherits from the `Movie()` class
# 4) Create another sub-class of the `Movie()` class called `ActionMovie()`
#     that overwrites the dunder init method of `Movie()` and adds another
#     instance variable called `pg` that is set by default to the number `13`.
# 5) Practice planning out and flushing out these classes even more.
#     Take notes in your notebook. What other attributes could a `Movie()` class
#     contain? What methods? What should the child classes inherit as-is or overwrite?

class Movie:
    
    def __init__(self, year, title, run_time, sequel_num = 1):
        self.year = year
        self.title = title
        self.run_time = run_time
        self.sequel_num = sequel_num
    
    def sequel(self, new_year, new_run_time):
        if self.sequel_num == 1:
            new_title = self.title + " 2"
        else:
            new_title = self.title[:-1] + f"{self.sequel_num + 1}"
        return Movie(new_year, new_title, new_run_time, self.sequel_num + 1)
    
    def __str__(self):
        return f"{self.title} : {self.year} - {self.run_time} mins long."
    
    def __repr(self):
        my_str = (f"Title: {self.title}\n"
            f"Year: {self.year}\n"
            f"Run Time: {self.run_time}\n"
            f"Sequel Number: {self.sequel_num}\n"
            )
        return my_str

s = Movie(2001, 'Shrek', 90)
print(s)
t = s.sequel(2004, 93)
print(t)
k = t.sequel(2007, 93)
print(k)

class RomCom(Movie):
    
    def __str__(self):
        return f"RomCom: {self.title} ({self.year}) - {self.run_time} mins long."

a = RomCom(2030, 'Future Rom Com', 110)
print(a)

class ActionMovie(Movie):
    
    def __init__(self, year, title, run_time, sequel_num, pg = 13):
        super().__init__(year, title, run_time, sequel_num)
        self.pg = pg
    
    def __str__(self):
        return f"Action: {self.title} ({self.year}) - {self.run_time} mins long."

b = ActionMovie(2050, 'Future Action Movie', 130, 1, 18)
print(b)