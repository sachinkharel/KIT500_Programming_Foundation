"""
3.3PP Functions: Describe the option you chose here
"""

__author__ = "Sachin Kharel"

def distance(initial_velocity: float, time: float) -> (float):
    """Calculates and returns the stopping distance from the initial velocity and reaction time"""
    FRICTION = 0.7
    GRAVITY = 9.81
    stopping_distance = (initial_velocity*time)+(initial_velocity**2)/(2*FRICTION*GRAVITY) #calculated stopping distance
    
    return stopping_distance
    

def main():
    
    initial_velocity: float     #user given initial_velocity
    reaction_time:float         #user given reaction_time
    print("Stopping Distance")
    
    print()
    print(f"Stopping Distance 1: {distance(27.8,1.5):.2f} m")
    print(f"Stopping Distance 2: {distance(13.9,1.5):.2f} m")
    print()
    
    initial_velocity = float(input("Input initial velocity (m/s): ")) #car's initial velocity
    reaction_time = float(input("Input reaction time (seconds): ")) #car's reaction time

    print()
    print("Calculating...")
    print(f"Stopping Distance: {distance(initial_velocity,reaction_time):.2f} m")
   
    
if __name__ == "__main__":
    main()