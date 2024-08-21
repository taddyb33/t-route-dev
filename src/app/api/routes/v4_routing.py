from typing import Annotated, List

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from nwm_routing import main_v04 as t_route
import yaml

from app.api.services.edit_config import edit_yaml, create_params
from app.core import get_settings
from app.core.settings import Settings
from app.schemas import TRouteOuput

router = APIRouter()

@router.get("/", response_model=TRouteOuput)
async def get_gauge_data(
    lid: str,
    feature_id: str, 
    start_time: str,
    num_forecast_days: int,
    settings: Annotated[Settings, Depends(get_settings)]
) -> TRouteOuput:
    """An API call for running T-Route

    Parameters
    ----------
    lid: str
        The Location of the RFC Point
    feature_id: str
        The COMID associated with the LID
    start_time: str
        The start time for the forecast
    num_forecast_days: int
        The number of days in the forecast
    Returns
    -------
    TRouteOutput
        A successful T-Route run
    """
    base_config = settings.base_config
    params = create_params(
        lid,
        feature_id,
        start_time,
        num_forecast_days,
        settings
    )
    yaml_file_path = edit_yaml(base_config, params)
    try:
        t_route(["-f", yaml_file_path.__str__()])
    except Exception as e:
        JSONResponse(
            status_code=500,
            content={"message": e},
        )

    yaml_file_path.unlink()

    return TRouteOuput(
        message="T-Route run successfully",
        lid=lid,
        feature_id=feature_id,
    )



    