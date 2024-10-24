{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8170dbdc",
   "metadata": {},
   "outputs": [],
   "source": [
    "olympic_records = []\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f6052865",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add_record():\n",
    "    game_name = input(\"Enter the game name: \")\n",
    "    year = int(input(\"Enter the year: \"))\n",
    "    player_name = input(\"Enter the player's name: \")\n",
    "    gender = input(\"Enter the gender (Male/Female): \")\n",
    "    event = input(\"Enter the event: \")\n",
    "    \n",
    "    gold_count = int(input(\"Enter the number of gold medals: \"))\n",
    "    silver_count = int(input(\"Enter the number of silver medals: \"))\n",
    "    bronze_count = int(input(\"Enter the number of bronze medals: \"))\n",
    "    \n",
    "    record = {\n",
    "        \"game_name\": game_name,\n",
    "        \"year\": year,\n",
    "        \"player_name\": player_name,\n",
    "        \"gender\": gender,\n",
    "        \"event\": event,\n",
    "        \"medals\": {\n",
    "            \"gold\": gold_count,\n",
    "            \"silver\": silver_count,\n",
    "            \"bronze\": bronze_count\n",
    "        }\n",
    "    }\n",
    "    olympic_records.append(record)\n",
    "    print(\"Record added successfully!\\n\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2c45c838",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add_records():\n",
    "    while True:\n",
    "        add_record()\n",
    "        continue_adding = input(\"Do you want to add another record? (yes/no): \").lower()\n",
    "        if continue_adding != \"yes\":\n",
    "            break\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "03184870",
   "metadata": {},
   "outputs": [],
   "source": [
    "def display_records(records):\n",
    "    for record in records:\n",
    "        print(f\"Game: {record['game_name']}, Year: {record['year']}, Player: {record['player_name']}, Gender: {record['gender']}\")\n",
    "        print(f\"Event: {record['event']}\")\n",
    "        print(f\"Medals - Gold: {record['medals']['gold']}, Silver: {record['medals']['silver']}, Bronze: {record['medals']['bronze']}\\n\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "79efdcbc",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_records_by_year(year):\n",
    "    return [record for record in olympic_records if record[\"year\"] == year]\n",
    "\n",
    "def get_records_by_player(player_name):\n",
    "    return [record for record in olympic_records if record[\"player_name\"].lower() == player_name.lower()]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1a7c5dcc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Choose an option:\n",
      "1. Add a new Olympic record\n",
      "2. Display all records\n",
      "3. Search records by year\n",
      "4. Search records by player\n",
      "5. Exit\n",
      "Enter your choice (1-5): 2\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'display_records' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 15\u001b[0m\n\u001b[0;32m     13\u001b[0m     add_records()\n\u001b[0;32m     14\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m choice \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m2\u001b[39m\u001b[38;5;124m'\u001b[39m:\n\u001b[1;32m---> 15\u001b[0m     display_records(olympic_records)\n\u001b[0;32m     16\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m choice \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m3\u001b[39m\u001b[38;5;124m'\u001b[39m:\n\u001b[0;32m     17\u001b[0m     year \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mint\u001b[39m(\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter the year to search: \u001b[39m\u001b[38;5;124m\"\u001b[39m))\n",
      "\u001b[1;31mNameError\u001b[0m: name 'display_records' is not defined"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    while True:\n",
    "        print(\"Choose an option:\")\n",
    "        print(\"1. Add a new Olympic record\")\n",
    "        print(\"2. Display all records\")\n",
    "        print(\"3. Search records by year\")\n",
    "        print(\"4. Search records by player\")\n",
    "        print(\"5. Exit\")\n",
    "        \n",
    "        choice = input(\"Enter your choice (1-5): \")\n",
    "        \n",
    "        if choice == '1':\n",
    "            add_records()\n",
    "        elif choice == '2':\n",
    "            display_records(olympic_records)\n",
    "        elif choice == '3':\n",
    "            year = int(input(\"Enter the year to search: \"))\n",
    "            records = get_records_by_year(year)\n",
    "            display_records(records)\n",
    "        elif choice == '4':\n",
    "            player_name = input(\"Enter the player's name to search: \")\n",
    "            records = get_records_by_player(player_name)\n",
    "            display_records(records)\n",
    "        elif choice == '5':\n",
    "            print(\"Exiting the program.\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"Invalid choice. Please try again.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f2100f9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
