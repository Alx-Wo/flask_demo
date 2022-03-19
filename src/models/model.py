"""Model stub
"""
import logging
from pathlib import Path

import yaml

LOGGER = logging.getLogger("src.models.model")


class MyModel():
    """Model stub that can do predictions on input data
    """

    def __init__(self, parameters: Path):
        """Initialize a model with a given parameters.yaml file

        Args:
            parameters (Path): file to a parameters.yaml
        """
        self.default_parameters = {"offset": 3}
        self.parameters = self._parse_parameter_file(parameters)

    def _parse_parameter_file(self, param_file_path: Path) -> dict:
        if param_file_path.exists() and param_file_path.suffix == ".yaml":
            with open(param_file_path, "r", encoding="utf-8") as fid:
                try:
                    parameters = yaml.safe_load(fid)
                except yaml.YAMLError as exc:
                    LOGGER.error(exc)
                    LOGGER.info("Using default value for offset: 3")
                    parameters = self.default_parameters
        else:
            parameters = self.default_parameters
        return parameters

    def provide_prediction(self, model_input: str) -> str:
        """Run model prediction on the input

        Args:
            model_input (str): _description_

        Returns:
            str: _description_
        """
        prediction = self.predict(model_input)
        return f"Given {model_input}, I predict: {prediction}"

    def predict(self, model_input: str) -> str:
        """Make a prediction on an input, using the models parameters

        Args:
            input (str): _description_

        Returns:
            str: prediction
        """
        return str(len(model_input) - self.parameters["offset"])
