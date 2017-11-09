# coding: utf-8

"""
    GraphHopper Directions API

    You use the GraphHopper Directions API to add route planning, navigation and route optimization to your software. E.g. the Routing API has turn instructions and elevation data and the Route Optimization API solves your logistic problems and supports various constraints like time window and capacity restrictions. Also it is possible to get all distances between all locations with our fast Matrix API.

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IsochroneResponsePolygon(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, properties=None, type=None, geometry=None):
        """
        IsochroneResponsePolygon - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'properties': 'IsochroneResponsePolygonProperties',
            'type': 'str',
            'geometry': 'IsochroneResponsePolygonGeometry'
        }

        self.attribute_map = {
            'properties': 'properties',
            'type': 'type',
            'geometry': 'geometry'
        }

        self._properties = properties
        self._type = type
        self._geometry = geometry

    @property
    def properties(self):
        """
        Gets the properties of this IsochroneResponsePolygon.

        :return: The properties of this IsochroneResponsePolygon.
        :rtype: IsochroneResponsePolygonProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this IsochroneResponsePolygon.

        :param properties: The properties of this IsochroneResponsePolygon.
        :type: IsochroneResponsePolygonProperties
        """

        self._properties = properties

    @property
    def type(self):
        """
        Gets the type of this IsochroneResponsePolygon.

        :return: The type of this IsochroneResponsePolygon.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this IsochroneResponsePolygon.

        :param type: The type of this IsochroneResponsePolygon.
        :type: str
        """

        self._type = type

    @property
    def geometry(self):
        """
        Gets the geometry of this IsochroneResponsePolygon.

        :return: The geometry of this IsochroneResponsePolygon.
        :rtype: IsochroneResponsePolygonGeometry
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """
        Sets the geometry of this IsochroneResponsePolygon.

        :param geometry: The geometry of this IsochroneResponsePolygon.
        :type: IsochroneResponsePolygonGeometry
        """

        self._geometry = geometry

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, IsochroneResponsePolygon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
