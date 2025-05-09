import json

class Producer:
    def __init__(self, machine_name=None):
        if machine_name:
            print(f'Importing Info for {machine_name}')
            self.name = machine_name
            if self.import_information():
                return
            
        
        print('Using Default Info')
        self.name = input('Machine Name: ') if not machine_name else machine_name
        self.energy_consumption = int(input('Energy Consumption: '))
        self.crafting_speed = {
            "Normal": float(input('Normal Crafting Speed: ')),
            "Uncommon": float(input('Uncommon Crafting Speed: ')),
            "Rare": float(input('Rare Crafting Speed: ')),
            "Epic": float(input('Epic Crafting Speed: ')),
            "Legendary": float(input('Legendary Crafting Speed: '))
        }
        self.module_slots = int(input('Number of Module Slots: '))
        self.energy_consumption_type = "Electrical" if self.name != "Biochamber" else "Nutrients"
        print('Updating dataset for future executions')
        self.export_information()
    
    def import_information(self):
        found = False
        with open('./Data/producers.json', 'r') as fin:
            for producer in (dataset := json.loads(fin.read())):
                if producer != self.name:
                    continue
                found = True
                self.energy_consumption = dataset[producer]['Energy Consumption']
                self.crafting_speed = dataset[producer]['Crafting Speed']
                self.module_slots = dataset[producer]['Module Slots']
                print(f'Data for {self.name} has been imported')
                return True
        print(f'{self.name} not found in records')
        return False
        

    def export_information(self):        
        export_json = {
            "Crafting Speed": self.crafting_speed,
            "Module Slots": self.module_slots,
            "Energy Consumption": self.energy_consumption
        }

        with open('./Data/producers.json', 'r') as fin:
            all_producers = json.loads(fin.read())

        all_producers[self.name] = export_json
    
        with open('./Data/producers.json', 'w') as fout:
            fout.write(json.dumps(all_producers, indent=4))