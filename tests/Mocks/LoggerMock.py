from unittest.mock import Mock

from .DynamicObject import DynamicObject

def createLoggerMock(logger: dict = {}):
		return DynamicObject({ **{
			'log': Mock(return_value=None)
		}, **logger})