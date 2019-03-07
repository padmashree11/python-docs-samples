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

import os
import pytest
from uuid import uuid4

from google.cloud import irm

import snippets


PROJECT = os.environ['GCLOUD_PROJECT']

@pytest.fixture(scope='module')
def incident():
    client = irm.IncidentServiceClient()
    parent = client.project_path(PROJECT)
    title = str(uuid4()) + ' test title'
    test_incident = client.create_incident({'title': title}, parent)

    yield test_incident

    test_incident.stage = 3 # RESOLVED
    update_mask = {'paths': ['stage']}
    client.update_incident(test_incident, update_mask=update_mask)


def test_create_incident():
    title = str(uuid4()) + ' create incident test'

    result = snippets.create_incident(PROJECT, title)
    assert result is not None
    assert 'Incident' in str(type(result))
    assert result.title == title

def test_create_signal():
    title = str(uuid4()) + ' create signal test'
    content = 'Test content string'

    result = snippets.create_signal(PROJECT, title, content)
    assert result is not None
    assert 'Signal' in str(type(result))
    assert result.title == title
    assert result.content == content

def test_annotate_incident(incident):
    content = 'A new annotation ' + str(uuid4())
    result = snippets.annotate_incident(incident, content)
    assert result is not None
    assert 'Annotation' in str(type(result))
    assert result.content == content

def test_change_severity(incident):
    new_severity = 1
    result = snippets.change_severity(incident, new_severity)
    assert result is not None
    assert 'Incident' in str(type(result))
    assert result.severity == new_severity

def test_change_stage(incident):
    new_stage = 1
    result = snippets.change_stage(incident, new_stage)
    assert result is not None
    assert 'Incident' in str(type(result))
    assert result.stage == new_stage

