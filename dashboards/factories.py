import uuid

from dashboards.models import Dashboard


class DashboardFactory(object):
    @staticmethod
    def create_dashboard_from_query_params(query_params):
        dashboard = Dashboard()
        dashboard.name = query_params['name']
        dashboard.description = query_params['description']
        dashboard.type = query_params['template']
        dashboard.uuid = uuid.uuid4()

        return dashboard
