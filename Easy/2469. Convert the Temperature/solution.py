class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        ans = []
        KELVIN = celsius + 273.15
        FAHRENHEIT = celsius * 1.8 + 32
        ans.append(KELVIN)
        ans.append(FAHRENHEIT)
        
        return ans