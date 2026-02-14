# Contributing to DBMS-SQL-Labs

Thank you for your interest in contributing to DBMS-SQL-Labs! This document provides guidelines and instructions for contributing to this educational repository.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Contribution Guidelines](#contribution-guidelines)
- [Style Guidelines](#style-guidelines)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

### Our Pledge
We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in all interactions.

### Expected Behavior
- Be respectful and inclusive
- Provide constructive feedback
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior
- Harassment or discrimination
- Trolling or insulting comments
- Publishing others' private information
- Other unprofessional conduct

## How Can I Contribute?

### 1. Reporting Bugs or Issues
If you find a bug or error in the labs:

1. Check if the issue already exists in [Issues](https://github.com/TeachingOW/DBMS-SQL-Labs/issues)
2. If not, create a new issue with:
   - Clear, descriptive title
   - Detailed description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots (if applicable)
   - Your environment (OS, MySQL version, etc.)

**Example:**
```
Title: SQL syntax error in Lab 4, Exercise 3

Description:
In Lab 4, Exercise 3, the provided SQL query has a syntax error.
The query uses 'INNER JOUN' instead of 'INNER JOIN' on line 45.

Steps to reproduce:
1. Open Lab 4
2. Navigate to Exercise 3
3. Copy and run the provided query

Expected: Query should execute successfully
Actual: Syntax error is thrown

Environment:
- OS: Ubuntu 20.04
- MySQL: 8.0.27
```

### 2. Suggesting Enhancements
Have ideas to improve the labs?

1. Open an issue with the "enhancement" label
2. Describe your suggestion clearly
3. Explain the benefits
4. Provide examples if possible

### 3. Improving Documentation
Documentation improvements are always welcome:
- Fix typos or grammatical errors
- Clarify confusing explanations
- Add missing information
- Improve code comments
- Create new guides or tutorials

### 4. Adding New Content
You can contribute new:
- Lab exercises
- Example datasets
- Code samples
- Tutorial content
- Practice problems

### 5. Fixing Bugs
Browse the [Issues](https://github.com/TeachingOW/DBMS-SQL-Labs/issues) for bugs labeled "bug" or "help wanted".

## Getting Started

### 1. Fork the Repository
Click the "Fork" button at the top right of the repository page.

### 2. Clone Your Fork
```bash
git clone https://github.com/YOUR_USERNAME/DBMS-SQL-Labs.git
cd DBMS-SQL-Labs
```

### 3. Add Upstream Remote
```bash
git remote add upstream https://github.com/TeachingOW/DBMS-SQL-Labs.git
```

### 4. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 5. Make Your Changes
- Edit files as needed
- Test your changes thoroughly
- Ensure code examples work correctly

### 6. Commit Your Changes
```bash
git add .
git commit -m "Brief description of changes"
```

### 7. Push to Your Fork
```bash
git push origin feature/your-feature-name
```

### 8. Create a Pull Request
Go to your fork on GitHub and click "New Pull Request".

## Contribution Guidelines

### Lab Content Guidelines

#### SQL Code
- **Test all SQL queries** before submitting
- Use **clear, descriptive variable names**
- Include **comments** for complex queries
- Follow **consistent formatting** (see Style Guidelines)
- Provide **both problem and solution** when appropriate

#### Examples
```sql
-- Good: Clear, commented, formatted
-- Calculate average salary by department
SELECT 
    d.department_name,
    AVG(e.salary) AS avg_salary
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
GROUP BY d.department_name
ORDER BY avg_salary DESC;

-- Avoid: Unclear, no comments, poor formatting
select d.department_name,avg(e.salary) from employees e inner join departments d on e.department_id=d.id group by d.department_name;
```

#### Lab Structure
Each lab should include:
1. **Title** - Clear, descriptive title
2. **Learning Objectives** - What students will learn
3. **Prerequisites** - Required knowledge
4. **Introduction** - Concept overview
5. **Step-by-step instructions** - Clear guidance
6. **Exercises** - Practice problems
7. **Solutions** - Example answers (in collapsible sections)
8. **Additional Resources** - Further reading

#### Markdown Files
- Use **clear headings** (h1 for title, h2 for sections, h3 for subsections)
- Include **code blocks** with syntax highlighting
- Add **tables** for structured data
- Use **lists** for sequential steps
- Include **images** when helpful (store in /images directory)

### Code Examples

#### Python
```python
# Good: Clear, documented, error handling
import mysql.connector
from mysql.connector import Error

def connect_to_database(host, database, user, password):
    """
    Establish connection to MySQL database.
    
    Args:
        host: Database host address
        database: Database name
        user: Username
        password: Password
    
    Returns:
        connection object or None
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        if connection.is_connected():
            print("Successfully connected to database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None
```

#### Java
```java
// Good: Clear, documented, resource management
public class DatabaseConnection {
    /**
     * Creates a connection to MySQL database
     * 
     * @param url JDBC connection URL
     * @param user Database username
     * @param password Database password
     * @return Connection object
     * @throws SQLException if connection fails
     */
    public static Connection getConnection(String url, String user, String password) 
            throws SQLException {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            return DriverManager.getConnection(url, user, password);
        } catch (ClassNotFoundException e) {
            throw new SQLException("MySQL JDBC Driver not found", e);
        }
    }
}
```

### Dataset Guidelines
When contributing datasets:
- Use **realistic, educational data**
- Include **diverse examples**
- Provide **data dictionary** explaining columns
- **Anonymize** any potentially sensitive information
- Include **schema creation scripts**
- Keep file sizes **reasonable** (< 10MB preferred)

### Documentation
- Write in **clear, simple English**
- Assume **beginner level knowledge** unless stated otherwise
- Include **examples** for complex concepts
- Link to **external resources** when helpful
- Keep content **up to date**

## Style Guidelines

### SQL Style
```sql
-- Keywords in UPPERCASE
SELECT column1, column2
FROM table_name
WHERE condition = value;

-- Indentation for readability
SELECT 
    t1.column1,
    t2.column2,
    COUNT(*) AS count
FROM table1 t1
INNER JOIN table2 t2 ON t1.id = t2.foreign_id
WHERE t1.status = 'active'
GROUP BY t1.column1, t2.column2
HAVING COUNT(*) > 5
ORDER BY count DESC;

-- Comments for complex logic
-- Calculate running total using window function
SELECT 
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) AS running_total
FROM transactions;
```

### Markdown Style
- Use ATX-style headers (#)
- Leave blank line before and after headers
- Use fenced code blocks with language specification
- Use `inline code` for code references in text
- Use **bold** for emphasis, *italic* for slight emphasis
- Keep line length reasonable (80-120 characters)

### File Naming
- Use lowercase
- Use hyphens for spaces
- Be descriptive
- Examples:
  - `getting-started.md`
  - `lab-window-functions.md`
  - `exercise-solutions.sql`

## Commit Message Guidelines

### Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- **feat**: New feature or lab
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Formatting, no code change
- **refactor**: Code refactoring
- **test**: Adding tests
- **chore**: Maintenance tasks

### Examples
```
feat(lab4): Add window functions exercises

Added 5 new exercises covering ROW_NUMBER, RANK, and DENSE_RANK
functions with solutions.

Closes #123

---

fix(lab2): Correct SQL syntax in JOIN example

Changed 'INNER JOUN' to 'INNER JOIN' in example query.

---

docs(readme): Update installation instructions

Added troubleshooting section for common MySQL connection issues.
```

### Subject Line
- Use imperative mood ("Add" not "Added")
- Don't capitalize first letter
- No period at the end
- Limit to 50 characters

### Body
- Explain what and why, not how
- Wrap at 72 characters
- Separate from subject with blank line

## Pull Request Process

### Before Submitting
1. ✅ **Test your changes** thoroughly
2. ✅ **Run all affected SQL scripts** to ensure they work
3. ✅ **Check for typos** and grammatical errors
4. ✅ **Update documentation** if needed
5. ✅ **Add yourself** to reports/CONTRIBUTORS.md (if first contribution)

### PR Description
Include:
- **Summary** of changes
- **Motivation** - Why is this change needed?
- **Testing** - How was it tested?
- **Screenshots** - If applicable (UI changes)
- **Related issues** - Link with "Closes #issue_number"

### Example PR
```markdown
## Description
Added 3 new exercises to Lab 5 covering advanced subquery techniques.

## Motivation
Students requested more practice problems for correlated subqueries
and EXISTS/NOT EXISTS operations.

## Changes
- Added Exercise 6: Correlated subquery with aggregates
- Added Exercise 7: EXISTS vs IN comparison
- Added Exercise 8: NOT EXISTS with multiple conditions
- Included solutions for all exercises

## Testing
- All SQL queries tested on MySQL 8.0.27
- Verified queries work with provided sample data
- Checked markdown rendering on GitHub

## Related Issues
Closes #45
```

### Review Process
1. Maintainer will review your PR
2. May request changes or clarifications
3. Once approved, PR will be merged
4. Your contribution will be acknowledged

### After Merge
1. Delete your branch
2. Pull latest changes from upstream
3. Consider contributing again!

## Recognition

### Contributors
All contributors are listed in [reports/CONTRIBUTORS.md](../reports/CONTRIBUTORS.md)

### Significant Contributions
Major contributions may be highlighted in:
- Repository README
- Release notes
- Project announcements

## Questions?

### Getting Help
- Open an issue for questions
- Check existing issues and documentation first
- Be patient - maintainers are volunteers

### Contact
- GitHub Issues: [Create an issue](https://github.com/TeachingOW/DBMS-SQL-Labs/issues)
- Discussions: [GitHub Discussions](https://github.com/TeachingOW/DBMS-SQL-Labs/discussions)

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

**Thank you for contributing to DBMS-SQL-Labs! Your efforts help students worldwide learn database concepts effectively.** 🎓
