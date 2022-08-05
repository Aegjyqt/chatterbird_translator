import database


class UserInput:
    """Governs user input"""

    def __init__(self) -> None:
        pass

    def get_simplified_string(self, string_for_processing: str) -> str:
        """changes text format to lowercase, gets rid of quotation marks"""
        return string_for_processing.lower().replace("\"", "")

    def get_string_with_nominative_identifier(self, user_input: str) -> str:
        """changes category-specific identifier words to the nominative case"""
        user_input_elements = user_input.split(' ')
        for category in database.chatterbird_database.get_all_database_instances():
            category_ids_list = category.get_ids()
            for word in user_input_elements:
                if word in category_ids_list:
                    user_input_elements[user_input_elements.index(word)] = category.get_ids()[0]  # переписать!!!
        return ' '.join(user_input_elements)

    def get_translation(self, user_input: str) -> str:
        """translates a string processed with the two of the above """
        pre_processed_str = self.get_string_with_nominative_identifier(user_input)
        if pre_processed_str in database.chatterbird_database.get_entire_database_dict():
            return database.chatterbird_database.get_entire_database_dict()[pre_processed_str]
