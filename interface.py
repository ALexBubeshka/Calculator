from easygui import *
from rational_calc import *
import sys
def start_inteface():
      msg ="Добро пожаловать в калькулятор\nВыберете один из пунтов"
      title = "Калькулятор"
      choices = ["Операции с рациональными числами", "Операции над комплексными числами"]
      choice = choicebox(msg, title, choices)
      return str(choice)

def choice_interface (choice):
      if choice == "Операции с рациональными числами":
                  text = "Введите данные через пробел\nПример: "
                  title = "Операции с рациональными числами"
                  d_text = "5 / 4 * 6 / 7 + 3 / 2 - 9" # Тут берем данные
                  output = enterbox(text, title, d_text)
      elif choice == "Операции над комплексными числами":
                  text = "Введите данные через пробел\nПример: "
                  title = "Операции над комплексными числами"
                  d_text = "( x1 + iy 1 ) + ( x2 + iy2 ) = ( x1 + x2 ) + i( y1 + y2 )" # Тут берем данные
                  output = enterbox(text, title, d_text)  
      return output
      
def answer (output,x):
      message = str(output) + "=" + str(x) +"\n\nХотите рассчитать снова?"# тут передать данные из функции Вадима
      title = "Решение" 
      output = ynbox(message, title,("Да","Нет"))
      if output:     
            answer(choice_interface(start_inteface()))
      else:     
            sys.exit

answer(choice_interface(start_inteface()),result_output())


