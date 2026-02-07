-- ================================================
-- Lab: SQL CASE Expressions
-- Complete setup and examples
-- ================================================

-- Create database
DROP DATABASE IF EXISTS case_lab;
CREATE DATABASE case_lab;
USE case_lab;

-- Create app_events table
CREATE TABLE app_events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    session_id INT NOT NULL,
    user_id INT NOT NULL,
    event_type VARCHAR(20) NOT NULL,
    event_timestamp TIMESTAMP NOT NULL,
    INDEX idx_session (session_id),
    INDEX idx_user (user_id),
    INDEX idx_type (event_type)
);

-- Insert sample data with various event types
INSERT INTO app_events (session_id, user_id, event_type, event_timestamp) VALUES
-- Session 1: Active session with lots of scrolling, few clicks, no purchase
(1, 101, 'scroll', '2024-01-15 10:00:00'),
(1, 101, 'scroll', '2024-01-15 10:05:00'),
(1, 101, 'scroll', '2024-01-15 10:10:00'),
(1, 101, 'scroll', '2024-01-15 10:15:00'),
(1, 101, 'scroll', '2024-01-15 10:20:00'),
(1, 101, 'scroll', '2024-01-15 10:25:00'),
(1, 101, 'scroll', '2024-01-15 10:30:00'),
(1, 101, 'click', '2024-01-15 10:35:00'),
(1, 101, 'scroll', '2024-01-15 10:40:00'),

-- Session 2: Short session, doesn't meet criteria
(2, 102, 'scroll', '2024-01-15 11:00:00'),
(2, 102, 'scroll', '2024-01-15 11:05:00'),
(2, 102, 'click', '2024-01-15 11:08:00'),

-- Session 3: Session with purchase (should be excluded)
(3, 103, 'scroll', '2024-01-15 12:00:00'),
(3, 103, 'scroll', '2024-01-15 12:10:00'),
(3, 103, 'scroll', '2024-01-15 12:20:00'),
(3, 103, 'scroll', '2024-01-15 12:30:00'),
(3, 103, 'scroll', '2024-01-15 12:40:00'),
(3, 103, 'scroll', '2024-01-15 12:50:00'),
(3, 103, 'click', '2024-01-15 12:55:00'),
(3, 103, 'purchase', '2024-01-15 13:00:00'),

-- Session 4: Long session with many scrolls, few clicks, no purchase
(4, 104, 'scroll', '2024-01-15 14:00:00'),
(4, 104, 'scroll', '2024-01-15 14:08:00'),
(4, 104, 'scroll', '2024-01-15 14:16:00'),
(4, 104, 'scroll', '2024-01-15 14:24:00'),
(4, 104, 'scroll', '2024-01-15 14:32:00'),
(4, 104, 'scroll', '2024-01-15 14:40:00'),
(4, 104, 'scroll', '2024-01-15 14:48:00'),
(4, 104, 'scroll', '2024-01-15 14:56:00'),
(4, 104, 'scroll', '2024-01-15 15:04:00'),
(4, 104, 'click', '2024-01-15 15:12:00'),

-- Session 5: High scroll-to-click ratio session
(5, 105, 'scroll', '2024-01-15 16:00:00'),
(5, 105, 'scroll', '2024-01-15 16:07:00'),
(5, 105, 'scroll', '2024-01-15 16:14:00'),
(5, 105, 'scroll', '2024-01-15 16:21:00'),
(5, 105, 'scroll', '2024-01-15 16:28:00'),
(5, 105, 'scroll', '2024-01-15 16:35:00'),
(5, 105, 'scroll', '2024-01-15 16:42:00'),
(5, 105, 'scroll', '2024-01-15 16:49:00'),
(5, 105, 'scroll', '2024-01-15 16:56:00'),
(5, 105, 'scroll', '2024-01-15 17:03:00'),
(5, 105, 'click', '2024-01-15 17:10:00');

-- ================================================
-- Solution 1: Using CASE Expressions (Clean & Efficient)
-- ================================================
SELECT 
    session_id,
    user_id,
    TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) AS session_duration_minutes,
    COUNT(CASE WHEN event_type = 'scroll' THEN 1 END) AS scroll_count
FROM app_events
GROUP BY session_id, user_id
HAVING session_duration_minutes > 30
    AND scroll_count >= 5
    AND COUNT(CASE WHEN event_type = 'click' THEN 1 END) / scroll_count < 0.2
    AND COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) = 0
