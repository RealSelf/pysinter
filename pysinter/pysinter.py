import requests
import json


class Sinter(object):
    """
    Class for interacting with the Sinter API

    * :py:meth:`list_projects` - lists all projects under the account specified when instantiating the Sinter object
    * :py:meth:`get_project' - returns details of a single project id
    * :py:meth:`list_job_definitions` - lists all job definitions for the specified project id
    * :py:meth:`get_job_definition` - (not implemented) returns details of a single job definition
    * :py:meth:`list_job_runs` - (not implemented) lists all job runs for the specified job id
    * :py:meth:`get_job_run` - returns details of a single job run
    * :py:meth:`trigger_job_run` - triggers an execution of a job definition, returns details of that job run
    """

    def __init__(self, account_id, api_token, api_version=1):
        self.account_id = account_id
        self.api_token = api_token
        self.api_version = api_version
        self.api_base = 'https://app.sinterdata.com/api/v{}/accounts/{}'.format(self.api_version, self.account_id)

    def _do_request(self, method, url_suffix):
        url = self.api_base + url_suffix
        headers = {'Authorization': 'Token %s' % self.api_token}
        method = method.upper()

        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers)
        else:
            raise ValueError("method must equal either 'GET' or 'POST'")

        if response.status_code == requests.codes.ok:
            return json.loads(response.content)
        else:
            raise RuntimeError(response.content)

    def list_projects(self):
        return self._do_request('GET', '/projects/')['data']

    def get_project(self, project_id):
        return self._do_request('GET', '/projects/%s/' % (project_id))['data']

    def list_job_definitions(self, project_id):
        return self._do_request('GET', '/projects/%s/definitions/' % (project_id))

    def get_job_definition(self, project_id, job_id):
        raise NotImplementedError
        # return self._do_request('/projects/%s/definitions/%s/' % (project_id, job_id))

    def list_job_runs(self, project_id, job_id):
        raise NotImplementedError
        # return self._do_request('/projects/%s/definitions/%s/runs/' % (project_id, job_id))

    def get_job_run(self, project_id, job_run_id):
        return self._do_request('GET', '/projects/%s/runs/%s/' % (project_id, job_run_id))

    def trigger_job_run(self, project_id, job_id):
        return self._do_request('POST', '/projects/%s/definitions/%s/runs/' % (project_id, job_id))
