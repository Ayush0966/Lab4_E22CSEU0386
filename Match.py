class FlightTable:
    def __init__(self):
        self.data = [
            {"Location": "Mumbai", "Team 01": "India", "Team 02": "Sri Lanka", "Timing": "DAY"},
            {"Location": "Delhi", "Team 01": "England", "Team 02": "Australia", "Timing": "DAY-NIGHT"},
            {"Location": "Chennai", "Team 01": "India", "Team 02": "South Africa", "Timing": "DAY"},
            {"Location": "Indore", "Team 01": "England", "Team 02": "Sri Lanka", "Timing": "DAY-NIGHT"},
            {"Location": "Mohali", "Team 01": "Australia", "Team 02": "South Africa", "Timing": "DAY-NIGHT"},
            {"Location": "Delhi", "Team 01": "India", "Team 02": "Australia", "Timing": "DAY"}
        ]

    def MatchesByTeam(self, TeamName):
        matches = []
        for match in self.data:
            if match["Team 01"] == TeamName or match["Team 02"] == TeamName:
                matches.append(match)
        return matches

    def MatchesByLoaction(self, location):
        matches = []
        for match in self.data:
            if match["Location"] == location:
                matches.append(match)
        return matches

    def MatchesByTimming(self, timing):
        matches = []
        for match in self.data:
            if match["Timing"] == timing:
                matches.append(match)
        return matches

def main():
    flight_table = FlightTable()

    while True:
        print("Choose a search parameter:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            TeamName = input("Enter the team name: ")
            matches = flight_table.MatchesByTeam(TeamName)
            if matches:
                print("Matches involving", TeamName)
                for match in matches:
                    print(match)
            else:
                print("No matches found for", TeamName)

        elif choice == "2":
            location = input("Enter the location: ")
            matches = flight_table.MatchesByLoaction(location)
            if matches:
                print("Matches in", location)
                for match in matches:
                    print(match)
            else:
                print("No matches found in", location)

        elif choice == "3":
            timing = input("Enter the timing: ")
            matches = flight_table.MatchesByTimming(timing)
            if matches:
                print("Matches with timing", timing)
                for match in matches:
                    print(match)
            else:
                print("No matches found with timing", timing)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
