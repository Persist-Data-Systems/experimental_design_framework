import json
from abc import ABC, abstractmethod

class Plot():
    """
    Base stub class for a plot
    """
    def __init__(self, plotDbId: str):
        if type(plotDbId) != str:
            raise TypeError(f"plotDbId should be a string")
        self.plotDbId = plotDbId
    
    @abstractmethod
    def out(self):
        pass

class MainPlot(Plot):
    """
    Class for a main plot in an experiment
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

class SubPlot(MainPlot):
    """
    Class for a sub plot in an experiment. Must pass all of the arguments for MainPlot parent class plus the parent_plotDbId.
    """
    def __init__(self, plotDbId: str, treatmentDbId: str, germplasmDbId: list[str], parent_plot: MainPlot):
        super().__init__(plotDbId, treatmentDbId, germplasmDbId)

        if type(parent_plot) != MainPlot:
            raise TypeError(f"The parent_plot for a base.SubPlot class should be a base.MainPlot")
        
        
        self.parent_plotDbId = parent_plot.plotDbId

    def out(self):
        return {
            "plotDbId": self.plotDbId,
            "parent_plotDbId": self.parent_plotDbId,
            "treatmentDbId": self.treatmentDbId,
            "germplasmDbId": self.germplasmDbId
        }

class SubSubPlot(MainPlot):
    """
    
    """
    def __init__(self, plotDbId: str, treatmentDbId: str, germplasmDbId: list[str], parent_plot: SubPlot):
        super().__init__(plotDbId, treatmentDbId, germplasmDbId)

        if type(parent_plot) != SubPlot:
            raise TypeError(f"The parent_plot for a base.SubSubPlot class should be a base.SubPlot")
        
        self.parent_plotDbId = parent_plot.plotDbId

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
        


# basePlot = Plot("asfdsfds")
# print(basePlot.plotDbId)

# main_plot_1 = MainPlot("123", "nitrogen", ["HANNOVER", "VALE"])
# print(main_plot_1.germplasmDbId)


# sub_plot_1 = SubPlot("123", "asfdsfds", "nitrogen", ["HANNOVER", "VALE"])
# print(sub_plot_1.germplasmDbId)

# print(type(sub_plot_1))