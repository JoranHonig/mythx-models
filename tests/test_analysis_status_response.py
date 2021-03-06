from hypothesis import given

from mythx_models.response import Analysis, AnalysisStatusResponse

from .strategies.analysis import analysis_status


@given(analysis_status())
def test_serde(response):
    resp = AnalysisStatusResponse(**response)
    assert resp.dict(by_alias=True) == response
