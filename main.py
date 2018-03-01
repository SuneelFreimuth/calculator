

operation = ''
from datetime import datetime
time = datetime.now()

with open('history.txt', 'a') as history:
  history.write('---------------' + '\n')
  history.write( "=== {}/{}/{}  {}:{} ===".format(time.month, time.day, time.year, time.hour, time.minute) + "\n")

  while operation != 'escape':
    operation = input('''What would you like to do?
Options: add, subtract, multiply, divide, escape
> ''')
    result = 0;
    equation = ''
    if operation == 'add':
      firstadd = float(input('First addend? '))
      secondadd = float(input('Second addend? '))
      summed = firstadd + secondadd
      equation = "{} + {} = {}".format(firstadd, secondadd, summed)

    elif operation == 'subtract':
      subtrahend = float(input('Subtrahend? '))
      subtractor = float(input('Subtractor? '))
      difference = subtrahend - subtractor
      equation = "{} - {} = {}".format(subtrahend, subtractor, difference)

    elif operation == 'escape':
      print('Escaped.')
      break
    
    print(equation)
    history.write(equation + '\n')

history.close()
print('Development build 1')
print('This is a statement that will '
  +'appear in Bob\'s Calculator when he pulls it.)