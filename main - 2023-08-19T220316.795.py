import datetime

class JournalingApp:
    def __init__(self):
        self.entries = {}
        self.entry_id_counter = 1

    def record_call(self, realtor_name, property_address, property_price):
        timestamp = datetime.datetime.now()
        entry_id = self.entry_id_counter
        self.entry_id_counter += 1

        entry = {
            "timestamp": timestamp,
            "realtor_name": realtor_name,
            "property_address": property_address,
            "property_price": property_price
        }

        self.entries[entry_id] = entry
        return entry_id

    def get_entry(self, entry_id):
        return self.entries.get(entry_id)

    def list_entries(self):
        for entry_id, entry in self.entries.items():
            print(f"Entry ID: {entry_id}")
            print(f"Timestamp: {entry['timestamp']}")
            print(f"Realtor Name: {entry['realtor_name']}")
            print(f"Property Address: {entry['property_address']}")
            print(f"Property Price: {entry['property_price']}\n")

# Create a JournalingApp instance
journal_app = JournalingApp()

# Record call entries
entry1_id = journal_app.record_call("John Doe", "123 Main St", 300000)
entry2_id = journal_app.record_call("Jane Smith", "456 Elm Ave", 250000)

# Display entries
print("Journal Entries:")
journal_app.list_entries()

# Retrieve specific entry
entry_id_to_retrieve = entry1_id
retrieved_entry = journal_app.get_entry(entry_id_to_retrieve)
if retrieved_entry:
    print(f"Retrieved Entry (ID {entry_id_to_retrieve}):")
    print(f"Timestamp: {retrieved_entry['timestamp']}")
    print(f"Realtor Name: {retrieved_entry['realtor_name']}")
    print(f"Property Address: {retrieved_entry['property_address']}")
    print(f"Property Price: {retrieved_entry['property_price']}")
else:
    print(f"Entry with ID {entry_id_to_retrieve} not found.")
