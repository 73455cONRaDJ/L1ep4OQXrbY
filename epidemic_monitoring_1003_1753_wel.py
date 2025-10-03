# 代码生成时间: 2025-10-03 17:53:55
import numpy as np

"""
Epidemic Monitoring System using Python and NumPy.
This program simulates the spread of a contagious disease
and keeps track of the number of infected individuals over time.
"""

class EpidemicMonitor:
    def __init__(self, population_size, initial_infected_count, infection_rate):
        """
        Initializes the epidemic monitoring system.
        
        Args:
        population_size (int): Total size of the population.
        initial_infected_count (int): Number of initially infected individuals.
        infection_rate (float): Probability of infection per interaction.
        """
        self.population_size = population_size
        self.initial_infected_count = initial_infected_count
        self.infection_rate = infection_rate
        self.infected = np.zeros(population_size, dtype=int)
        self.infected[:initial_infected_count] = 1
        self.total_infected = 0

    def simulate_day(self):
        """
        Simulates a single day in the epidemic progression.
        Updates the infected array based on the infection rate.
        """
        new_infections = np.random.binomial(1, self.infection_rate, size=self.population_size - self.total_infected)
        new_infected = np.where(new_infections == 1)[0] + self.total_infected
        self.infected[new_infected] = 1
        self.total_infected += np.sum(new_infections)

    def get_infected_count(self):
        """
        Returns the current number of infected individuals.
        """
        return self.total_infected

    def run_simulation(self, days):
        """
        Runs the simulation for a specified number of days.
        
        Args:
        days (int): Number of days to simulate.
        
        Returns:
        np.ndarray: Array of infected counts for each day.
        """
        infected_counts = np.zeros(days, dtype=int)
        for day in range(days):
            self.simulate_day()
            infected_counts[day] = self.get_infected_count()
        return infected_counts

# Example usage:
if __name__ == "__main__":
    try:
        pop_size = 1000  # Population size
        initial_infected = 10  # Initially infected individuals
        infection_rate = 0.01  # Infection rate per interaction
        days_to_simulate = 30  # Days to simulate
        
        # Create an instance of the EpidemicMonitor
        monitor = EpidemicMonitor(pop_size, initial_infected, infection_rate)
        
        # Run the simulation
        infected_counts = monitor.run_simulation(days_to_simulate)
        print("Infected counts over time: ", infected_counts)
    except Exception as e:
        print("An error occurred: ", str(e))