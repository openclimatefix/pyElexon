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

class InsightsApiModelsResponsesDemandForecastDemandForecastWeekly(object):
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
        'publish_time': 'datetime',
        'transmission_system_demand': 'int',
        'national_demand': 'int',
        'forecast_week': 'int',
        'forecast_year': 'int',
        'week_start_date': 'date'
    }

    attribute_map = {
        'publish_time': 'publishTime',
        'transmission_system_demand': 'transmissionSystemDemand',
        'national_demand': 'nationalDemand',
        'forecast_week': 'forecastWeek',
        'forecast_year': 'forecastYear',
        'week_start_date': 'weekStartDate'
    }

    def __init__(self, publish_time=None, transmission_system_demand=None, national_demand=None, forecast_week=None, forecast_year=None, week_start_date=None):  # noqa: E501
        """InsightsApiModelsResponsesDemandForecastDemandForecastWeekly - a model defined in Swagger"""  # noqa: E501
        self._publish_time = None
        self._transmission_system_demand = None
        self._national_demand = None
        self._forecast_week = None
        self._forecast_year = None
        self._week_start_date = None
        self.discriminator = None
        if publish_time is not None:
            self.publish_time = publish_time
        if transmission_system_demand is not None:
            self.transmission_system_demand = transmission_system_demand
        if national_demand is not None:
            self.national_demand = national_demand
        if forecast_week is not None:
            self.forecast_week = forecast_week
        if forecast_year is not None:
            self.forecast_year = forecast_year
        if week_start_date is not None:
            self.week_start_date = week_start_date

    @property
    def publish_time(self):
        """Gets the publish_time of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.  # noqa: E501


        :return: The publish_time of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.


        :param publish_time: The publish_time of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.  # noqa: E501
        :type: datetime
        """

        self._publish_time = publish_time

    @property
    def transmission_system_demand(self):
        """Gets the transmission_system_demand of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.  # noqa: E501


        :return: The transmission_system_demand of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.  # noqa: E501
        :rtype: int
        """
        return self._transmission_system_demand

    @transmission_system_demand.setter
    def transmission_system_demand(self, transmission_system_demand):
        """Sets the transmission_system_demand of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.


        :param transmission_system_demand: The transmission_system_demand of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.  # noqa: E501
        :type: int
        """

        self._transmission_system_demand = transmission_system_demand

    @property
    def national_demand(self):
        """Gets the national_demand of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.  # noqa: E501


        :return: The national_demand of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.  # noqa: E501
        :rtype: int
        """
        return self._national_demand

    @national_demand.setter
    def national_demand(self, national_demand):
        """Sets the national_demand of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.


        :param national_demand: The national_demand of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.  # noqa: E501
        :type: int
        """

        self._national_demand = national_demand

    @property
    def forecast_week(self):
        """Gets the forecast_week of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.  # noqa: E501


        :return: The forecast_week of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.  # noqa: E501
        :rtype: int
        """
        return self._forecast_week

    @forecast_week.setter
    def forecast_week(self, forecast_week):
        """Sets the forecast_week of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.


        :param forecast_week: The forecast_week of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.  # noqa: E501
        :type: int
        """

        self._forecast_week = forecast_week

    @property
    def forecast_year(self):
        """Gets the forecast_year of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.  # noqa: E501


        :return: The forecast_year of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.  # noqa: E501
        :rtype: int
        """
        return self._forecast_year

    @forecast_year.setter
    def forecast_year(self, forecast_year):
        """Sets the forecast_year of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.


        :param forecast_year: The forecast_year of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.  # noqa: E501
        :type: int
        """

        self._forecast_year = forecast_year

    @property
    def week_start_date(self):
        """Gets the week_start_date of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.  # noqa: E501


        :return: The week_start_date of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.  # noqa: E501
        :rtype: date
        """
        return self._week_start_date

    @week_start_date.setter
    def week_start_date(self, week_start_date):
        """Sets the week_start_date of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.


        :param week_start_date: The week_start_date of this InsightsApiModelsResponsesDemandForecastDemandForecastWeekly.  # noqa: E501
        :type: date
        """

        self._week_start_date = week_start_date

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
        if issubclass(InsightsApiModelsResponsesDemandForecastDemandForecastWeekly, dict):
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
        if not isinstance(other, InsightsApiModelsResponsesDemandForecastDemandForecastWeekly):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other