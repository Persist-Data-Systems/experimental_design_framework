import numpy as np
import json
import pandas as pd
from functools import reduce
from base import BaseDesign, MainPlot, SubPlot, SubSubPlot

class DemonstrationStrip(BaseDesign):
    """
    Builds a model of a demonstration strip design
    """

    def __init__(self, metadata: dict, treatments: list[str], treatmentDbIds: list[str], plotDbIds: list[str], germplasmDbIds: list[list[str]]) -> None:
        super().__init__()

        if type(treatments) != list or not all(isinstance(item, str) for item in treatments):
            raise ValueError(f"treatments should be a list of strings")
        elif type(treatmentDbIds) != list or not all(isinstance(item, str) for item in treatmentDbIds):
            raise ValueError(f"treatmentDbIds should be a list of strings")
        elif type(plotDbIds) != list or not all(isinstance(item, str) for item in plotDbIds):
            raise ValueError(f"plotDbIds should be a list of strings")
        elif type(germplasmDbIds) != list or not all(isinstance(item, list) for item in germplasmDbIds):
            raise ValueError(f"treatmentDbIds should be of type list[list[str]]")
        
        flattened_germpplasm = list(reduce(lambda x, y: x + y, germplasmDbIds, []))
        if not all(isinstance(item, str) for item in flattened_germpplasm):
            raise ValueError(f"treatmentDbIds should be of type list[list[str]]")


        self.design_parameters = {
            "design_plan": "demonstration_strip",
            "design_description": "This is the simplest experimental design consisting of a total of two to n singular treatments assigned to main plots. Demonstration strips are always un-replicated thus there are no more than 1 plot of a given treatment represented in the trial.",
            "num_replications": 1,
            "num_plots": len(treatments),
            "treatments": treatments
        }

        for k, v in metadata.items():
            self.metadata[k] = v

        self.treatments = treatments
        self.treatment_ids = treatmentDbIds
        self.plot_ids = plotDbIds
        self.germplasm_ids = germplasmDbIds

    def build(self):
        if not all(self.design_parameters['num_plots'] == len(i) for i in [self.treatments, self.treatment_ids, self.plot_ids, self.germplasm_ids]):
            raise ValueError(f"The lengths of treatments, treatment_ids, plot_ids, and germplasm_ids are not equal")
        
        self.design['plots'] = []

        for i in range(len(self.treatments)):                
            plot = MainPlot(plotDbId=self.plot_ids[i],
                            treatmentDbId=self.treatment_ids[i],
                            germplasmDbId=self.germplasm_ids[i])
            self.design['plots'].append(plot.out())
    


if __name__ == '__main__':
    base = BaseDesign()
    print(base.metadata)


    plot_ids = ['p1234', 'p2345', 'p345']
    treatment_ids = ['t1', 't34', 't56']
    germplasm_ids = ['A', 'B', 'C']
    germplasm_ids = [['A'], ['B'], ['C']]

    dstrip = DemonstrationStrip(
        metadata={
            "studyDbId": "<studyDbId>",
		    "trialDbId": "<trialDbId>",
		    "locationDbId": "<locationDbId>",
		    "active": True,
		    "date_created": "<yyyymmdd>",
		    "design_user": "userDbId"
        },
        treatments=['lo_N', 'med_N', 'hi_N'], 
        treatmentDbIds=treatment_ids,
        plotDbIds=plot_ids,
        germplasmDbIds=germplasm_ids
    )
    print(dstrip.metadata)
    print(dstrip.design_parameters)
    print(dstrip.design)
    dstrip.build()
    print(len(germplasm_ids))
    print(dstrip.design)