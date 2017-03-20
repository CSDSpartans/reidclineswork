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
 
total_lines_in_file = (line_counter + 11)
print(" ")
print("--End of Poem--")
print(" ")
print(" ")
print("Total number of stanzas in this poem are", stanza_counter)
print("Total number of lines in this file are", total_lines_in_file)
print(" ")
print("Tuesday Afternoon first appeared in the album, Days of Future Passed")
print("Days of Future Passed was released in 1967")
print("The Moody Blues members are Justin Hayward, Mike Pinder, and the London Festival Orchestra")
file_input.close()
