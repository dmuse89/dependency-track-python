# Copyright 2020 Alvin Chen sonoma001@gmail.com
# SPDX-License-Identifier: GPL-2.0+

import logging

from .exceptions import DependencyTrackApiError

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Bom:
    """Class dedicated to all "projects" related endpoints"""

    def upload_bom(self, file_name, project_id=None, project_name=None, project_version=None, auto_create=False):
        """Upload a supported bill of material format document

        API Endpoint: POST /bom

        :return: UUID-Token
        :rtype: string
        :raises DependencyTrackApiError: if the REST call failed
        """
        multipart_form_data = {}
        multipart_form_data['bom']=('bom', open(file_name, 'r'))

        if project_id:
            multipart_form_data['project']=project_id
        if project_name:
            multipart_form_data['projectName']=project_name
        if project_version:
            multipart_form_data['projectVersion']=project_version
        multipart_form_data['autoCreate']=auto_create
        response = self.session.post(self.api + "/bom", params=self.paginated_param_payload, files=multipart_form_data)
        if response.status_code == 200:
            return response.json()
        else:
            description = f"Unable to upload BOM file"
            raise DependencyTrackApiError(description, response)






