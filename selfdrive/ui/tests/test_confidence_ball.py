import pytest
from openpilot.system.ui.lib.application import gui_app
from openpilot.selfdrive.ui.onroad.augmented_road_view import AugmentedRoadView
from openpilot.selfdrive.ui.mici.onroad.confidence_ball import ConfidenceBall

def test_confidence_ball_added():
  # Initialize a headless/dummy raylib window so widget instantiation is safe
  gui_app.init_window("Test Window")
  try:
    arv = AugmentedRoadView()
    assert hasattr(arv, "_confidence_ball"), "AugmentedRoadView does not have _confidence_ball attribute"
    assert isinstance(arv._confidence_ball, ConfidenceBall), "_confidence_ball is not an instance of ConfidenceBall"
  finally:
    pass
