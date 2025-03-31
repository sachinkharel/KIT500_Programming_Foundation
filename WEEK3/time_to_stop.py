"""
3.3PP Functions: Time Required to Stop
"""

__author__ = "Sachin Kharel"


def calculate_time_to_stop(mass:float, velocity: float, braking_force: float) -> (float):
    """Calculates and returns the time required to stop by using the mass, velocity and braking force input"""
    time_to_stop = (mass*velocity)/braking_force #formula for time to stop
    
    return time_to_stop
    

def main():
    
    mass1:float = 1500 #mass of vehicle 1
    velocity1:float = 25 #initial velocity of vehicle 1
    braking_force1:float = 6000 #braking force of vehicle 1
    
    mass2:float = 1000 #mass of vehicle 2
    velocity2:float = 15 #initial velocity of vehicle 2
    braking_force2:float = 4000 #braking force of vehicle 2
    
    #displaying the time required to stop for both vehicles
    print("Time Required to Stop")
    
    print()
    
    print(f"Time to Stop 1: {calculate_time_to_stop(mass1,velocity1,braking_force1):.2f} seconds")
    print(f"Time to Stop 2: {calculate_time_to_stop(mass2,velocity2,braking_force2):.2f} seconds")
    
    print()
    
    mass = float(input("Input vehicle mass (kg): ")) #taking input for mass
    velocity = float(input("Input initial velocity (m/s): ")) #taking input for initial velocity
    braking_force = float(input("Input braking force (N): ")) #taking input for braking force
    
    print()
    print("Calculating...")
    
    #displaying the time required to stop for the vehicle using the input values
    print(f"Time to Stop: {calculate_time_to_stop(mass,velocity,braking_force):.2f} seconds")
    
    
if __name__ == "__main__":
    main()