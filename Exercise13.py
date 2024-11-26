import sqlite3
import matplotlib.pyplot as plt

# Create a database named population_[your initials]
DB_NAME = 'population_OF.db'
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Create a table named population
cursor.execute('''
CREATE TABLE IF NOT EXISTS population (
    city TEXT,
    year INTEGER,
    population INTEGER
)
''')

# Define cities in Florida and their populations for the year 2023
cities = [
    ("Miami", 467963),
    ("Orlando", 307573),
    ("Tampa", 396700),
    ("Jacksonville", 911507),
    ("St. Petersburg", 265098),
    ("Hialeah", 233000),
    ("Fort Lauderdale", 183109),
    ("Port St. Lucie", 217527),
    ("Cape Coral", 202231),
    ("Gainesville", 133857)
]

# Insert initial population data for the year 2023
year = 2023
for city, population in cities:
    cursor.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)", (city, year, population))

conn.commit()

def simulate_population_growth(city, year, growth_rate=0.02, years=20):
    cursor.execute("SELECT population FROM population WHERE city=? AND year=?", (city, year))
    current_population = cursor.fetchone()

    if not current_population:
        print(f"No data found for {city}.")
        return [], []

    current_population = current_population[0]
    population_data = []
    years_list = []

    for year_offset in range(1, years + 1):
        current_population *= (1 + growth_rate)
        population_data.append(int(current_population))
        years_list.append(year + year_offset)

        # Insert the new population data into the table
        cursor.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
                       (city, year + year_offset, int(current_population)))

    conn.commit()
    return years_list, population_data

def plot_population_growth(years, population, city):
    plt.figure(figsize=(10, 5))
    plt.plot(years, population, marker='o')
    plt.title(f'Population Growth in {city}')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    plt.xticks(years)
    plt.show()

def main():
    year = 2023
    while True:
        print("\nChoose a city to view population growth:")
        for idx, (city, _) in enumerate(cities):
            print(f"{idx + 1}. {city}")

        choice = input("Enter the number of the city or 'q' to quit: ")

        if choice.lower() == 'q':
            break

        if choice.isdigit() and 1 <= int(choice) <= len(cities):
            city = cities[int(choice) - 1][0]
            years, population = simulate_population_growth(city, year)
            plot_population_growth(years, population, city)
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
    conn.close()
