
class Supervisors:
    def __init__(self, id, name, email, numlessons, restrictions):
        self.skip_restriction=2
        self.id=id
        self.name=name
        self.email=email
        self.numlessons=numlessons
        self.restrictions=restrictions
    def is_supervisor_full(self):
        if self.numlessons == 0:
            return True
        else:
            return False
      
class Lessons:
    def __init__(self,id,date_time,rooms,semester,teacher,No_supervisors):
        self.id = id
        self.date_time = date_time
        self.rooms = rooms
        self.semester = semester 
        self.teacher = teacher 
        self.No_supervisors = No_supervisors
    def is_lesson_ready(self):
        if self.No_supervisors == 0:
            return False
        else:
            return True

def make_line_list(file):
    for line in file: #Διατρέχουμε το αρχείο
        line_list = line.split(',') #Δημιουργούμε μια λίστα κάθε γραμμής με βάση το ','
        line_list[-1]=line_list[-1].strip() #αφαιρεί τον χαρακτήρα \n στο τελευταίο στοιχείο
        return line_list #επιστρέφει τη λίστα 
    
def make_list_of_objects(clas,opened_file):
    '''Δημιουργεί μια λίστα από αντικείμενα'''
    headers=make_line_list(opened_file) #αφαιρούμε την πρώτη σειρά του αρχείου
    list_of_objects=[]
    while True:
        current=make_line_list(opened_file) # αναθέτουμε στη μεταβλητή current κάθε φορά τη λίστα κάθε γραμμής του αρχείου
        if current!=None:
            if len(current) == 6: # ελέγχουμε εάν διαχειριζόμαστε το αρχείο με τους επόπτες ή αυτό με τα μαθήματα
                list_of_objects.append(clas(int(current[0]), current[1], current[2], current[3], current[4],int(current[5]))) #δημιουργούμε αντικείμενα με βάση της current και τα προσθέτουμε στη λίστα
            else:
                list_of_objects.append(clas(int(current[0]), current[1], current[2], int(current[3]), current[4]))
        else:
            break # τερματίζει η επαναληπτική όταν έχει τελειώσει η ανάγνωση του αρχείου
    return list_of_objects #επιστρέφει τη λίστα των ααντικειμένων 

def supervisor_availability(supervisor_id, lesson_id, lesson_l,list_of_supervisors,list_of_lessons):
    '''Ελέγχει τη διαθεσιμότητα ενός επόπτη για ένα συγκεκριμένο μάθημα'''
    for c_superv in list_of_supervisors:# τρέχουμε την λίστα των αντικείμενων με τους επόπτες
        if c_superv.id==supervisor_id: # κάνουμε αναζήτηση για να βρόυμε τον σωστό επόπτη
            if c_superv.is_supervisor_full() or c_superv in lesson_l: # Ελέγχουμε εάν ο επόπτης δεν μπορεί να ανατεθεί σε μάθημα ή εάν έχει ήδη ανατεθεί στο μάθημα
                return False
            restriction = c_superv.restrictions # αναθέτουμε στη μεταβλητή restriction τους περιορισμούς του επόπτη
            new_restriction = restriction[1:-1] # αφαιρούμε τις ' [] ' 
            restriction_mini_list = new_restriction.split() # δημιουργούμε μια νέα λίστα με βασή το space ' '
            for x in restriction_mini_list: # προσπελαύνουμε τη λίστα 
                if lesson_id == int(x): #ελέγχουμε εάν το μάθημα που εξετάζουμε ανήκει στους περιορισμούς του επόπτη
                    return False #εάν το βρούμε στους περιορισμόυς τότε σταματάμε
            '''Αλλίως εάν βρέθηκε μειώνουμε κατα 1 τους επόπτες που χρειάζεται το 
            συγκεκριμένο μάθημα όπως και μειώνουμε τα μαθήματα που πρέπει να βρεθεί ο επόπτης '''
            c_superv.numlessons = c_superv.numlessons - 1
            for c_lesson in list_of_lessons:
                if c_lesson.id==lesson_id:
                    c_lesson.No_supervisors = c_lesson.No_supervisors - 1
            return True