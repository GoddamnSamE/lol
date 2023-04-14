class car:
    def __init__(self,Cost:int,Model,Color,NumberOfDoors:int,CompanyName,ZeroToHundredSpeed:int):
        self.Cost = Cost
        self.Model = Model
        self.Color = Color
        self.NumberOfDoors = NumberOfDoors
        self.CompanyName = CompanyName
        self.ZeroToHundredSpeed = ZeroToHundredSpeed
    def Move(self,Name):
        pass
    def Braking(self,Name):
        print(f"{self.Name} is stopping")
    def Honking(self,Name):
        print(f"{self.Name} is honking. please change your place")
    def NumberOfSeats(self,NumberOfDoors,Name):
        if int(self.NumberOfDoors) == 2:
            print(f"2 people can seat on {self.Name} ")
        else:
            print(f"4 people can seat on {self.Name} ")
    def ServiceSystem(self,Name,CompanyName):
        print(f"{self.Name} is produced by {self.CompanyName}. if your car have any problem, call the {self.CompanyName} company")
class Engine:
    def __init__(self,NumberOfCylinder : int ,CylinderType,PistonMaterial,CylinderVolume : int ,PowerToWeightRatio : int):
        self.NumberOfCylinder = NumberOfCylinder
        self.CylinderType = CylinderType
        self.PistonMaterial = PistonMaterial
        self.CylinderVolume = CylinderVolume
        self.PowerToWeightRatio = PowerToWeightRatio
    def EnginePower(self,NumberOfCylinder):
        if NumberOfCylinder < 6:
            print("This engine has low power")
        elif NumberOfCylinder == 6:
            print("This engine has normal power")
        else:
            print("This engine has high power")
    def EngineVolume(self,NumberOfCylinder,CylinderVolume):
        print(f"This engine's volume is{NumberOfCylinder*CylinderVolume}")
    def HeatTransfer(self,PistonMaterial):
        if self.PistonMaterial == "Aluminium":
            print("This engine has high heat transfer, but it's expensive")
        else :
            print("This engine has low heat transer, but it's cheap")
    def Use(self,PowerToWeightRatio):
        if self.PowerToWeightRatio > 6:
            print('This engine belongs to a normal car')
        else:
            print("This engine belongs to a race car ")
    def EngineTotalDescription(self):
        print(f"{self.Power}/n{self.EngineVolume}/n{self.Use}")
    def EngineIntrestingsFacts(self):
        pass
class PetrolEngine(Engine):
    def __init__(self, NumberOfCylinder, CylinderType, PistonMaterial, CylinderVolume, PowerToWeightRatio,CoolingSystem):
        super().__init__(NumberOfCylinder, CylinderType, PistonMaterial, CylinderVolume, PowerToWeightRatio)
        self.CoolingSystem = CoolingSystem
    def CoolingPower(self,CoolingSystem):
        if self.CoolingSystem in ("Air-cooled","AirCooled") :
            print("watch out.Your engine is old and has an old-fashioned cooling system")
        else:
            print("Your engine's cooling system is OK")
    def EngineIntrestingsFacts(self):
        print("This engine cosume petrol!!!")
        print("Your engine is first kind which used to make cars. /n this kind of engine has a real effect in increasing global warming")
class DieselEngine(Engine):
    def __init__(self, NumberOfCylinder, CylinderType, PistonMaterial, CylinderVolume, PowerToWeightRatio,NumberOfStrake : int):
        super().__init__(NumberOfCylinder, CylinderType, PistonMaterial, CylinderVolume, PowerToWeightRatio)
        self.NumberOfStrake = NumberOfStrake
    def InUse(self,NumberOfStrake):
        if NumberOfStrake == 2:
            print("NO one use this trash .change it quickly")
        else:
            print("Your engine is just ok, you can use it.")
    def EngineIntrestingsFacts(self):
        print("Your engine type can cnsume many things")
        print("This Engine is the most used engine in the world. /n most tanks in World War II use this kind of engine")
class ElectricEngine(Engine):
    def __init__(self, NumberOfCylinder, CylinderType, PistonMaterial, CylinderVolume, PowerToWeightRatio,AmountOfConsumedKWatt : int):
        super().__init__(NumberOfCylinder, CylinderType, PistonMaterial, CylinderVolume, PowerToWeightRatio)
        self.AmountOfConsumedkWatt = AmountOfConsumedKWatt
    def TypeGuess(self,AmountOfConsumedKWatt):
        if AmountOfConsumedKWatt > 75 :
            print("wow I guess you have a very modern and expensive car")
        else:
            print("Your car is modern,but hoenstly i don't think it's not expensive")
class Hybrid(car):
    