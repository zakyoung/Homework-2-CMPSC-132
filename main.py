import random
class Course:
  '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
  '''
  """
  Course class that allows you to create a new course to be listed on the catalog
  """
  def __init__(self, cid, cname, credits):
    self.cid = cid
    self.cname = cname
    self.credits = credits
  def __str__(self):
    return f'{self.cid}({self.credits}): {self.cname}'

  __repr__ = __str__

  def __eq__(self, other):
    if isinstance(self,Course) and isinstance(other,Course):
      if self.cid == other.cid:
        return True
      else:
        return False
    else:
      return False

class Catalog:
  ''' 
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.courseOfferings
        {'CMPSC132': CMPSC132(3): Programming in Python II, 'CMPSC360': CMPSC360(3): Discrete Mathematics}
        >>> C.removeCourse('CMPSC360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC132': CMPSC132(3): Programming in Python II}
        >>> isinstance(C.courseOfferings['CMPSC132'], Course)
        True
  '''
  """
  The catalog class creates course objects.
  Attributes:
    courseOffering- Dictionary of courses where the key is the cid and the value is the course

  Methods:

    addCourse - Allows for a new course to be created and added to course courseOfferings

    remove Course - if the course in in current offerings removes it from the course dictionary
  """
  def __init__(self):
    #id is key course is value
    self.courseOfferings = {}
  def addCourse(self, cid, cname, credits):
    if cid not in self.courseOfferings:
      self.courseOfferings[cid] = Course(cid,cname,credits)
      return "Course added successfully"
    else:
      return "Course already added"

  def removeCourse(self, cid):
    if cid not in self.courseOfferings:
      return "Course not found"
    else:
      del self.courseOfferings[cid]
      return "Course removed successfully"

class Semester:
  '''
  >>> cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
  >>> cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
  >>> math230 = Course("MATH 230", 'Calculus', 4)
  >>> phys213 = Course("PHYS 213", 'General Physics', 2)
  >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
  >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
  >>> semester = Semester(1)
  >>> semester
  No courses
  >>> semester.addCourse(cmpsc132)
  >>> semester.addCourse(math230)
  >>> semester
  CMPSC132, MATH 230
  >>> semester.isFullTime
  False
  >>> semester.totalCredits
  7
  >>> semester.addCourse(phys213)
  >>> semester.addCourse(econ102)
  >>> semester.addCourse(econ102)
  'Course already added'
  >>> semester.addCourse(phil119)
  >>> semester.isFullTime
  True
  >>> semester.dropCourse(phil119)
  >>> semester.addCourse(Course("JAPNS 001", 'Japanese I', 4))
  >>> semester.totalCredits
  16
  >>> semester.dropCourse(cmpsc131)
  'No such course'
  >>> semester.addCourse(Course(42, 'name',"zero credits"))
  'Invalid course'
  >>> semester.courses
  [CMPSC132(3): Programming in Python II, MATH 230(4): Calculus, PHYS 213(2): General Physics, ECON 102(3): Intro to Economics, JAPNS 001(4): Japanese I]
   '''
  """
    The semester class creates a registers a new semester and adds classes to it
    Methods:
    addCourse - if a proper course object is provided it adds the course to the semester courses attribute

    RemoveCourse - converse to the addCourse class except it removes courses from the semester courses attribute

    totalCredits - property method that calculates the number of credits based on enrolled classes. uses a sum() to total up the cids in the list of course objects

    isFullTIme - checks to see if totalCredits is >= 12
   """
  def __init__(self, sem_num):
    self.sem_num = sem_num
    self.courses = []

  def __str__(self):
    if len(self.courses) > 0:
      return ', '.join([course.cid for course in self.courses])
    else:
      return "No courses"

  __repr__ = __str__

  def addCourse(self, course):
    if isinstance(course, Course) and isinstance(course.cid and course.cname,str) and isinstance(course.credits,int):
      if course.cid not in [coursecid.cid for coursecid in self.courses]:
        self.courses.append(course)
        return
      else:
        return "Course already added"
    else:
      return "Invalid course"

  def dropCourse(self, course):
    if isinstance(course, Course):
      if course.cid in [coursecid.cid for coursecid in self.courses]:
        self.courses.remove(course)
        return None
      else:
        return "No such course"
    else:
      return "Invalid course"

  @property
  def totalCredits(self):
    self.credits = sum([course.credits for course in self.courses])
    return self.credits

  @property
  def isFullTime(self):
    if self.totalCredits >= 12:
      return True
    else:
      return False
class Loan:
  '''
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.getLoan(4000)
        'Not full-time'
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2)
        'Course added successfully'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC360', C,1)
        'Course added successfully'
        >>> s1.getLoan(4000)
        'Not full-time'
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> s1.getLoan(4000)
        >>> s1.account.loans
        {27611: Balance: $4000}
        >>> s1.getLoan(6000)
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $6000}
    '''
  """
    creates a new loan and generates a random id for that loan
  """
  def __init__(self, amount):
    self.amount = amount
    self.loan_id = self.__loanID
  def __str__(self):
    return f"Balance: ${self.amount}"
  __repr__ = __str__
  @property
  def __loanID(self):
    return random.randint(10000,99999)
class Person:
  '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
  '''
  """
  This makes a person object that has a name and social security number
  This class is inherited by the staff and student classes

  ssn is a private attribute and can only be retrived from the get_ssn method
  """
  def __init__(self, name, ssn):
    self.name = name
    self.__ssn = ssn

  def __str__(self):
    return f"Person({self.name}, ***-**-{self.__ssn[7:]})"

  __repr__ = __str__

  def get_ssn(self):
    return self.__ssn


  def __eq__(self, other):
    if isinstance(self,Person) and isinstance(other,Person):
      return self.get_ssn() == other.get_ssn()
    else:
      return False
