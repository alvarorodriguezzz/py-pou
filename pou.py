import random

class Pou:
  # inciciar
  def __init__(self, name):
    self.name = name
    self.age = random.randint(1,10)
    self.hunger = random.randint(4,10)
    self.energy = 0
    self.happiness = 0
    self.health = 0
    self.knowledge = 0
    self.dream =0
    self.alive = True

  def status(self):
    print("Name:", self.name)
    print("Age:", round(self.age, 2))
    print("Hunger:", self.hunger)
    print("Energy:", self.energy)
    print("Happiness:", self.happiness)
    print("Health:", self.health)
    print("Knowledge:", self.knowledge)
    print("Dream:", self.dream)
    if self.hunger >=10:
        print("Toto está hambriento!!")
    elif self.happiness >= 7:
        print("Toto está muy feliz :)")
    elif self.dream >=10:
        print("¡Tiene mucho sueño!")

  def __str__(self):
    return f"Name: {self.name}\nAge: {self.age}\nHunger: {self.hunger}\nEnergy: {self.energy}\nHappiness: {self.happiness}\nHealth: {self.health}\nKnowledge: {self.knowledge}\nDream: {self.dream}"

  def play(self):
    self.hunger += 2
    self.energy -= 1
    self.health += 0
    self.dream += 0
    if (self.energy <=0 ):
        self.happiness -= 2
    else:
        self.happiness +=3

  def eat(self):
    self.hunger -= 4
    self.energy += 1
    self.health += 1
    self.happiness += 1
    self.dream +=1
    
    
  def sleep(self):
    self.hunger += 3
    self.energy += 4
    self.health += 1
    self.happiness += 2
    self.dream -= 5
    
  def study(self):
      self.knowledge+=3
      self.energy-=5
      self.happiness-=2
      self.age += 0.2
      self.dream +=2

  # add more methods

toto = Pou("Toto")

while True:
  option = input("\n******************** MAIN Pou MENU  ******************** \n\nWhat do you want to do? (play, eat, sleep, study, exit): \n\n *****************************************************\n")
  

  if option == "play":
    toto.play()
    toto.status()
  # add more methods
  elif option =="eat":
      toto.eat()
      toto.status()
  elif option=="sleep":
      toto.sleep()
      toto.status()
  elif option =="study":
      toto.study()
      toto.status()
      
    
  else:
      print("El juego termino")
      break
