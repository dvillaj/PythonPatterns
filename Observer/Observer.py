import abc

class Observer(abc.ABC):

    @abc.abstractmethod
    def update(self, observable, args = None):
        pass


class Observable():
    def __init__(self):
        self.observers = []

    def registerObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        index = self.observers.index(observer)
        if (index >= 0):
            del self.observers[index]

    def notifyObservers(self, args = None):
        for observer in self.observers:
            observer.update(**args)


class DisplayElement(abc.ABC):

    @abc.abstractmethod
    def display(self):
        pass


class WeatherData(Observable):

    def __init__(self):
        self.observers = []

    def registerObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        index = self.observers.index(observer)
        if (index >= 0):
            del self.observers[index]

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()

    def getTemperature(self):
        return self.temperature

    def getHumidity(self):
        return self.humidity

    def getPressure(self):
        return self.pressure



class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, weatherData):
        self.weatherData = weatherData
        weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()


    def display(self):
        print(f"Current conditions: {self.temperature} F degrees and {self.humidity}% humidity")



class ForecastDisplay(Observer, DisplayElement):

    def __init__(self, weatherData):
        self.weatherData = weatherData
        self.currentPressure = 29.92
        weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.lastPressure = self.currentPressure
        self.pressure = pressure
        self.display()

    def display(self):
        print("Forecast")
        if (self.currentPressure > self.lastPressure):
            print("Improving weather on the way!")
        elif (self.currentPressure == self.lastPressure):
            print("More of the same!")
        else:
            print("Watch out for cooler, rainy weather")


class HeatIndexDisplay(Observer, DisplayElement):
    def __init__(self, weatherData):
        self.weatherData = weatherData
        self.heatIndex = 0.0
        weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.heatIndex = self.compute(temperature, humidity)
        self.display()

    def display(self):
        print(f"Heat index is {self.heatIndex}")

    def compute(self, t, rh):
        return ((16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh)
            + (0.00941695 * (t * t))
            + (0.00728898 * (rh * rh))
            + (0.000345372 * (t * t * rh))
            - (0.000814971 * (t * rh * rh))
            + (0.0000102102 * (t * t * rh * rh))
            - (0.000038646 * (t * t * t))
            + (0.0000291583 * (rh * rh * rh))
            + (0.00000142721 * (t * t * t * rh))
            + (0.000000197483 * (t * rh * rh * rh))
            - (0.0000000218429 * (t * t * t * rh * rh))
            + (0.000000000843296 * (t * t * rh * rh * rh)))
            - (0.0000000000481975 * (t * t * t * rh * rh * rh)))


class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weatherData):
        self.weatherData = weatherData
        self.maxTemp = 0.0
        self.minTemp = 200.0
        self.tempSum = 0.0
        self.numReadings = 0
        weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.tempSum += temperature
        self.numReadings += 1

        if (temperature > self.maxTemp):
            self.maxTemp = temperature

        if (temperature < self.minTemp):
            self.minTemp = temperature

        self.display()


    def display(self):
        print(f"Avg/Max/Min temperature = {(self.tempSum / self.numReadings)}/{self.maxTemp}/{self.minTemp}")



if __name__ == "__main__":
    weatherData = WeatherData();

    currentDisplay = CurrentConditionsDisplay(weatherData)
    statisticsDisplay = StatisticsDisplay(weatherData)
    forecastDisplay = ForecastDisplay(weatherData)
    heatIndexDisplay = HeatIndexDisplay(weatherData)

    weatherData.setMeasurements(80, 65, 30.4)
    weatherData.setMeasurements(82, 70, 29.2)
    weatherData.setMeasurements(78, 90, 29.2)