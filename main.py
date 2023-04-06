# Task Nr.1:

# Create a class which takes temperature measurements in Kelvins and add static methods to transform those to 
# Celsius and Fahrenheit units. Use OOP abstraction.
from abc import abstractmethod, ABC

class ConvertTool(ABC):
    @abstractmethod
    def convert_to_celsius() -> float:
        pass
    
    @abstractmethod
    def convert_to_fahrenheit(self) -> float:
        pass

class Temperature(ConvertTool):

    @staticmethod
    def convert_to_celsius(kelvin_temp: float) -> float:
        return round(kelvin_temp - 273.15, 2)
    
    @staticmethod
    def convert_to_fahrenheit(kelvin_temp: float) -> float:
        return round(kelvin_temp * 1.8 - 459.67, 2)

kelvin_temp = 122
print(f"Kelvin {kelvin_temp} is {Temperature.convert_to_celsius(kelvin_temp)} C and {Temperature.convert_to_fahrenheit(kelvin_temp)} F")