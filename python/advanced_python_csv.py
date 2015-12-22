import csv
import itertools

'''
We cannot pass the csvReader as function argument. So in order to save it,
we create two classes to store the information in memory.
The first class is Faculty and stores all the Faculty personnel.
The second class is Person and stores the information for each Person in the Faculty
'''
class Person:
  def __init__(self,name,title,email,degrees):
    self.name = name
    self.title = title
    self.email = email
    self.degrees = degrees

  def __str__(self):
    return 'Name: %s | Title: %s | Email: %s | Degrees: %s ' % (self.name, self.title, self.email, self.degrees)

class Faculty:
  facultyPersonnel = []
  degrees = {}
  titles = {}
  emails = []
  emailDomains = {}

  def __init__(self): pass

  def __init__(self, dictReader): #build Faculty with Dictionary reader from csv
    for row in dictReader:
      self.addPerson(Person(row['name'],row['title'],row['email'],row['degree']))
    self.degreesAndFrequencies()
    self.titlesAndFrequencies()
    self.getEmails()
    self.getEmailDomains()

  def addPerson(self,Person):
    self.facultyPersonnel.append(Person)

  def printFaculty(self):
    for person in self.facultyPersonnel:
      print(person)

  #Contains answer to Q1 (question 1)
  def degreesAndFrequencies(self):
    for person in self.facultyPersonnel:
      degrees = filter(None,person.degrees.replace('.','').split(' ')) # get all the degrees of a person
      for degree in degrees:
        if degree not in self.degrees:
          self.degrees[degree] = 1 #new dictionary degree with frequency initialized to one
        else:
          self.degrees[degree] += 1 #increment frequency of degree

  #Contains answer to Q2 (question 2)
  def titlesAndFrequencies(self):
    for person in self.facultyPersonnel:
      if person.title not in self.titles:
        self.titles[person.title] = 1
      else:
        self.titles[person.title] += 1

  #Contains answer to Q3 (question 3)
  def getEmails(self):
    for person in self.facultyPersonnel:
      self.emails.append(person.email)

  def getEmailDomains(self):
    for person in self.facultyPersonnel:
      ext = person.email.split('@')[1]
      if ext not in self.emailDomains:
        self.emailDomains[ext] = 1
      else:
        self.emailDomains[ext] += 1

  #Contains answer to Q4 (question 4)
  def findUniqueEmailDomains(self):
    list = []
    print(self.emailDomains)
    for domain in self.emailDomains:
      if self.emailDomains[domain] == 1:
        list.append(domain)
    return list

  def printDegrees(self):
    print("\nFaculty degrees and their frequencies:")
    print(self.degrees)

  def printTitles(self):
    print("\nFaculty titles and their frequencies:")
    print(self.titles)

  def printEmails(self):
    print("\nFaculty emails: ")
    for email in self.emails:
      print(email)

  def printEmailDomains(self):
    print("\nFaculty email domains:")
    for domain in self.emailDomains:
      print(domain)

  def printUniqueDomains(self):
    uniqueDomains = self.findUniqueEmailDomains()
    print("\nFaculty unique email domains:")
    for domain in uniqueDomains:
      print(domain)

  def printNElementsFromDict(self, n, dict):
    n_items = list(itertools.islice(dict.items(),n))
    for item in n_items:
      print(item)

  #Contains answer to Q6 (question 6)
  def buildDictionaryQ6(self):
    dic = {}
    for person in self.facultyPersonnel:
      lst = []
      familyName = person.name.rsplit(None, 1)[-1]
      if familyName not in dic:
        dic[familyName] = [[person.degrees,person.title,person.email]]
      else:
        dic[familyName].append([person.degrees,person.title,person.email])
    
    print("\nNew dictionary format (Q6):")
    self.printNElementsFromDict(3,dic)

  #Contains answer to Q7 (question 7)
  def buildDictionaryQ7(self):
    dic = {}
    for person in self.facultyPersonnel:
      nameValues = person.name.split(None)
      firstName = nameValues[0]
      lastName = nameValues[-1]
      dic[(firstName,lastName)] = [person.degrees,person.title,person.email]

    print("\nNew dictionary format (Q7):")
    self.printNElementsFromDict(3,dic)

with open('faculty.csv','rt') as csvfile:
  dictReader = csv.DictReader(csvfile,skipinitialspace = True)

  #degrees, titles, emails and domain names are computed on construction
  faculty = Faculty(dictReader)

#Q1. Find how many different degrees there are, and their frequencies:
#print degrees and their frequencies
faculty.printDegrees()

#Q2. Find how many different titles there are, and their frequencies:
#print titles and their frequencies
faculty.printTitles()

#Q3. Search for email addresses and put them in a list
#print faculty emails
faculty.printEmails()

#Q4. Find how many different email domains there are (Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). Print the list of unique email domains.
#print domain names with frequencies and print unique domain names
faculty.printEmailDomains()
faculty.printUniqueDomains()

#Q5. Write email addresses from Part I to csv file


'''
Q6. Create a dictionary in the below format:

faculty_dict = { 'Ellenberg': [\
            ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
            ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
                          ],
            'Li': [\
            ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
            ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
            ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                          ]
          }
'''
faculty.buildDictionaryQ6()

'''
Q7. The previous dictionary does not have the best design for keys. Create a new dictionary with keys as:

professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
                ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
                ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
                ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
                ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
            }
'''
faculty.buildDictionaryQ7()