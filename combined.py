
from functions import *

choice = input("Use default files: supervisors.csv, lessons.csv? Y/N: ")
if choice == "Y" or choice == "y":
    c1, c2 = 'supervisors.csv', 'lessons.csv'
else:
    c1, c2 = input("Name of supervisors file: "), input("Name of lessons file: ")
supervisor_file = open(c1,'r', encoding= 'utf8')
lesson_file = open(c2,'r', encoding= 'utf8')

supervisors_list = make_list_of_objects(Supervisors,supervisor_file)
lessons_list = make_list_of_objects(Lessons,lesson_file)
file1 = open('results.txt', 'a')# Δημιουργούμε ένα αρχείο όπου θα αποτυπώσουμε τα αποτελέσματα
for lesson in lessons_list: # Διατρέχουμε την λίστα των αντικειμένων Lessons
    '''Ταξινομούμε κάθε φορά την λίστα των αντικειμένων supervisors σε φθίνουσα σειρά 
    με βάση τα μαθήματα στα οποία πρέπει να παρευρεθούν'''
    supervisors_list = sorted(supervisors_list,key = lambda x:x.numlessons,reverse = True)
    lesson_sup=[]#Δημιουργούμε μια κενή λίστα στην οποία θα αποθηκεύουμε τους επόπτες για το συγκερκιμένο μάθημα
    for supervisor in supervisors_list:#Διατρέχουμε την λίστα των αντικειμένων Supervisors
        if lesson.is_lesson_ready():#Αν το μάθημα χρειάζεται άλλους επόπτες
            if supervisor_availability(supervisor.id, lesson.id, lesson_sup,supervisors_list,lessons_list):# Έλεγχουμε τη διαθεσημότητα του επόπτη για το μάθημα
                lesson_sup.append(supervisor) # Πρόσθετουμε τον επόπτη στη λίστα αφού είναι διαθέσιμος
        else:
            break
    '''Τέλος γράφουμε στο νέο αρχείο
      για κάθε μάθημα τους επόπτες που του ανατέθηκαν '''
    file1.write(f'Exam {lesson.id} with supervisors:\n')
    for supervisor in lesson_sup:
        file1.write(f'{supervisor.name} ({supervisor.email})\n')
    file1.write("\n")
    
supervisor_file.close()
lesson_file.close()
file1.close()