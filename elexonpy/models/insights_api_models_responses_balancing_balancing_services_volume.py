# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InsightsApiModelsResponsesBalancingBalancingServicesVolume(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'settlement_date': 'date',
        'settlement_period': 'int',
        'bm_unit_applicable_balancing_services_volume': 'float',
        'national_grid_bm_unit': 'str',
        'bm_unit': 'str',
        'time': 'datetime'
    }

    attribute_map = {
        'settlement_date': 'settlementDate',
        'settlement_period': 'settlementPeriod',
        'bm_unit_applicable_balancing_services_volume': 'bmUnitApplicableBalancingServicesVolume',
        'national_grid_bm_unit': 'nationalGridBmUnit',
        'bm_unit': 'bmUnit',
        'time': 'time'
    }

    def __init__(self, settlement_date=None, settlement_period=None, bm_unit_applicable_balancing_services_volume=None, national_grid_bm_unit=None, bm_unit=None, time=None):  # noqa: E501
        """InsightsApiModelsResponsesBalancingBalancingServicesVolume - a model defined in Swagger"""  # noqa: E501
        self._settlement_date = None
        self._settlement_period = None
        self._bm_unit_applicable_balancing_services_volume = None
        self._national_grid_bm_unit = None
        self._bm_unit = None
        self._time = None
        self.discriminator = None
        if settlement_date is not None:
            self.settlement_date = settlement_date
        if settlement_period is not None:
            self.settlement_period = settlement_period
        if bm_unit_applicable_balancing_services_volume is not None:
            self.bm_unit_applicable_balancing_services_volume = bm_unit_applicable_balancing_services_volume
        if national_grid_bm_unit is not None:
            self.national_grid_bm_unit = national_grid_bm_unit
        if bm_unit is not None:
            self.bm_unit = bm_unit
        if time is not None:
            self.time = time

    @property
    def settlement_date(self):
        """Gets the settlement_date of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.  # noqa: E501


        :return: The settlement_date of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.  # noqa: E501
        :rtype: date
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.


        :param settlement_date: The settlement_date of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.  # noqa: E501
        :type: date
        """

        self._settlement_date = settlement_date

    @property
    def settlement_period(self):
        """Gets the settlement_period of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.  # noqa: E501


        :return: The settlement_period of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.  # noqa: E501
        :rtype: int
        """
        return self._settlement_period

    @settlement_period.setter
    def settlement_period(self, settlement_period):
        """Sets the settlement_period of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.


        :param settlement_period: The settlement_period of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.  # noqa: E501
        :type: int
        """

        self._settlement_period = settlement_period

    @property
    def bm_unit_applicable_balancing_services_volume(self):
        """Gets the bm_unit_applicable_balancing_services_volume of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.  # noqa: E501


        :return: The bm_unit_applicable_balancing_services_volume of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.  # noqa: E501
        :rtype: float
        """
        return self._bm_unit_applicable_balancing_services_volume

    @bm_unit_applicable_balancing_services_volume.setter
    def bm_unit_applicable_balancing_services_volume(self, bm_unit_applicable_balancing_services_volume):
        """Sets the bm_unit_applicable_balancing_services_volume of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.


        :param bm_unit_applicable_balancing_services_volume: The bm_unit_applicable_balancing_services_volume of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.  # noqa: E501
        :type: float
        """

        self._bm_unit_applicable_balancing_services_volume = bm_unit_applicable_balancing_services_volume

    @property
    def national_grid_bm_unit(self):
        """Gets the national_grid_bm_unit of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.  # noqa: E501


        :return: The national_grid_bm_unit of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.  # noqa: E501
        :rtype: str
        """
        return self._national_grid_bm_unit

    @national_grid_bm_unit.setter
    def national_grid_bm_unit(self, national_grid_bm_unit):
        """Sets the national_grid_bm_unit of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.


        :param national_grid_bm_unit: The national_grid_bm_unit of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.  # noqa: E501
        :type: str
        """

        self._national_grid_bm_unit = national_grid_bm_unit

    @property
    def bm_unit(self):
        """Gets the bm_unit of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.  # noqa: E501


        :return: The bm_unit of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.  # noqa: E501
        :rtype: str
        """
        return self._bm_unit

    @bm_unit.setter
    def bm_unit(self, bm_unit):
        """Sets the bm_unit of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.


        :param bm_unit: The bm_unit of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.  # noqa: E501
        :type: str
        """

        self._bm_unit = bm_unit

    @property
    def time(self):
        """Gets the time of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.  # noqa: E501


        :return: The time of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.


        :param time: The time of this InsightsApiModelsResponsesBalancingBalancingServicesVolume.  # noqa: E501
        :type: datetime
        """

        self._time = time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InsightsApiModelsResponsesBalancingBalancingServicesVolume, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InsightsApiModelsResponsesBalancingBalancingServicesVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other