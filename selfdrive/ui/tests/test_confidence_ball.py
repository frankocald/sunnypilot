import pytest
from unittest.mock import MagicMock
from openpilot.system.ui.lib.application import gui_app
from openpilot.selfdrive.ui.ui_state import ui_state
from openpilot.selfdrive.ui.onroad.augmented_road_view import AugmentedRoadView
from openpilot.selfdrive.ui.mici.onroad.confidence_ball import ConfidenceBall

def test_confidence_ball_added():
  # Initialize a headless/dummy raylib window so widget instantiation is safe
  gui_app.init_window("Test Window")
  # Initialize params before creating view
  ui_state.update_params()
  try:
    arv = AugmentedRoadView()
    assert hasattr(arv, "_confidence_ball"), "AugmentedRoadView does not have _confidence_ball attribute"
    assert isinstance(arv._confidence_ball, ConfidenceBall), "_confidence_ball is not an instance of ConfidenceBall"
  finally:
    pass

def test_confidence_ball_toggle():
  # Initialize a headless/dummy raylib window so widget instantiation is safe
  gui_app.init_window("Test Window")
  ui_state.update_params()
  try:
    arv = AugmentedRoadView()
    arv._confidence_ball.render = MagicMock()
    
    # Test with toggle enabled
    ui_state.show_confidence_ball = True
    ui_state.started = True
    
    arv._render(arv.rect)
    assert arv._confidence_ball.render.called, "Confidence ball render was not called when toggle is enabled"
    
    # Test with toggle disabled
    arv._confidence_ball.render.reset_mock()
    ui_state.show_confidence_ball = False
    
    arv._render(arv.rect)
    assert not arv._confidence_ball.render.called, "Confidence ball render was called when toggle is disabled"
  finally:
    ui_state.started = False
