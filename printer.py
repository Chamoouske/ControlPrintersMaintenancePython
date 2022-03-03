class Printer:
    def __init__(self, mac, model, sector, maintenance):
        self.mac = mac
        self.model = model
        self.sector = sector
        self.maintenance = maintenance

    def add_maintenance(self, date, reason):
        self.maintenance[date] = reason