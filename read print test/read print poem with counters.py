#   This reads and prints the whole document.
#           It does not prt a blank line after each line of the file

name_of_mydocument = 'tuesdayafternoon.txt'
file_input = open(name_of_mydocument, 'r')     #open file for reading

line = file_input.readline()
print('      ', line, end = '')
line = file_input.readline()
print('      ', line, end = '')
line = file_input.readline()
print(line, end = '')
line = file_input.readline()


line_counter = 1
stanza_counter = 1
total_lines_in_file = 3

while line != '':                      # while not end of file
    total_lines_in_file += 1
    if line == '\n':
      stanza_counter += 1
      print(" ")
       
    else:
      if line_counter <10:
        print(line_counter, ")   ", line, end = '')
      else:
        print(line_counter, ")  ", line, end = '')
      line_counter +=1
      
    line = file_input.readline()

 
print(" ")
print("--End of Poem--")
print(" ")
print(" ")
print("Total number of stanzas in this poem are", stanza_counter,".")
print("Total number of lines in this file are", total_lines_in_file,".")
print(" ")
print("The song \"Tuesday Afternoon\" first appeared on the album \x1B[3mDays of Future Passed\x1b[23m in 1967.")
print("The Moody Blues members are Justin Hayward, Mike Pinder,  John Lodge, Graeme Edge, Ray Thomas and the London Festival Orchestra.")
file_input.close()