ORDER BY scroll_count DESC, session_id;

-- ================================================
-- Solution 2: Using CTEs (Complex but Educational)
-- ================================================
WITH A AS (
    -- Count events by type for each session
    SELECT session_id, user_id, event_type, COUNT(*) AS c
    FROM app_events
    GROUP BY session_id, user_id, event_type 
), 
E AS (
    -- Ensure all sessions have a 'click' row (even if count is 0)
    SELECT * FROM A 
    UNION
    SELECT session_id, user_id, 'click', 0 
    FROM A 
    WHERE session_id NOT IN (
        SELECT session_id FROM A WHERE event_type = 'click'
    )
),
T AS (
    -- Calculate session duration in seconds
    SELECT  
        session_id,  
        UNIX_TIMESTAMP(MAX(event_timestamp)) - UNIX_TIMESTAMP(MIN(event_timestamp)) AS d
    FROM app_events
    GROUP BY session_id
),
TT AS (
    -- Join everything together
    SELECT 
        T.session_id, 
        E_c.user_id,  
        E_s.c AS scroll_count, 
        E_c.c AS clicks,
        T.d AS duration
    FROM E E_c
    JOIN E E_s ON E_c.session_id = E_s.session_id
    JOIN T ON E_c.session_id = T.session_id
    WHERE E_s.event_type = 'scroll'
        AND E_c.event_type = 'click'
)

-- Final selection with filters
SELECT 
    session_id, 
    user_id, 
    duration/60 AS session_duration_minutes, 
    scroll_count  
FROM TT
WHERE session_id NOT IN (
    SELECT session_id FROM E WHERE event_type = 'purchase'
)
    AND duration > 30*60 
    AND scroll_count >= 5 
    AND clicks/scroll_count < 0.2
ORDER BY scroll_count DESC, session_id;

-- ================================================
-- Practice Exercises
-- ================================================

-- Exercise 1: Categorize sessions by duration
SELECT 
    session_id,
    user_id,
    TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) AS duration,
    CASE
        WHEN TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) < 15 THEN 'short'
        WHEN TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) <= 45 THEN 'medium'
        ELSE 'long'
    END AS session_category
FROM app_events
GROUP BY session_id, user_id;

-- Exercise 2: Multiple conditional counts with engagement score
SELECT 
    session_id,
    user_id,
    COUNT(*) AS total_events,
    COUNT(CASE WHEN event_type = 'scroll' THEN 1 END) AS scroll_count,
    COUNT(CASE WHEN event_type = 'click' THEN 1 END) AS click_count,
    COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) AS purchase_count,
    (COUNT(CASE WHEN event_type = 'scroll' THEN 1 END) * 1 +
     COUNT(CASE WHEN event_type = 'click' THEN 1 END) * 3 +
     COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) * 10) AS engagement_score
FROM app_events
GROUP BY session_id, user_id
ORDER BY engagement_score DESC;

-- Exercise 3: CASE in HAVING clause
SELECT 
    session_id,
    user_id,
    TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) AS duration,
    COUNT(CASE WHEN event_type = 'scroll' THEN 1 END) AS scroll_count,
    COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) AS purchase_count
FROM app_events
GROUP BY session_id, user_id
HAVING 
    CASE 
        WHEN COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) > 0 THEN 1
        WHEN COUNT(CASE WHEN event_type = 'scroll' THEN 1 END) >= 5 
             AND TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) > 20 THEN 1
        ELSE 0
    END = 1;

-- ================================================
-- Advanced Examples
-- ================================================

-- Weighted engagement score
SELECT 
    session_id,
    user_id,
    SUM(CASE 
        WHEN event_type = 'scroll' THEN 1
        WHEN event_type = 'click' THEN 3
        WHEN event_type = 'purchase' THEN 10
        ELSE 0
    END) AS weighted_engagement
FROM app_events
GROUP BY session_id, user_id
ORDER BY weighted_engagement DESC;

-- Custom sorting with CASE in ORDER BY
SELECT 
    session_id,
    user_id,
    COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) AS purchases,
    COUNT(CASE WHEN event_type = 'scroll' THEN 1 END) AS scrolls
FROM app_events
GROUP BY session_id, user_id
ORDER BY 
    CASE WHEN COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) > 0 THEN 0 ELSE 1 END,
    COUNT(CASE WHEN event_type = 'scroll' THEN 1 END) DESC;
