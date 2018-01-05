A Python 3.6 wrapper for Sinter's (https://www.sinterdata.com) API.

# Usage
```python
from pysinter import Sinter

sinter = Sinter({{account_id}}, {{api_token}})

projects = sinter.list_projects()

response = sinter.trigger_job_run({{project_id}}, {{job_id}}