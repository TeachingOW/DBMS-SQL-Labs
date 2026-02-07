# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-02-07 (s26 Branch)

### 🎉 Major Release: Enhanced Documentation and Organization

This release represents a major overhaul of the repository structure and documentation, making it significantly more accessible and organized for learners and instructors.

### Added

#### 📚 Comprehensive Documentation
- **Getting Started Guide** (`docs/GETTING_STARTED.md`)
  - Complete setup instructions for MySQL, Python, Java, Node.js
  - Troubleshooting section for common issues
  - Quick start guides for different skill levels
  - Tool installation guides for MongoDB, Neo4j, Jupyter
  
- **Course Syllabus** (`docs/COURSE_SYLLABUS.md`)
  - 16-week structured curriculum
  - Weekly schedule with topics and labs
  - Grading policy and assessment guidelines
  - Project ideas and deliverables
  - Learning outcomes for each module
  
- **SQL Cheat Sheet** (`docs/SQL_CHEAT_SHEET.md`)
  - Comprehensive reference for all SQL commands
  - Organized by topic (DDL, DML, Queries, Joins, etc.)
  - Code examples for every command
  - Best practices and performance tips
  - Window functions and CTEs reference
  
- **Contributing Guide** (`docs/CONTRIBUTING.md`)
  - Detailed contribution guidelines
  - Code style standards for SQL, Python, Java
  - Pull request process
  - Issue reporting templates
  - Commit message conventions
  
- **Lab Index** (`LAB_INDEX.md`)
  - Complete catalog of all 21 labs
  - Detailed descriptions with learning objectives
  - Prerequisites for each lab
  - Duration estimates
  - Difficulty levels (Beginner to Expert)
  - Multiple learning paths
  
- **Practice Exercises** (`exercises/PRACTICE_EXERCISES.md`)
  - Additional exercises by topic
  - Challenge problems for advanced learners
  - Difficulty ratings
  - Links to external practice platforms
  
- **Project Roadmap** (`docs/ROADMAP.md`)
  - Short, medium, and long-term goals
  - Feature development timeline
  - Success metrics
  - How to contribute to roadmap

#### 🗂️ Repository Organization
- Created `/labs` directory structure
  - `/labs/html_labs` - All HTML lab files organized
  - `/labs/notebooks` - Jupyter notebook labs
  - `/labs/code` - Programming examples
  
- Created `/docs` directory for documentation
- Created `/exercises` directory for practice problems
- Created `/solutions` directory (structure for future solutions)
- Created `/supplementary` directory (for additional materials)

#### ✨ Enhanced Features
- Added badges to README (stars, license, PRs welcome)
- Quick links section in README
- Learning paths for different skill levels
- Search by topic in Lab Index
- Multiple ways to navigate content

### Changed

#### 📝 README Improvements
- Restructured for better navigation
- Added Quick Links section at the top
- Updated lab references to use new structure
- Added highlights for featured labs (⭐)
- Improved descriptions and organization
- Added "How to Use This Repository" section

#### 🔧 Configuration
- Enhanced `.gitignore` file
  - Exclude Mac .DS_Store files
  - Exclude Python cache files
  - Exclude node_modules
  - Exclude IDE files
  - Exclude credentials and secrets

### Improved

- Better cross-referencing between documents
- Consistent formatting across all markdown files
- More descriptive file names
- Improved accessibility with clear hierarchy
- Better onboarding for new contributors
- Enhanced discoverability of resources

### Fixed

- Fixed CASE Expressions lab link in README
- Corrected file path references
- Improved consistency in documentation style

---

## [1.0.0] - Initial Release

### Added
- 21 comprehensive SQL labs covering:
  - Database Creation & Basic Queries
  - Advanced Queries & Joins
  - Foreign Keys & Relationships
  - Multi-Table Operations
  - Set Operations & Nested Queries
  - Aggregate Functions & Grouping
  - CASE Expressions
  - Window Functions & Recursive Queries
  - Views & Virtual Tables
  - Database Normalization
  - Advanced SQL Techniques
  - Java Database Interface
  - Python Database Interface
  - Jupyter Notebook Integration
  - Analytical Functions (ROLLUP, CUBE)
  - Triggers & Stored Procedures
  - Transaction Management
  - Isolation Levels
  - JSON & XML Processing
  - MongoDB (NoSQL)
  - Neo4j (Graph Database)

- Dataset Files:
  - IMDB Movie Data
  - Air Travel Data
  - Cities Data
  - Employee Data
  - Student Grades
  - Drivers Database

- Code Examples:
  - Node.js database integration
  - Express.js server examples
  - JavaScript client code

- Jupyter Notebooks:
  - MySQL-Jupyter integration
  - ROLLUP examples
  - Triggers examples

- Supplementary Materials:
  - In-Class Exercise (Workers Database)
  - CASE Expression detailed guide (markdown)
  - Bank triggers assignment
  - ORM introduction document

- Basic Documentation:
  - README with lab overview
  - GitHub Pages site

---

## Upcoming Changes (Planned)

### Version 2.1 (Next Minor Release)
- [ ] Convert HTML labs to Markdown format
- [ ] Add solution guides for all exercises
- [ ] Create video tutorial links
- [ ] Add assessment rubrics

### Version 3.0 (Next Major Release)
- [ ] Interactive SQL playground
- [ ] Auto-grading system
- [ ] Video content for each lab
- [ ] Multi-language support

---

## Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for details on how to contribute to this changelog.

---

## Links

- [Repository](https://github.com/TeachingOW/DBMS-SQL-Labs)
- [Website](https://teachingow.github.io/DBMS-SQL-Labs/)
- [Issues](https://github.com/TeachingOW/DBMS-SQL-Labs/issues)
- [Pull Requests](https://github.com/TeachingOW/DBMS-SQL-Labs/pulls)

---

**Note**: All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/).
