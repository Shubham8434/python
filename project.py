olympic_record = []
country_details = []

def add_record():
    game_name = "High Jump"
    player_name = input("Enter the player name: ")
    year = input("Enter the year: ")
    player_gender = input("Enter the gender (Male/Female): ")
    location = input("Enter the location: ")

    gold_count = int(input("Enter the number of gold medals: "))
    silver_count = int(input("Enter the number of silver medals: "))
    bronze_count = int(input("Enter the number of bronze medals: "))

    record = {
        "game_name": game_name,
        "year": year,
        "player_name": player_name,
        "player_gender": player_gender,
        "location": location,
        "medal": {
            "gold": gold_count,
            "silver": silver_count,
            "bronze": bronze_count
        }
    }
    olympic_record.append(record)
    print("Record added successfully!\n")

def display_record(records):
    for record in records:
        print(f"Game: {record['game_name']}, Year: {record['year']}, Player: {record['player_name']}, Gender: {record['player_gender']}, Location: {record['location']}")
        print(f"Medals - Gold: {record['medal']['gold']}, Silver: {record['medal']['silver']}, Bronze: {record['medal']['bronze']}\n")

def get_records_year(year):
    return [record for record in olympic_record if record["year"] == year]

def get_record_player(player_name):
    return [record for record in olympic_record if record["player_name"].lower() == player_name.lower()]

def remove_record(records, player_name):
    original_length = len(records)
    records[:] = [record for record in records if record["player_name"].lower() != player_name.lower()]
    if len(records) < original_length:
        print(f"Records for {player_name} removed successfully!\n")
    else:
        print(f"No records found for {player_name}.\n")

def five_year_details():
    game_name = "High Jump"
    player_name = input("Enter the player name: ")
    year = int(input("Enter the year: "))
    country = input("Enter the country: ")

    record = {
        "game_name": game_name,
        "player_name": player_name,
        "year": year,
        "country": country,
    }

    country_details.append(record)
    print("Five-year details added successfully!\n")

def view_all_five_years():
    for detail in country_details:
        print(f"Game: {detail['game_name']}, Player: {detail['player_name']}, Year: {detail['year']}, Country: {detail['country']}\n")

def remove_five_year_details(player_name):
    original_length = len(country_details)
    country_details[:] = [detail for detail in country_details if detail["player_name"].lower() != player_name.lower()]
    if len(country_details) < original_length:
        print(f"Five-year details for {player_name} removed successfully!\n")
    else:
        print(f"No five-year details found for {player_name}.\n")

while True:
    print("Choose an option: ")
    print("1. Add a new record")
    print("2. Display all records")
    print("3. Search by year")
    print("4. Search by player name")
    print("5. Remove record by player name")
    print("6. Add five-year details")
    print("7. View all five-year details")
    print("8. Remove five-year details by player name")
    print("9. Exit")

    choice = int(input("Enter your choice (1-9): "))

    if choice == 1:
        add_record()
    elif choice == 2:
        display_record(olympic_record)
    elif choice == 3:
        year = input("Enter the year: ")
        records = get_records_year(year)
        if records:
            display_record(records)
        else:
            print("No records found for the given year.\n")
    elif choice == 4:
        name = input("Enter the player name: ")
        records = get_record_player(name)
        if records:
            display_record(records)
        else:
            print("No records found for the given player name.\n")
    elif choice == 5:
        name = input("Enter the player name to remove from records: ")
        remove_record(olympic_record, name)
    elif choice == 6:
        five_year_details()
    elif choice == 7:
        view_all_five_years()
    elif choice == 8:
        name = input("Enter the player name to remove from five-year details: ")
        remove_five_year_details(name)
    elif choice == 9:
        break
    else:
        print("Invalid choice! Please choose a valid option.\n")



# to share my python file to eveyone then you can send file with .exe file