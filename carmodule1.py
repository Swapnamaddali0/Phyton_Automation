
#to write in .py file  - %% writefile.py
#%%writefile carCons.py
# dir  - List object attribute.
class CarApp:
    '''Car Application'''
    
    def __init__(self,name):
        '''Initialising CarApp Class '''
        self.name = name # object Variable
        print("Constructor Method:",name)
        
    def info(self): # self - Class reference arguement #cname is local variable
        '''car Information Method'''
        print("It's Audi Car:")
            
if __name__ == '__main__':
    AudiCar = CarApp("class Audi car")
    #dir(AudiCar)
    #help(AudiCar)
    #print(AudiCar.__doc__)
