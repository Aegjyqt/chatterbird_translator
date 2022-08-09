from datasheet import Datasheet


class Database:
    """Governs tha making of a database from specific sheets + holds specific info on sheets"""

    def __init__(self, workbook_path: str, datasheets_list: list) -> None:
        """Creates essential parameters and instance-specific attributes for use in UserInput"""
        self.workbook_path = workbook_path
        self.datasheets_list = datasheets_list
        self._all_datasheet_instances = []
        self._entire_database_dict = {}

    def make_database(self) -> None:
        """Creates a database from sheets specified and fills its instance-specific attributes for use in UserInput"""
        for sheet in self.datasheets_list:
            new_datasheet = Datasheet(workbook_path=self.workbook_path, this_sheet_name=sheet)
            new_datasheet.fill_datasheet_dict()
            self._entire_database_dict.update(new_datasheet.access_datasheet_dict())
            self._all_datasheet_instances.append(new_datasheet)

    def get_all_database_instances(self) -> list:
        return self._all_datasheet_instances

    def get_entire_database_dict(self) -> dict:
        return self._entire_database_dict


datasheets = ['управление', 'факультет']
chatterbird_database = Database(workbook_path='lists_for_chatterbird.xlsx', datasheets_list=datasheets)
chatterbird_database.make_database()
