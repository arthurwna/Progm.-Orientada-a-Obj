    

   # class Conta: 
  #      def __int__(self):
  #      self.saldo = 1000

  #      def saldo(self):
   #         return self.saldo      #permite ver o saldo

   # conta = Conta()
  #  print(conta.saldo)

  #  conta.saldo = 2000

  #  print(conta.saldo)


#------------

#por convenção [_nome]

   # class Conta: 
    #    def __int__(self):
    #    self._saldo = 1000


    #    def saldo(self):
    #        return self._saldo      #permite ver o saldo

  #  conta = Conta()
   # print(conta._saldo)

 #   conta._saldo = 2000   #isso é pribido por convenção

 #   print(conta._saldo)

#-----------------

   # class Conta:

     #   def __int__(self):
     #       self.__saldo = 42

  #  t = Conta()

  #  print(t._Conta__saldo)  # 42 (funciona)
 #   t._Conta__saldo = 100   # muda mesmo
 #   print(t._Conta__saldo)  # 100

    #isso da erro! (correto)
    #print(t.__saldo)       #AtributeError+ 'test' object has no atributte '__saldo'




#--------------


#nome + @property

 #class Conta: 
    #def __int__(self):
     #self.__saldo = 1000

     #@property
     #def saldo(self):
      #return self.__saldo      #permite ver o saldo

  #conta = Conta()
  #print(conta.saldo)

  #conta.__saldo = 2000   #isso é pribido por convenção

 # print(conta.saldo)

#-------------------

#from dataclasses import dataclass

@dataclass(frozen=true)
class Conta:
   saldo: float = 1000
    nome: str = "Maria"

conta = Conta()

print(conta.saldo)     #1000

isso da erro

conta.saldo = 5000       #frozenInstanceError