class Staff(Person):
  '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> st1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC360', C, 1)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC132}
  '''
  """
  class that creates a staff object

  This class has methods such as getSupervisor, setSupervisor, applyHold, removeHold, and unenrollStudent. These are pretty self documenting with the getSupervisor and setSupervisor affecting the staff object while the applyHold, removeHold, and unenrollStudent affecting the given student instance.
  """
  def __init__(self, name, ssn, supervisor=None):
    super().__init__(name,ssn)
    self.__supervisor = supervisor

  def __str__(self):
    return f"Staff({self.name}, {self.id})"
  
  __repr__ = __str__

  @property
  def id(self):
    initials = ''.join([name[0].lower() for name in self.name.split()])
    return f"905{initials}{self.get_ssn()[7:]}"

  @property   
  def getSupervisor(self):
    return self.__supervisor

  def setSupervisor(self, new_supervisor):
    if isinstance(new_supervisor,Staff):
      self.__supervisor = new_supervisor
      return "Completed!"
    return None

  def applyHold(self, student):
    if isinstance(student,Student):
      student.hold = True
      return "Completed!"
    else: 
      return None

  def removeHold(self, student):
    if isinstance(student,Student):
      student.hold = False
      return "Completed!"
    else:
      return None

  def unenrollStudent(self, student):
    if isinstance(student,Student):
      student.active = False
      return "Completed!"
    else:
      return None
class StudentAccount:
  '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2)
        'Course added successfully'
        >>> C.addCourse('CMPEN270', 'Digital Design', 4)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
  '''
  """
  This is the students account which is individual to every student instance

  The creditCost is outside the intialization so a change to it should affect all of the instances of the class

  This class has 2 main methods: makePayment and chargeAccount. makePayment is you paying off the balance you owe and chargeAccount is adding to the money you owe
  """
  creditCost = 1000
  def __init__(self, student):
    self.student = student
    self.balance = 0
    self.loans = {}

  def __str__(self):
    return f'Name: {self.student.name}\nID: {self.student.id}\nBalance: ${self.balance}'

  __repr__ = __str__

  def makePayment(self, amount):
    self.balance-=amount
    return self.balance

  def chargeAccount(self, amount):
    self.balance+=amount
    return self.balance

class Student(Person):
  '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC311', C, 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132, CMPSC360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC132', C, 1)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC360', 1)
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC360', 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: No courses}
        >>> s1.enrollCourse('CMPSC360', C, 2)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
  '''
  """
  The student class has many methods with the main ones being: 
    __createStudentAccount - private method that creates a student account

    id - Creates a new id based on the person instances name and ssn

    registerSemester - allows you to create a new semester object and it adds this new instance to the semesters dictionary and based on the len of the dictionary

    enroll course - enrolls in a course by referince the course offerings and adding it to the students semester object

    drop course - drops course from the semester instance for the student

    get loan - creates a new loan for the student if they are active and have no holds
  """
  def __init__(self, name, ssn, year):
    random.seed(1)
    super().__init__(name,ssn)
    self.year = year
    self.semesters = {}
    self.hold = False
    self.active =True
    self.account = self.__createStudentAccount()

  def __str__(self):
    return f"Student({self.name}, {self.id}, {self.year})"

  __repr__ = __str__

  def __createStudentAccount(self):
    if self.active:
      return StudentAccount(self)
    else:
      return None


  @property
  def id(self):
    initials = ''.join([name[0].lower() for name in self.name.split()])
    return f"{initials}{self.get_ssn()[7:]}"

  def registerSemester(self):
    if self.hold == False and self.active == True:
      self.semesters[len(self.semesters)+1] = Semester(len(self.semesters)+1)
      if len(self.semesters) <= 2:
        self.year = "Freshman"
      elif len(self.semesters) < 5:
        self.year = "Sophomore"
      elif len(self.semesters) < 7:
        self.year = "Junior"
      else:
        self.year = "Senior"
      return None
    else:
      return "Unsuccessful operation"

  def enrollCourse(self, cid, catalog, semester):
    #Finds a Course object with the given id from the catalog and adds it to the courses attribute of the
    #Semester object. Charge the student’s account the appropriate amount of money.#
    if self.hold == False and self.active == True:
      if cid in catalog.courseOfferings:
        if catalog.courseOfferings[cid] not in self.semesters[semester].courses:
          self.semesters[semester].addCourse(catalog.courseOfferings[cid])
          self.account.chargeAccount(StudentAccount.creditCost*catalog.courseOfferings[cid].credits)
          return 'Course added successfully'
        else:
          return "Course already enrolled"
      else:
        return 'Course not found'
    else:
      return "Unsuccessful operation"
    #self.account.chargeAccount()
    #confused on how to charge them the amount

  def dropCourse(self, cid, semester):
    if not self.hold and self.active:
      for course in self.semesters[semester].courses:
        if course.cid == cid:
          self.semesters[semester].dropCourse(course)
          return "Course dropped successfully"
        else:
          continue
      return "Course not found"
    else:
      return "Unsuccessful operation"

  def getLoan(self, amount):
    if len(self.semesters) > 0:
      if self.active and self.semesters[max(self.semesters)].isFullTime:
        loan = Loan(amount)
        self.account.loans[loan.loan_id] = loan
        self.account.makePayment(loan.amount)
      elif not self.active:
        return "Unsuccessful operation"
      else:
        return "Not full-time"
    else:
      return "Not full-time"

def createStudent(person):
    """
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> s = createStudent(p)
        >>> s
        Student(Jason Smith, js2629, Freshman)
        >>> isinstance(s, Student)
        True
    """
    new_student = Student(person.name,person.get_ssn(),'Freshman')
    return new_student