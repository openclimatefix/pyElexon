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

class InsightsApiModelsResponsesGenerationAvailabilityWeekly(object):
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
        'dataset': 'str',
        'publish_time': 'datetime',
        'fuel_type': 'str',
        'ngc_bm_unit': 'str',
        'output_usable': 'int',
        'year': 'int',
        'calendar_week_number': 'int'
    }

    attribute_map = {
        'dataset': 'dataset',
        'publish_time': 'publishTime',
        'fuel_type': 'fuelType',
        'ngc_bm_unit': 'ngcBmUnit',
        'output_usable': 'outputUsable',
        'year': 'year',
        'calendar_week_number': 'calendarWeekNumber'
    }

    def __init__(self, dataset=None, publish_time=None, fuel_type=None, ngc_bm_unit=None, output_usable=None, year=None, calendar_week_number=None):  # noqa: E501
        """InsightsApiModelsResponsesGenerationAvailabilityWeekly - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._publish_time = None
        self._fuel_type = None
        self._ngc_bm_unit = None
        self._output_usable = None
        self._year = None
        self._calendar_week_number = None
        self.discriminator = None
        if dataset is not None:
            self.dataset = dataset
        if publish_time is not None:
            self.publish_time = publish_time
        if fuel_type is not None:
            self.fuel_type = fuel_type
        if ngc_bm_unit is not None:
            self.ngc_bm_unit = ngc_bm_unit
        if output_usable is not None:
            self.output_usable = output_usable
        if year is not None:
            self.year = year
        if calendar_week_number is not None:
            self.calendar_week_number = calendar_week_number

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.


        :param dataset: The dataset of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def publish_time(self):
        """Gets the publish_time of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501


        :return: The publish_time of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.


        :param publish_time: The publish_time of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501
        :type: datetime
        """

        self._publish_time = publish_time

    @property
    def fuel_type(self):
        """Gets the fuel_type of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501


        :return: The fuel_type of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501
        :rtype: str
        """
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel_type):
        """Sets the fuel_type of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.


        :param fuel_type: The fuel_type of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501
        :type: str
        """

        self._fuel_type = fuel_type

    @property
    def ngc_bm_unit(self):
        """Gets the ngc_bm_unit of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501


        :return: The ngc_bm_unit of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501
        :rtype: str
        """
        return self._ngc_bm_unit

    @ngc_bm_unit.setter
    def ngc_bm_unit(self, ngc_bm_unit):
        """Sets the ngc_bm_unit of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.


        :param ngc_bm_unit: The ngc_bm_unit of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501
        :type: str
        """

        self._ngc_bm_unit = ngc_bm_unit

    @property
    def output_usable(self):
        """Gets the output_usable of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501


        :return: The output_usable of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501
        :rtype: int
        """
        return self._output_usable

    @output_usable.setter
    def output_usable(self, output_usable):
        """Sets the output_usable of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.


        :param output_usable: The output_usable of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501
        :type: int
        """

        self._output_usable = output_usable

    @property
    def year(self):
        """Gets the year of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501


        :return: The year of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.


        :param year: The year of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def calendar_week_number(self):
        """Gets the calendar_week_number of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501


        :return: The calendar_week_number of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501
        :rtype: int
        """
        return self._calendar_week_number

    @calendar_week_number.setter
    def calendar_week_number(self, calendar_week_number):
        """Sets the calendar_week_number of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.


        :param calendar_week_number: The calendar_week_number of this InsightsApiModelsResponsesGenerationAvailabilityWeekly.  # noqa: E501
        :type: int
        """

        self._calendar_week_number = calendar_week_number

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
        if issubclass(InsightsApiModelsResponsesGenerationAvailabilityWeekly, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesGenerationAvailabilityWeekly):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other