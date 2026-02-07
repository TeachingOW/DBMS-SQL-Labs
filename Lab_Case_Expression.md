# Lab: SQL CASE Expressions

## 🎯 Learning Objectives

By the end of this lab, you will be able to:
- Understand and use SQL CASE expressions effectively
- Compare CASE expressions with alternative query approaches
- Apply CASE expressions in SELECT, WHERE, and HAVING clauses
- Use CASE with aggregate functions for conditional counting
- Understand when CASE expressions improve query readability and performance

## 📋 Prerequisites

- Understanding of basic SQL SELECT statements
- Knowledge of aggregate functions (COUNT, SUM, AVG)
- Familiarity with GROUP BY and HAVING clauses
- Basic understanding of subqueries and CTEs (Common Table Expressions)

## 📚 Introduction

The **CASE expression** is one of SQL's most powerful and versatile tools. It allows you to implement conditional logic directly within your SQL queries, making your code more readable and often more efficient.

### CASE Expression Syntax

```sql
-- Simple CASE (comparing against a single column)
CASE column_name
    WHEN value1 THEN result1
    WHEN value2 THEN result2
    ELSE default_result
END

-- Searched CASE (more flexible with conditions)
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ELSE default_result
END
```

### Common Use Cases

1. **Conditional Aggregation**: Count or sum only rows meeting specific criteria
2. **Data Transformation**: Convert values or categorize data
3. **Complex Filtering**: Implement sophisticated WHERE/HAVING conditions
4. **Pivot Operations**: Transform rows into columns

## 🚀 Getting Started

### Step 1: Create the Database and Sample Data

We'll work with an `app_events` table that tracks user interactions in a mobile application. This realistic scenario demonstrates how CASE expressions can analyze user behavior patterns.

```sql
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
```

## 🎓 Problem: Finding Browse-Heavy Sessions

**Business Goal**: Identify user sessions that indicate a poor user experience - users who scroll a lot but don't click much and don't make purchases. These sessions may indicate:
- Confusing UI/UX
- Irrelevant content
- Poor product recommendations
- Potential bugs or performance issues

### Criteria for Browse-Heavy Sessions:
1. Session duration > 30 minutes
2. At least 5 scroll events
3. Click-to-scroll ratio < 0.2 (less than 20% clicks relative to scrolls)
4. No purchase events

## 💡 Solution 1: Using CASE Expressions (Clean & Efficient)

This approach uses CASE expressions to conditionally count events directly within the query:

```sql
-- Write your MySQL query statement below
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
```

### How This Query Works:

1. **Conditional Counting with CASE**:
   ```sql
   COUNT(CASE WHEN event_type = 'scroll' THEN 1 END)
   ```
   - The CASE expression returns 1 only when event_type is 'scroll'
   - COUNT ignores NULL values, so only scroll events are counted
   - This is more readable than filtering with WHERE

2. **Session Duration Calculation**:
   ```sql
   TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp))
   ```
   - Calculates the difference between first and last event in minutes

3. **Click-to-Scroll Ratio**:
   ```sql
   COUNT(CASE WHEN event_type = 'click' THEN 1 END) / scroll_count < 0.2
   ```
   - Divides click count by scroll count to get the ratio

4. **No Purchase Condition**:
   ```sql
   COUNT(CASE WHEN event_type = 'purchase' THEN 1 END) = 0
   ```
   - Ensures no purchase events exist in the session

### Advantages of CASE Expression Approach:
- ✅ **Concise**: Single query, easy to read
- ✅ **Performant**: Single pass through the data
- ✅ **Maintainable**: Logic is clear and straightforward
- ✅ **Flexible**: Easy to add more conditions

## 🔄 Solution 2: Using CTEs (Complex but Educational)

This alternative approach uses Common Table Expressions to achieve the same result. While more verbose, it demonstrates how queries can be decomposed into logical steps:

```sql
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
```

### How This CTE Approach Works:

1. **CTE A**: Groups events by type and counts them
2. **CTE E**: Handles sessions with no clicks by adding a zero-count row
3. **CTE T**: Calculates session duration in seconds
4. **CTE TT**: Joins all CTEs together to create a comprehensive view
5. **Final SELECT**: Applies filters and formats output

### Comparison: CASE vs CTE Approach

