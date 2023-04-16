from abc import ABC , abstractmethod
class Car:
    def __init__(self,Cost:int,Model,Color,NumberOfDoors:int,CompanyName,ZeroToHundredSpeed:int,EngineType,HeaterSystem):
        self.Cost = Cost
        self.Model = Model
        self.Color = Color
        self.NumberOfDoors = NumberOfDoors
        self.CompanyName = CompanyName
        self.ZeroToHundredSpeed = ZeroToHundredSpeed
        self.EngineType
        self.HeaterSystem
    @abstractmethod
    def Move(self,Model):
        raise ValueError("You don't define this method for your car")
    @abstractmethod
    def Braking(self,Model):
        raise ValueError("You don't define this method for your car")
    @abstractmethod
    def Honking(self,Model):
        raise ValueError("You don't define this method for your car")
    def NumberOfSeats(self,NumberOfDoors,Model):
        if int(self.NumberOfDoors) == 2:
            print(f"2 people can seat on {self.Model} ")
        else:
            print(f"4 people can seat on {self.Model} ")
    def ServiceSystem(self,Model,CompanyName):
        print(f"{self.Model} is produced by {self.CompanyName}. if your car have any problem, call the {self.CompanyName} company")
#############################################################################################################1
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
########################################################################################################2
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
#########################################################################################################3
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
######################################################################################4
class ElectricEngine(Engine):
    def __init__(self, NumberOfCylinder, CylinderType, PistonMaterial, CylinderVolume, PowerToWeightRatio,AmountOfConsumedKWatt : int):
        super().__init__(NumberOfCylinder, CylinderType, PistonMaterial, CylinderVolume, PowerToWeightRatio)
        self.AmountOfConsumedkWatt = AmountOfConsumedKWatt
    def TypeGuess(self,AmountOfConsumedKWatt):
        if AmountOfConsumedKWatt > 75 :
            print("wow I guess you have a very modern and expensive car")
        else:
            print("Your car is modern,but hoenstly i don't think it's not expensive")
#################################################################################################5
class HybridEngine(PetrolEngine,ElectricEngine):
    def __init__(self, NumberOfCylinder, CylinderType, PistonMaterial, CylinderVolume, PowerToWeightRatio, CoolingSystem,AmountOfConsumedKWatt):
        super(PetrolEngine, ElectricEngine).__init__(NumberOfCylinder, CylinderType, PistonMaterial, CylinderVolume, PowerToWeightRatio, CoolingSystem,AmountOfConsumedKWatt)
    def EngineIntrestingsFacts(self):
        print("This engine is made to decrease the greenhouse gases effect on global warming /n Today some bikes are using something like these engines")
##############################################################################################6
class HeaterSystem:
    def __init__(self,HeaterOrCooler,OnOrOff,Degree : int,Time :int ,AutoMode):
        self.HeaterOrCooler = HeaterOrCooler
        self.OnOrOff = OnOrOff
        self.Degree = Degree
        self.Time = Time
        self.AutoMode = AutoMode
    def TurnOn(self,OnOrOff):
        if self.OnOrOff == "on" :
            print("Turn On the HeaterSystem")
        else:
            pass
    def TurnOff(self,OnOrOff):
         if self.OnOrOff == "off" :
            print("Turn Off the HeaterSystem")
    def HeaterOrCooler(self,HeaterOrCooler):
        if self.HeaterOrCooler == "Heater":
            print("Your car will be warmer soon")
        else:
            print("Your car will be cooler soon")
    def Degree(self,Degree):
        if self.Degree == 1:
            print("your heater system is  on first(lowwest) degree")
        elif self.Degree == 2:
            print("your heater system is  on second(moddest) degree")
        else:
            print("your heater system is  on highest degree")
    def AutoOff(self,Time):
        print(f"your heaterSystem will off in {self.Time} minuts ")
#######################################################7
class Pride(Car):
    def __init__(self, Cost, Model, Color, NumberOfDoors, CompanyName, ZeroToHundredSpeed, EngineType, HeaterSystem) :
        super().__init__(Cost,Model,Color,ZeroToHundredSpeed,HeaterSystem)        
        self.NumberOfDoors = 4
        self.CompanyName = "Saipa"
        self.EngineType = PetrolEngine(4, "m13", "Aluminium", 400, 8, "AirCooled")
    def Move(self,Model):
        print(f"pride({self.Model}) is moving")
    def Braking(self, Model):
        print(f"pride ({self.model}) is stopping")
    def Honking(self, Model):
        print(f"pride ({self.Model}) is honking . please move")
##############################################8
class Persia(Car):
    def __init__(self, Cost, Model, Color, NumberOfDoors, CompanyName, ZeroToHundredSpeed, EngineType, HeaterSystem):
        super().__init__(Cost,Model,Color,ZeroToHundredSpeed,HeaterSystem)
        self.NumberOfDoors = 4
        self.CompanyName = "IranKhodro"
        self.EngineType = PetrolEngine(4, "ELX", "Aluminium", 400, 7.6, "AirCooled")
    def Move(self,Model):
        print(f"Persia({self.Model}) is moving")
    def Braking(self, Model):
        print(f"Persia ({self.model}) is stopping")
    def Honking(self, Model):
        print(f"Persia ({self.Model}) is honking . please move")      
#######################################################9
class Peugeot(Car):
    def __init__(self, Cost, Model, Color, NumberOfDoors, CompanyName, ZeroToHundredSpeed, EngineType, HeaterSystem):
        super().__init__(Cost,Model,Color,CompanyName,ZeroToHundredSpeed,EngineType,HeaterSystem)
    def Move(self,Model):
        print(f"Peugeot({self.Model}) is moving")
    def Braking(self, Model):
        print(f"Peugeot ({self.model}) is stopping")
    def Honking(self, Model):
        print(f"Peugeot ({self.Model}) is honking . please move")
###################################################10
class sls(Car):
    def __init__(self, Cost, Model, Color, NumberOfDoors, CompanyName, ZeroToHundredSpeed, EngineType, HeaterSystem):
        super().__init__(Cost,Model,Color,ZeroToHundredSpeed,HeaterSystem)
        self.NumberOfDoors = 2
        self.ComopanyName = "Benz"
        self.EngineType = PetrolEngine(8, "M159 V8", "Aluminium", 1300, 4, "WaterCooled")
#################################################11
        
        


        
            

                        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        