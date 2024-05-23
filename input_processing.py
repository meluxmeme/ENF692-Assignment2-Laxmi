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

    def initialize(self):
        response = input(
        "Are changes detected in the vision input ?\nSelect 1 for light, 2 for pedestrian, 3 for vehicle, and 0 to end the program: ")
        if response in["1" , "2" , "3", "0"]:
            return response
        else:
            raise ValueError("Invalid input, The input must be either 0, 1, 2 or 3")



def print_message(sensor):

    if sensor.light=="red" or sensor.pedestrain == "yes"  or sensor.vehicle=="yes":
        print("\n \t\t STOP")
    elif sensor.light=="green" and sensor.pedestrain=="no" and sensor.vehicle=="no":
        print(" \n \t\t PROCEED")
    elif sensor.light=="yellow" and sensor.pedestrain=="no" and sensor.vehicle=="no":
        print("\n \t\t CAUTION")

    print("\nLight = " + str(sensor.light) + "  Pedestrian =  " + str(sensor.pedestrain) + "  Vehicle = " + str(sensor.vehicle) + "\n")


   



def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sensor = Sensor()

    while True:
        try:
           
            response = sensor.initialize()
            if response == "1":
                sensor.update_status_light()

            elif response == "2":
                sensor.update_status_pedest()

            elif response == "3":
                sensor.update_status_vehicle()

            elif response == "0":
                print("End")
                break
            #sensor.update()

        except ValueError as e: 
            print(e)
   
        print_message(sensor)



if __name__ == '__main__':
    main()

