import abc

# With Registration
 
class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text) or
                NotImplemented)



# Abstract Method Declaration only add these methods


#    @abc.abstractmethod
#     def load_data_source(self, path: str, file_name: str):
#         """Load in the data set"""
#         raise NotImplementedError

#     @abc.abstractmethod
#     def extract_text(self, full_file_path: str):
#         """Extract text from the data set"""
#         raise NotImplementedError


class PdfParserNew:
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass


@FormalParserInterface.register # <- retire if is Method Declaration 
class EmlParserNew:
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass







if __name__ == "__main__":

    print(issubclass(PdfParserNew, FormalParserInterface))
    print(issubclass(EmlParserNew, FormalParserInterface))
