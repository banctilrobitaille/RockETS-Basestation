import uuid

from dashboards.models import Dashboard, DashboardWidget, DashboardRow
from exceptions import InvalidDashboardParametersException


class DashboardFactory(object):
    @staticmethod
    def create_dashboard_from_query_params(query_params):
        dashboard = Dashboard()
        dashboard.name = query_params['name']
        dashboard.description = query_params['description']
        dashboard.template = query_params['template']
        dashboard.monitored_object_id = query_params['monitored-object-uuid']
        dashboard.transmitter_id = query_params['transmitter-uuid']
        dashboard.uuid = uuid.uuid4()
        for widget in DashboardFactory.__get_default_widgets_for(template=query_params['template']):
            dashboard.widgets.append(widget)

        return dashboard

    @staticmethod
    def __get_default_widgets_for(template):
        widgets = []

        if template == Dashboard.TEMPLATES['aircraft']:
            widgets.append(DashboardWidgetFactory.create_default_widget_from(
                    widget_type=DashboardWidget.TYPES['altimeter']))
            widgets.append(DashboardWidgetFactory.create_default_widget_from(
                    widget_type=DashboardWidget.TYPES['variometer']))
            widgets.append(DashboardWidgetFactory.create_default_widget_from(
                    widget_type=DashboardWidget.TYPES['heading']))
            widgets.append(DashboardWidgetFactory.create_default_widget_from(
                    widget_type=DashboardWidget.TYPES['airspeed']))

        return widgets


class DashboardWidgetFactory(object):
    DEFAULT_GAUGE_SIZE = 2
    DEFAULT_CHART_SIZE = 5
    DEFAULT_ALTITUDE_GAUGE_POSITION = 0
    DEFAULT_VERTICAL_SPEED_GAUGE_POSITION = 1
    DEFAULT_HEADING_INDICATOR_POSITION = 2
    DEFAULT_AIR_SPEED_GAUGE_POSITION = 3

    @staticmethod
    def create_default_widget_from(widget_type):
        widget = DashboardWidget()

        if widget_type is DashboardWidget.TYPES['variometer']:
            widget.name = "Vertical speed"
            widget.description = "The vertical speed gauge(variometer) inform of the rate of descent or climb"
            widget.measure_units = DashboardWidget.MEASURE_UNITS['feet_per_minute']
            widget.width = DashboardWidgetFactory.DEFAULT_GAUGE_SIZE
            widget.grid_position = DashboardWidgetFactory.DEFAULT_VERTICAL_SPEED_GAUGE_POSITION
            widget.type = DashboardWidget.TYPES['variometer']
            widget.category = DashboardWidget.CATEGORIES['gauge']
            widget.uuid = uuid.uuid4()
        elif widget_type is DashboardWidget.TYPES['airspeed']:
            widget.name = "Air speed"
            widget.description = "The airspeed indicator or airspeed gauge is an instrument used in an aircraft to " \
                                 "display the craft's airspeed, typically in knots"
            widget.measure_units = DashboardWidget.MEASURE_UNITS['knots']
            widget.width = DashboardWidgetFactory.DEFAULT_GAUGE_SIZE
            widget.grid_position = DashboardWidgetFactory.DEFAULT_AIR_SPEED_GAUGE_POSITION
            widget.type = DashboardWidget.TYPES['airspeed']
            widget.category = DashboardWidget.CATEGORIES['gauge']
            widget.uuid = uuid.uuid4()
        elif widget_type is DashboardWidget.TYPES['altimeter']:
            widget.name = "Altitude"
            widget.description = "An altimeter or an altitude meter is an instrument used to measure the altitude" \
                                 " of an object above a fixed level."
            widget.measure_units = DashboardWidget.MEASURE_UNITS['feet']
            widget.width = DashboardWidgetFactory.DEFAULT_GAUGE_SIZE
            widget.grid_position = DashboardWidgetFactory.DEFAULT_ALTITUDE_GAUGE_POSITION
            widget.type = DashboardWidget.TYPES['altimeter']
            widget.category = DashboardWidget.CATEGORIES['gauge']
            widget.uuid = uuid.uuid4()
        elif widget_type is DashboardWidget.TYPES['heading']:
            widget.name = "Heading"
            widget.description = "The heading indicator (also called an HI) is a flight instrument used in an" \
                                 " aircraft to inform the pilot of the aircraft's heading."
            widget.width = DashboardWidgetFactory.DEFAULT_GAUGE_SIZE
            widget.grid_position = DashboardWidgetFactory.DEFAULT_HEADING_INDICATOR_POSITION
            widget.type = DashboardWidget.TYPES['heading']
            widget.category = DashboardWidget.CATEGORIES['gauge']
            widget.uuid = uuid.uuid4()
        elif widget_type is DashboardWidget.TYPES['line-chart']:
            widget.name = "Chart"
            widget.description = "A line chart or line graph is a type of chart which displays information as a" \
                                 " series of data points called 'markers' connected by straight line segments."
            widget.width = DashboardWidgetFactory.DEFAULT_CHART_SIZE
            widget.type = DashboardWidget.TYPES['line-chart']
            widget.category = DashboardWidget.CATEGORIES['chart']
            widget.uuid = uuid.uuid4()
        else:
            raise InvalidDashboardParametersException("The provided dashboard widget type is invalid")

        return widget

    @staticmethod
    def create_widget_from_query_params(query_params):
        widget = DashboardWidget()

        widget.name = query_params['name']
        widget.description = query_params['description']
        widget.measure_units = DashboardWidget.MEASURE_UNITS[query_params['measure-units']]
        widget.width = int(query_params['width'])
        widget.grid_position = 0
        widget.type = query_params['type']
        widget.category = DashboardWidget.TYPES_TO_CATEGORY[query_params['type']]
        widget.uuid = uuid.uuid4()
        widget.sensor_id = query_params['sensor']
        widget.sensor_measure = query_params['sensor-measure']

        return widget


class DashboardRowsFactory(object):
    @staticmethod
    def create_dashboard_rows_from(widgets):
        dashboard_rows = []
        dashboard_row = DashboardRow()

        for widget in widgets:
            if dashboard_row.has_room_for(widget):
                dashboard_row.add_widget(widget)
            else:
                dashboard_rows.append(dashboard_row)
                dashboard_row = DashboardRow()
                dashboard_row.add_widget(widget)

        dashboard_rows.append(dashboard_row)
        return dashboard_rows
