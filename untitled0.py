class car:
    def __init__(self,Cost:int,Name,Color,NumberOfDoors:int,CompanyName,ZeroToHundredSpeed:int):
        self.Cost = Cost
        self.Name = Name
        self.Color = Color
        self.NumberOfDoors = NumberOfDoors
        self.CompanyName = CompanyName
        self.ZeroToHundredSpeed = ZeroToHundredSpeed
    def Move(self,Name):
        print(f"{self.Name} is moving ")
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
    def EngineAllDescription(self):
        print(f"{self.Power}/n{self.EngineVolume}/n{self.Use}")
class 

            
        