| Aspect | CASE Expression | CTE Approach |
|--------|----------------|--------------|
| **Lines of Code** | 10 lines | 40+ lines |
| **Readability** | High - logic is clear | Medium - requires understanding multiple CTEs |
| **Performance** | Better - single scan | Potentially slower - multiple scans/joins |
| **Debugging** | Harder to debug intermediate steps | Easier - can query each CTE separately |
| **Maintainability** | Better - less code | More complex - multiple dependencies |
| **Use Case** | Production queries | Learning/debugging complex logic |

## 🧪 Practice Exercises

### Exercise 1: Basic CASE Usage
Write a query to categorize sessions as 'short' (< 15 min), 'medium' (15-45 min), or 'long' (> 45 min):

```sql
-- Your solution here
```

<details>
<summary>Solution</summary>

```sql
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
```
</details>

### Exercise 2: Multiple Conditional Counts
Write a query that shows for each session:
- Total events
- Number of scrolls
- Number of clicks  
- Number of purchases
- An engagement score (scrolls * 1 + clicks * 3 + purchases * 10)

```sql
-- Your solution here
```

<details>
<summary>Solution</summary>

```sql
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
```
</details>

### Exercise 3: CASE in WHERE Clause
Write a query to find sessions where:
- If the session has any purchase, include it regardless of other criteria
- If no purchase, only include if scroll_count >= 5 and duration > 20 minutes

```sql
-- Your solution here
```

<details>
<summary>Solution</summary>

```sql
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
```
</details>

### Exercise 4: Convert CTE to CASE
Try rewriting the following CTE query using CASE expressions:

```sql
WITH event_counts AS (
    SELECT 
        session_id,
        user_id,
        SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END) AS scrolls,
        SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) AS clicks
    FROM app_events
    GROUP BY session_id, user_id
)
SELECT * FROM event_counts WHERE scrolls > clicks * 2;
```

Can this be written more efficiently without the CTE?

<details>
<summary>Solution</summary>

```sql
SELECT 
    session_id,
    user_id,
    COUNT(CASE WHEN event_type = 'scroll' THEN 1 END) AS scrolls,
    COUNT(CASE WHEN event_type = 'click' THEN 1 END) AS clicks
FROM app_events
GROUP BY session_id, user_id
HAVING COUNT(CASE WHEN event_type = 'scroll' THEN 1 END) > 
       COUNT(CASE WHEN event_type = 'click' THEN 1 END) * 2;
```
</details>

## 🎓 Advanced Topics

### Using CASE with SUM for Weighted Counts

```sql
-- Calculate engagement score with different weights
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
GROUP BY session_id, user_id;
```

### CASE in ORDER BY for Custom Sorting

```sql
-- Order by purchase first, then by scroll count
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
```

## 📊 Performance Considerations

### When to Use CASE:
- ✅ When you need conditional aggregation
- ✅ When transforming data in the same query
- ✅ When the logic is straightforward
- ✅ When performance is critical (single pass through data)

### When CTEs Might Be Better:
- ✅ When debugging complex logic step by step
- ✅ When the same subquery is needed multiple times
- ✅ When logic needs to be clearly separated for readability
- ✅ For teaching/learning purposes

## 🔑 Key Takeaways

1. **CASE expressions** are powerful tools for conditional logic in SQL
2. They can be used in SELECT, WHERE, HAVING, and ORDER BY clauses
3. CASE with aggregate functions enables conditional counting/summing
4. The CASE approach is often **more concise and performant** than alternatives
5. CTEs can make complex queries more **readable for debugging**
6. Choose the approach that best balances **performance and maintainability**

## 📚 Additional Resources

- [MySQL CASE Documentation](https://dev.mysql.com/doc/refman/8.0/en/flow-control-functions.html#operator_case)
- [SQL CASE Expression Best Practices](https://mode.com/sql-tutorial/sql-case/)
- [Aggregate Functions with CASE](https://learnsql.com/blog/case-when-with-aggregate-functions/)

## 🎯 Summary

In this lab, you learned:
- How to use CASE expressions for conditional logic
- The difference between simple and searched CASE
- How CASE expressions work with aggregate functions
- When to use CASE vs alternative approaches like CTEs
- Real-world applications of CASE expressions in data analysis

Practice these concepts with your own datasets to master conditional logic in SQL!
