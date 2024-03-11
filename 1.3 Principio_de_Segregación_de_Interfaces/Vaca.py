from Herbivoro import Herbivoro


class Vaca(Herbivoro):
  def comer(self):
      Herbivoro.comer(self)
      print("Vaca comiendo")
  def dormir(self):
      Herbivoro.dormir(self)
      print("Vaca durmiendo")
  def respirar(self):  
      Herbivoro.respirar(self)
      print("Vaca respirando")

