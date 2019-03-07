# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# [START monitoring_irm_annotate_incident]
def annotate_incident(incident, content):
    from google.cloud import irm

    client = irm.IncidentServiceClient()
    annotation = client.create_annotation(incident.name, {'content': content})
    return annotation
# [END monitoring_irm_annotate_incident]

# [START monitoring_irm_change_severity]
def change_severity(incident, new_severity):
    from google.cloud import irm

    client = irm.IncidentServiceClient()
    incident.severity = new_severity
    update_mask = {'paths': ['severity']}

    updated = client.update_incident(incident, update_mask=update_mask)
    return updated
# [END monitoring_irm_change_severity]
    from google.cloud import irm


# [START monitoring_irm_change_stage]
def change_stage(incident, new_stage):
    from google.cloud import irm

    client = irm.IncidentServiceClient()
    incident.stage = new_stage
    update_mask = {'paths': ['stage']}

    updated = client.update_incident(incident, update_mask=update_mask)
    return updated
# [END monitoring_irm_change_stage]

# [START monitoring_irm_create_incident]
def create_incident(project_id, title):
    from google.cloud import irm

    client = irm.IncidentServiceClient()
    parent = client.project_path(project_id)

    incident = client.create_incident({'title': title}, parent)
    return incident
# [END monitoring_irm_create_incident]

# [START monitoring_irm_create_signal]
def create_signal(project_id, title, content):
    from google.cloud import irm

    client = irm.IncidentServiceClient()
    parent = client.project_path(project_id)

    signal = client.create_signal(parent,
        {'title': title, 'content': content})
    return signal
# [END monitoring_irm_create_signal]
