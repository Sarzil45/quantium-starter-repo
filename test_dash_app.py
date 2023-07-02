# Import the functions that we need to test
from dash_app import app


def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)


def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#line-chart", timeout=10)


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region", timeout=10)
