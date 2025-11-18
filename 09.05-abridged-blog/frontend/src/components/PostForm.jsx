import React, {useState, useEffect} from 'react';

function PostForm({ onSubmit, initPost = {title: '', content: ''}, 
    buttonText, onCancel}) {
    
    const [title, setTitle] = useState(initPost.title);
    const [content, setContent] = useState(initPost.content);

    useEffect(() => {
        setTitle(initPost.title);
        setContent(initPost.content);
    }, [initPost.title, initPost.content, initPost.id]);

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!title.trim() || !content.trim()) {
            alert("Title and content cannot be empty.");
            return;
        }
        onSubmit( {title, content} );
    };

    return (
        <form onSubmit={handleSubmit}>
            <div className="form-group">
                <label htmlFor="title">Title:</label>
                <input
                    type="text"
                    id="title"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    required
                />
            </div>
            <div className="form-group">
                <label htmlFor="content">Content:</label>
                <input
                    type="text"
                    id="content"
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                    required
                />
            </div>
            <div className="post-actions">
                <button type="submit" className="btn btn-primary">
                    {buttonText}
                </button>
                {onCancel && (
                    <button type="button" onClick={onCancel}
                    className="btn btn-secondary">
                        Cancel
                    </button>
                )}
            </div>

        </form>

    );
}

export default PostForm;