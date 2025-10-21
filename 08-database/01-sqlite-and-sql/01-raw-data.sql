-- This script creates a single, denormalized table ('raw_blog_data') 
-- and seeds it with realistic, non-numeric data for demonstrating data redundancy 
-- and the necessity of database decomposition (normalization).

DROP TABLE IF EXISTS raw_blog_data;

-- We use a single INSERT INTO statement to simulate data loaded from a single source (like a CSV)
-- before it has been split into normalized tables.
CREATE TABLE raw_blog_data (
    user_id INTEGER,
    username TEXT,
    email TEXT,
    post_id INTEGER,
    post_title TEXT,
    post_content TEXT,
    created_at DATETIME,
    tag_id INTEGER,
    tag_name TEXT
);

INSERT INTO raw_blog_data (user_id, username, email, post_id, post_title, post_content, created_at, tag_id, tag_name) VALUES
(1, 'AnyaS', 'anya@dev.com', 1, 'Understanding Python Decorators', 'A deep dive into @wraps and functional programming.', '2025-10-01 10:00:00', 1, 'Python'),
(1, 'AnyaS', 'anya@dev.com', 1, 'Understanding Python Decorators', 'A deep dive into @wraps and functional programming.', '2025-10-01 10:00:00', 3, 'Flask'),
(1, 'AnyaS', 'anya@dev.com', 2, 'Designing Clean Database Schemas', 'A guide to First, Second, and Third Normal Form.', '2025-10-01 11:00:00', 2, 'SQL'),
(1, 'AnyaS', 'anya@dev.com', 2, 'Designing Clean Database Schemas', 'A guide to First, Second, and Third Normal Form.', '2025-10-01 11:00:00', 5, 'Testing'),

(2, 'BenR', 'ben@code.com', 3, 'Flexbox vs. CSS Grid: A Visual Guide', 'When to use one over the other for responsive design.', '2025-10-02 09:00:00', 4, 'CSS'),
(2, 'BenR', 'ben@code.com', 3, 'Flexbox vs. CSS Grid: A Visual Guide', 'When to use one over the other for responsive design.', '2025-10-02 09:00:00', 6, 'WebDev'),
(2, 'BenR', 'ben@code.com', 4, 'Consuming Public APIs with Fetch', 'Handling JSON responses and error states in Javascript.', '2025-10-02 14:00:00', 8, 'JavaScript'),
(2, 'BenR', 'ben@code.com', 4, 'Consuming Public APIs with Fetch', 'Handling JSON responses and error states in Javascript.', '2025-10-02 14:00:00', 9, 'APIs'),

(3, 'ChloeT', 'chloe@data.org', 5, 'Data Viz with Pandas and Matplotlib', 'Creating meaningful charts from raw data.', '2025-10-03 16:30:00', 1, 'Python'),
(3, 'ChloeT', 'chloe@data.org', 5, 'Data Viz with Pandas and Matplotlib', 'Creating meaningful charts from raw data.', '2025-10-03 16:30:00', 7, 'DataScience'),
(3, 'ChloeT', 'chloe@data.org', 6, 'Advanced Window Functions in SQL', 'A deep dive into partitioning and ranking data.', '2025-10-03 08:45:00', 2, 'SQL'),
(3, 'ChloeT', 'chloe@data.org', 6, 'Advanced Window Functions in SQL', 'A deep dive into partitioning and ranking data.', '2025-10-03 08:45:00', 10, 'Docker'),

(4, 'DavidK', 'david@tech.com', 7, 'Unit Testing Flask Endpoints with Pytest', 'Mocking the database and ensuring 200 responses.', '2025-10-04 12:00:00', 3, 'Flask'),
(4, 'DavidK', 'david@tech.com', 7, 'Unit Testing Flask Endpoints with Pytest', 'Mocking the database and ensuring 200 responses.', '2025-10-04 12:00:00', 5, 'Testing'),
(4, 'DavidK', 'david@tech.com', 8, 'The Power of CSS Custom Properties', 'How to manage themes and dynamic styling.', '2025-10-04 09:30:00', 4, 'CSS'),
(4, 'DavidK', 'david@tech.com', 8, 'The Power of CSS Custom Properties', 'How to manage themes and dynamic styling.', '2025-10-04 09:30:00', 8, 'JavaScript'),

