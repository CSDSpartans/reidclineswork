#   This reads and prints the whole document.
#           It does not prt a blank line after each line of the file

name_of_mydocument = 'tuesdayafternoon.txt'
file_input = open(name_of_mydocument, 'r')     #open file for reading

line = file_input.readline()
print(line)
line = file_input.readline()
print(line)
line = file_input.readline()
print(line)
line = file_input.readline()

line_counter = 1
stanza_counter = 1

while line != '':                      # while not end of file
    if line == '\n':
      stanza_counter += 1
      print(" ")
    else:
      if line_counter <10:
        print(line_counter, ")   ", line, end = '')
      else:
        print(line_counter, ")  ", line, end = '')
      line_counter += 1
      
    line = file_input.readline()
 


print(" ")
print(" ")
print("The number of stanzas is", stanza_counter)

file_input.close()
