import json

# Base URL for the posts API endpoints
API_BASE = '/api/v1/posts'

# POST /posts (Create)
def test_add_post_success(client):
    data = {
        'title': 'My First Post',
        'content': 'This is the content of my first post.'
    }
    
    response = client.post(
        API_BASE,
        data=json.dumps(data),
        content_type='application/json'
    )
    
    assert response.status_code == 201
    response_data = json.loads(response.data)
    
    # Check that the response contains the created post data
    assert 'id' in response_data
    assert response_data['title'] == 'My First Post'

def test_add_post_missing_content_fails(client):
    data = {'title': 'Title is here'}
    
    response = client.post(
        API_BASE,
        data=json.dumps(data),
        content_type='application/json'
    )
    
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == 'Content is required'


# GET /posts (Read All)
def test_get_all_posts_with_data(client, create_test_post):
    # Create two posts using the fixture function
    create_test_post("Post A", "Content A")
    create_test_post("Post B", "Content B")
    
    response = client.get(API_BASE)
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2
    # The API should return a list of dictionaries
    assert data[0]['title'] == 'Post B' 

# PATCH /posts/<int:post_id> (Update)
def test_edit_post_success(client, create_test_post):
    post_id = create_test_post(title="Original Title", content="Original Content")
    
    update_data = {
        'title': 'Updated Title',
        'content': 'Updated Content Text'
    }

    response = client.patch(
        f'{API_BASE}/{post_id}',
        data=json.dumps(update_data),
        content_type='application/json'
    )

    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data['id'] == post_id
    assert response_data['title'] == 'Updated Title'
    
def test_edit_post_missing_not_found(client):
    response = client.patch(
        f'{API_BASE}/999',
        data=json.dumps({'title': 'New'}),
        content_type='application/json'
    )
    assert response.status_code == 404
    assert json.loads(response.data)['message'] == 'Post ID 999 not found.'
    
    
# DELETE /posts/<int:post_id> (Delete)
def test_delete_post_success(client, create_test_post):
    post_id = create_test_post()
    
    response = client.delete(f'{API_BASE}/{post_id}')
    
    assert response.status_code == 200
    assert json.loads(response.data)['message'] == f'Post ID {post_id} deleted'
    
    # Verification: Ensure it's gone
    get_response = client.get(API_BASE)
    assert len(json.loads(get_response.data)) == 0

def test_delete_post_not_found(client):
    response = client.delete(f'{API_BASE}/999')
    
    assert response.status_code == 404
    assert json.loads(response.data)['message'] == 'Post ID 999 not found.'