from Carnivoro import Carnivoro


class Perro(Carnivoro):
  def comer(self):
      Carnivoro.comer(self)
      print("Perro comiendo")
  def dormir(self):
      Carnivoro.dormir(self)
      print("Perro durmiendo")
  def respirar(self):  
      Carnivoro.respirar(self)
      print("Perro respirando")
    
