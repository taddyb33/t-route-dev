# Testing the T-Route FastAPI Extension

The following folder contains data files that are to be used to test the T-Route FastAPI code within src/app

To use these files, follow the steps below:

1. Copy the `test_compose.yaml` file in the root project dir 
2. Run `docker compose -f test_compose.yaml up`
3. visit `localhost:8004/docs` in your browser
4. Enter the following parameters into the `/api/v1/flow_routing/v4` endpoint
- lid=CAGM7
- feature_id=2930769
- hy_id=1074884
- initial_start=0
- start_time=2024-08-24T00:00:00
- num_forecast_days=5
5. Click execute
6. A Status 200 code means the run ran, and test/api/data/troute_output will be populated in the `{lid}/` folder

## Docs:
See `doc/api_docs.md` for specific docs related to the T-Route API