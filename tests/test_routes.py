"""
Test functions to test the features of app/routes.py
"""

def test_get_single_book_by_title_success(client, mocker):
    client, mock_collection = client
    mock_collection.find.return_value = [{'title': 'Test Book', 'led_position': 42}]
    mocker.patch('app.routes.Book', return_value=mocker.Mock(led_position=42))
    response = client.post('/singleBookByTitle', json={'title': 'Test Book'})
    assert response.data == b'success'
    mock_collection.find.assert_called_once_with({'title': 'Test Book'}, {'_id': 0})

def test_get_single_book_by_title_validation_error(client):
    client, _ = client
    response = client.post('/singleBookByTitle', json={'title': ''})
    assert b'error' in response.data
    assert response.status_code == 200  # Adjust according to your error handling logic

def test_get_single_book_by_title_multiple_books(client, mocker):
    client, mock_collection = client
    mock_collection.find.return_value = [
        {'title': 'Test Book', 'led_position': 42},
        {'title': 'Test Book', 'led_position': 43}
    ]
    mocker.patch('app.routes.Book', side_effect=lambda **kwargs: mocker.Mock(**kwargs))
    response = client.post('/singleBookByTitle', json={'title': 'Test Book'})
    assert response.data == b'success'

def test_get_single_book_by_title_value_error(client, mocker):
    client, _ = client
    mocker.patch('app.routes.SingleBookByTitleRequest.validate',
                 side_effect=ValueError('Invalid title'))
    response = client.post('/singleBookByTitle', json={'title': '##Invalid'})
    assert b'Invalid title' in response.data
    assert response.status_code == 200  # Adjust according to your error handling logic
