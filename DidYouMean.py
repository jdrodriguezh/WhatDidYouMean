#!/usr/bin/python3

# -----------------------------------------------------------
# Proyecto I de Sistemas Inteligentes
# Did you mean...?
# Desarrollado por Josué Rodríguez (11641196)
# Comandos implementados: ls, df, ping
# -----------------------------------------------------------

import subprocess as sp
import re

#Bloque de código que ejecuta el comando
def execute(args):
  try:
    #print("trying...")
    if(args[0] == "ping"):
      p1 = sp.Popen([args[0], '-c 2', args[1]], stdout=sp.PIPE)
      #output = p1.communicate()[0]
      #print(output)
      output = p1.communicate()[0].decode("utf-8")
      #communicate devuelve algo en bytes, utilizamos decode para pasarlo a string
      messageRcvd = output.split("\n")
      for message in messageRcvd:
        print(message)
    else:
      sp.call(args)
  except:
    #print("failing...")
    print("Command '{}' not defined".format(args))
#----------------------------------------

#Bloque de código que analiza la entrada erronea
def analyze(args, correct, list):
  #Busca si el comando ya está en lsList
  if(args[0] in list):
    args[0] = correct
    execute(args)
  else:
    #Si no está, le pregunta al usuario wdym y lo guarda (o no)
    answer = input("Command {} not found\nDid you mean '{}'[y/n]: ".format(args[0],correct))
    answer = answer.lower()
    if(answer[0] == 'y'):
      list.append(args[0])
      #for tries in list:
      #  print(tries)
      args[0] = correct
      execute(args)
    elif(answer[0] == 'n'):
      print("Ok then!")
    else:
      print("I'll take that as a NO...")
    return list
#------------------------------------------

def main():
  lsList = []
  dfList = []
  pingList = []
  alive = True
  while alive:
    command = input("PySHELL> ")
    #print("The command is '{}'".format(command))
    if(re.match(r'^[eE][xX][iI][tT]$',command)):
      alive = False
    else:
      args = command.split()
      if(args[0] == "ls" or args[0] == "df" or args[0] == "ping"):
        execute(args)
      else:
        if(re.match(r'^[jklñ{][asdf]$',args[0])):
          #evaluar ls
          analyze(args,"ls",lsList)
        elif(re.match(r'^[asdfg][sdfgh]$',args[0])):
          #evaluar df
          analyze(args,"df",dfList)
        elif(re.match(r'^[iop][yuiop][vbnm,][dfghj]$', args[0])):
          #evaluar ping
          analyze(args,"ping",pingList)
        else:
          print("We really don't know what you mean... :s")
#-----------------------------------------    
    
if '__main__' == __name__:
  main()