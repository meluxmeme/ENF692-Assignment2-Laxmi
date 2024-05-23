# input_processing.py
# Laxmi Paudel, ENSF 692 P24

class Sensor:

    def __init__(self):
        self.light ="green"
        self.pedestrain = "no"
        self.vehicle = "no"



    
    def update_status_light(self):
        light_update = input("Which light has chaned? Type red, green or yellow. : ")
        if light_update in ["green", "red", "yellow"]:
            self.light = light_update
            
        else:
            raise ValueError("Invalid light change")

 
    def update_status_pedest(self):
        ped_update = input("Is pedestrain detected ? Type yes or no: ")
        if ped_update in ["yes", "no"]:
            self.pedestrain = ped_update
           
        else:
            raise ValueError("Invalid pedestrian change")


    def update_status_vehicle(self):
        veh_update = input("Is vehicle detected ? Type yes or no: ")
        if veh_update in ["yes", "no"]:
           self.vehicle = veh_update
           
        
        else:
            raise ValueError("Invalid vehicle change")



def print_message(sensor):
    pass



def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

