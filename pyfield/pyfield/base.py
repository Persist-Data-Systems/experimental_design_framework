import json
from abc import ABC, abstractmethod

class Plot():
    """
    
    """
    def __init__(self, plotDbId: str):
        if type(plotDbId) != str:
            raise TypeError(f"plotDbId should be a string")
        self.plotDbId = plotDbId

class MainPlot(Plot):
    """
    
    """
    def __init__(self, plotDbId: str, treatmentDbId: str, germplasmDbId: list[str]):
        super().__init__(plotDbId)
        if type(treatmentDbId) != str:
            raise TypeError(f"treatmentDbId should be a string.")
        elif type(germplasmDbId) != list:
            raise TypeError(f"germplasmDbId should be a list of strings.")
        elif not all(isinstance(i, str) for i in germplasmDbId):
            raise TypeError(f"germplasmDbId should be a list of strings.")
        
        self.treatmentDbId = treatmentDbId
        self.germplasmDbId = germplasmDbId
    
    def out(self):
        return {
            "plotDbId": self.plotDbId,
            "treatmentDbId": self.treatmentDbId,
            "germplasmDbId": self.germplasmDbId
        }

class SubPlot(Plot):
    """
    
    """
    def __init__(self, plotDbId: str, parent_plotDbId: str, treatmentDbId: str, germplasmDbId: list[str]):
        super().__init__(plotDbId)
        if type(treatmentDbId) != str:
            raise TypeError(f"parent_plotDbId should be a string")
        if type(treatmentDbId) != str:
            raise TypeError(f"treatmentDbId should be a string.")
        elif type(germplasmDbId) != list:
            raise TypeError(f"germplasmDbId should be a list of strings.")
        elif not all(isinstance(i, str) for i in germplasmDbId):
            raise TypeError(f"germplasmDbId should be a list of strings.")
        
        self.parent_plotDbId = parent_plotDbId
        self.treatmentDbId = treatmentDbId
        self.germplasmDbId = germplasmDbId

    def out(self):
        return {
            "plotDbId": self.plotDbId,
            "parent_plotDbId": self.parent_plotDbId,
            "treatmentDbId": self.treatmentDbId,
            "germplasmDbId": self.germplasmDbId
        }

class SubSubPlot(Plot):
    """
    
    """
    def __init__(self, plotDbId: str, parent_plotDbId: str, treatmentDbId: str, germplasmDbId: list[str]):
        super().__init__(plotDbId)
        if type(treatmentDbId) != str:
            raise TypeError(f"parent_plotDbId should be a string")
        if type(treatmentDbId) != str:
            raise TypeError(f"treatmentDbId should be a string.")
        elif type(germplasmDbId) != list:
            raise TypeError(f"germplasmDbId should be a list of strings.")
        elif not all(isinstance(i, str) for i in germplasmDbId):
            raise TypeError(f"germplasmDbId should be a list of strings.")
        
        self.parent_plotDbId = parent_plotDbId
        self.treatmentDbId = treatmentDbId
        self.germplasmDbId = germplasmDbId

    def out(self):
        return {
            "plotDbId": self.plotDbId,
            "parent_plotDbId": self.parent_plotDbId,
            "treatmentDbId": self.treatmentDbId,
            "germplasmDbId": self.germplasmDbId
        }
class BaseDesign():
    """
    Base class for all field designs. Used for subclass methods
    """
    def __init__(self) -> None:
        self.metadata = {"version": "0.1.0"}
        self.design_parameters = {}
        self.design = {}
        self.fieldbook = None
        self.dataframe = None

    
    @abstractmethod
    def build(self):
        """
        Build the field design
        """
        


basePlot = Plot("asfdsfds")
print(basePlot.plotDbId)

main_plot_1 = MainPlot("123", "nitrogen", ["HANNOVER", "VALE"])
print(main_plot_1.germplasmDbId)


sub_plot_1 = SubPlot("123", "asfdsfds", "nitrogen", ["HANNOVER", "VALE"])
print(sub_plot_1.germplasmDbId)

print(type(sub_plot_1))