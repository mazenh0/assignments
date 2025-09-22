## COMP 1701
## MAZEN HAMID  
## THU NOV 7

import math

def calculate_hrv(interval1, interval2, interval3):
    """
    Calculates heart rate variability (HRV).
    Uses 3 heartbeat intervals and does math.
    """
    diff1 = interval1 - interval2
    diff2 = interval2 - interval3
    
    squared_diff1 = diff1 ** 2
    squared_diff2 = diff2 ** 2
    
    avg_squared_diff = (squared_diff1 + squared_diff2) / 2
    hrv = math.sqrt(avg_squared_diff)
    return hrv

def main():
    """
    Main function that checks if you're sick or stressed.
    Asks a bunch of questions and gives a diagnosis.
    """
    temperature = float(input("Enter your temperature (°C): "))
    o_u = input("Was the temperature measured Orally (O) or Underarm (U)? (enter O or U): ").strip().upper()
    
    if o_u == 'U':
        temperature += 0.5  # Adjust if underarm reading
    has_fever = temperature >= 37.5
    
    if has_fever:
        """
        If there's a fever, ask about nausea.
        If nauseous, probably flu; if not, probably infection.
        """
        nausea = input("Are you experiencing nausea? (enter y or n): ").strip().lower() == 'y'
        
        if nausea:
            diagnosis = "Flu"
        else:
            diagnosis = "Infection"
    else:
        """
        If no fever, check for stress signs.
        Ask for heartbeat intervals and cortisol level.
        """
        print("Please enter 3 heartbeat intervals in ms ")
        interval1 = float(input("Enter first interval: "))
        interval2 = float(input("Enter second interval: "))
        interval3 = float(input("Enter third interval: "))
        
        hrv = calculate_hrv(interval1, interval2, interval3)
        
        cortisol_levels = float(input("Enter cortisol level in mcg/dL: "))
        low_hrv = hrv < 50
        high_cortisol = cortisol_levels > 10
        
        if low_hrv and high_cortisol:
            diagnosis = "Stress"
        else:
            diagnosis = "Healthy"
    
    # Final output of diagnosis
    print(f"\nDiagnosis: {diagnosis}")


main()
