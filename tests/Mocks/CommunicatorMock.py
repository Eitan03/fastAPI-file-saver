from unittest.mock import Mock

from .DynamicObject import DynamicObject

def createCommunicatorMock(communicator: dict = {}):
		return DynamicObject({ **{
			'log': Mock(return_value=None)
		}, **communicator})