import datetime

class ExerciseSession:
    def __init__(self, exercise=None, intensity=None, duration=None):
        if exercise is None:
            exercise = input("Exercise: ").title()
        if intensity is None:
            while True:
                try:
                    intensity = input("Intensity (Low, Medium, High): ").title()
                    if intensity not in ["Low", "L", "Medium", "M", "High", "H"]:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input: Please enter Low, Medium, or High")
        if duration is None:
            while True:
                try:
                    duration = int(input("How many minutes? "))
                    if duration <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input: Enter a positive integer")
        
        self.exercise = exercise
        if intensity in ["L", "Low"]:
            self.intensity = "Low"
        elif intensity in ["M", "Medium"]:
            self.intensity = "Medium"
        elif intensity in ["H", "High"]:
            self.intensity = "High"
        self.duration = duration

    def get_exercise(self):
        return self.exercise
    
    def get_intensity(self):
        return f"{self.intensity} intensity"
    
    def get_duration(self):
        return f"{self.duration} minutes"
    
    def set_exercise(self, exercise_name):
        self.exercise = exercise_name
        
    def set_intensity(self, intensity_amount):
        if intensity_amount.title() in ["L", "Low"]:
            self.intensity = "Low"
        elif intensity_amount.title() in ["M", "Medium"]:
            self.intensity = "Medium"
        elif intensity_amount.title() in ["H", "High"]:
            self.intensity = "High"
    
    def set_duration(self, duration_amount):
        self.duration = duration_amount
    
    def calories_burned(self, calories=0):
        intensity = self.intensity.title()
        if intensity == "Low":
            calories = 4
        elif intensity == "Medium":
            calories = 8
        elif intensity == "High":
            calories = 12
        return f"Calories Burned: {calories * self.duration}"

    def log_to_file(self, filename="exercise_log.txt"):
        with open(filename, "a") as file:
            now = datetime.datetime.now()
            date_str = now.strftime('%b %d, %Y')
            file.write(f"Date: {date_str} Time: {now.strftime('%H:%M')}\n")
            file.write(f"Exercise: {self.exercise}\n")
            if self.intensity == "L":
                self.intensity = "Low"
            elif self.intensity == "M":
                self.intensity = "Medium"
            elif self.intensity == "H":
                self.intensity = "High"
            file.write(f"Intensity: {self.intensity}\n")
            file.write(f"Duration: {self.duration} minutes\n")
            file.write(f"{self.calories_burned()}\n")
            file.write("-" * 40 + "\n")
while True:
    new_exercise = ExerciseSession()
    print(new_exercise.calories_burned())

    new_exercise.log_to_file()
    
    answer = input("Again? (y/n) ").lower()
    if answer not in ["yes", "y"]:
        break