(5, 'EllaG', 'ella@web.co', 9, 'Containerizing Your Python Application', 'Using Docker Compose for multi-service setup.', '2025-10-05 15:45:00', 9, 'APIs'),
(5, 'EllaG', 'ella@web.co', 9, 'Containerizing Your Python Application', 'Using Docker Compose for multi-service setup.', '2025-10-05 15:45:00', 10, 'Docker'),
(5, 'EllaG', 'ella@web.co', 10, 'Intro to D3.js for Web Data', 'Creating interactive visualizations in the browser.', '2025-10-05 11:15:00', 6, 'WebDev'),
(5, 'EllaG', 'ella@web.co', 10, 'Intro to D3.js for Web Data', 'Creating interactive visualizations in the browser.', '2025-10-05 11:15:00', 7, 'DataScience'),

(6, 'FinnM', 'finn@app.net', 11, 'Optimizing Queries with EXPLAIN', 'Understanding query plans and performance tuning.', '2025-10-06 10:00:00', 1, 'Python'),
(6, 'FinnM', 'finn@app.net', 11, 'Optimizing Queries with EXPLAIN', 'Understanding query plans and performance tuning.', '2025-10-06 10:00:00', 2, 'SQL'),
(6, 'FinnM', 'finn@app.net', 12, 'Integrating Tailwind CSS in Flask', 'A modern approach to styling web apps.', '2025-10-06 11:30:00', 3, 'Flask'),
(6, 'FinnM', 'finn@app.net', 12, 'Integrating Tailwind CSS in Flask', 'A modern approach to styling web apps.', '2025-10-06 11:30:00', 4, 'CSS'),

(7, 'GraceL', 'grace@lab.io', 13, 'E2E Testing with Cypress', 'Writing robust end-to-end user flows.', '2025-10-07 09:00:00', 5, 'Testing'),
(7, 'GraceL', 'grace@lab.io', 13, 'E2E Testing with Cypress', 'Writing robust end-to-end user flows.', '2025-10-07 09:00:00', 6, 'WebDev'),
(7, 'GraceL', 'grace@lab.io', 14, 'Building Real-time Dashboards', 'Using WebSockets for live data updates.', '2025-10-07 14:00:00', 7, 'DataScience'),
(7, 'GraceL', 'grace@lab.io', 14, 'Building Real-time Dashboards', 'Using WebSockets for live data updates.', '2025-10-07 14:00:00', 8, 'JavaScript'),

(8, 'HenryP', 'henry@sys.ai', 15, 'Authentication with OAuth2 and Flask', 'Setting up token-based authentication.', '2025-10-08 16:30:00', 9, 'APIs'),
(8, 'HenryP', 'henry@sys.ai', 15, 'Authentication with OAuth2 and Flask', 'Setting up token-based authentication.', '2025-10-08 16:30:00', 1, 'Python'),
(8, 'HenryP', 'henry@sys.ai', 16, 'Database Mocking for Unit Tests', 'Using SQLite in-memory for fast testing.', '2025-10-08 08:45:00', 2, 'SQL'),
(8, 'HenryP', 'henry@sys.ai', 16, 'Database Mocking for Unit Tests', 'Using SQLite in-memory for fast testing.', '2025-10-08 08:45:00', 5, 'Testing'),

(9, 'IvyJ', 'ivy@soft.com', 17, 'CSS-in-JS vs Utility-First CSS', 'Comparing modern styling methodologies.', '2025-10-09 12:00:00', 4, 'CSS'),
(9, 'IvyJ', 'ivy@soft.com', 17, 'CSS-in-JS vs Utility-First CSS', 'Comparing modern styling methodologies.', '2025-10-09 12:00:00', 3, 'Flask'),
(9, 'IvyJ', 'ivy@soft.com', 18, 'Multi-Stage Docker Builds for React', 'Reducing image size for front-end applications.', '2025-10-09 09:30:00', 10, 'Docker'),
(9, 'IvyJ', 'ivy@soft.com', 18, 'Multi-Stage Docker Builds for React', 'Reducing image size for front-end applications.', '2025-10-09 09:30:00', 6, 'WebDev'),

(10, 'JenH', 'jen@blog.org', 19, 'Machine Learning in the Browser', 'Using TensorFlow.js for client-side model inference.', '2025-10-10 15:45:00', 7, 'DataScience'),
(10, 'JenH', 'jen@blog.org', 19, 'Machine Learning in the Browser', 'Using TensorFlow.js for client-side model inference.', '2025-10-10 15:45:00', 8, 'JavaScript'),
(10, 'JenH', 'jen@blog.org', 20, 'Building a GraphQL Endpoint with SQLAlchemy', 'Migrating from REST to GraphQL for complex data needs.', '2025-10-10 11:15:00', 9, 'APIs'),
(10, 'JenH', 'jen@blog.org', 20, 'Building a GraphQL Endpoint with SQLAlchemy', 'Migrating from REST to GraphQL for complex data needs.', '2025-10-10 11:15:00', 2, 'SQL');
