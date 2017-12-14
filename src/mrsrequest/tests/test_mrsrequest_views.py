import io
import json

from dbdiff.fixture import Fixture
import mock
import pytest

from django.urls import reverse

from person.models import Person
from pmt.models import PMT
from mrsrequest.models import MRSRequest
from mrsrequest.tests.utils import sessions, upload_request
from mrsrequest.views import MRSFileDeleteView, MRSFileUploadView
from transport.models import Transport, Bill


def test_mrsfiledeleteview_allowed_objects_usage(rf):
    '''Test promise to use model.objects.allowed_objects() for security.'''

    request = rf.delete('/delete/123')

    view = MRSFileDeleteView(
        request=request,
        model=mock.Mock(),
        kwargs=dict(pk=13)
    )
    response = view.dispatch(request, pk=13)

    # Check if the manager allowed_objects was called properly, it's the heart
    # of security in the file delete view, it's a bit obscure so don't rely on
    # it and add integration tests for each of your url made with
    # MRSFileDeleteView and your model, ie. like pmt module.
    view.model.objects.allowed_objects.assert_called_once_with(request)
    assert view.object is (
        view.model.objects.allowed_objects.return_value.get.return_value
    ), 'delete() should have made self.object = self.get_object()'

    # Check that the object was deleted
    view.object.delete.assert_called_once()

    # Check that we have a nice response code
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize("session", sessions)
def test_mrsfileuploadview_security(rf, id, session):
    '''Save upload if request had MRSRequest.allow(request).'''
    record = type(
        'TestModel',
        (mock.Mock,),
        dict(get_delete_url=lambda s: '/del'),
    )

    model = mock.Mock()
    model.objects.record_upload.return_value = record()

    view = MRSFileUploadView.as_view(model=model)

    with io.BytesIO(b'test_mrsfileuploadview_security') as f:
        f.name = 'test_mrsfileuploadview_security.jpg'

        request = upload_request(rf, id, f)
        request.session = session

        # Test deny
        response = view(request, mrsrequest_uuid=id)
        assert response.status_code == 400
        assert model.objects.record_upload.call_count == 0, (
            'record_upload should not have been called')

        # Allow
        MRSRequest(id=id).allow(request)

        # Test allow
        response = view(request, mrsrequest_uuid=id)
        assert response.status_code == 201

        # Test record_upload call: mrsrequest argument
        mrsrequest = model.objects.record_upload.call_args_list[0][0][0]
        assert mrsrequest.id == id, 'should have kept uuid from upload_request'

        # Test record_upload call: file argument
        mrsrequest = model.objects.record_upload.call_args_list[0][0][0]
        upload = model.objects.record_upload.call_args_list[0][0][1]
        assert upload == request.FILES['file'], (
            'should have used the passed file'
        )

        # record_upload() should have been called once, as described above
        model.objects.record_upload.assert_called_once()

        # Test response
        data = json.loads(response.content)
        assert data['deleteUrl'] == '/del', 'should be get_delete_url()'


def form_data():
    return dict(
        transported_first_name='First',
        transported_last_name='Last',
        transported_birth_date='2000-01-01',
    )


@pytest.mark.django_db
def test_your_import(client):
    pytest.skip()
    client.post(
        reverse('mrsrequest_create'),
        form_data()
    )

    Fixture(
        './tests/first.json',
        models=[MRSRequest, Person, PMT, Transport, Bill]
    ).assertNoDiff()