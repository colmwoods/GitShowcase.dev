# [GitShowcase.dev](https://gitshowcase-dev-a0b7673e36ce.herokuapp.com)

Developer: Colm Woods ([colmwoods](https://www.github.com/colmwoods))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/colmwoods/GitShowcase.dev)](https://www.github.com/colmwoods/GitShowcase.dev/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/colmwoods/GitShowcase.dev)](https://www.github.com/colmwoods/GitShowcase.dev/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/colmwoods/GitShowcase.dev)](https://www.github.com/colmwoods/GitShowcase.dev)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://gitshowcase-dev-a0b7673e36ce.herokuapp.com)

## Project Introduction and Rationale

**GitShowcase.dev** is a full-stack Django web application that enables developers to showcase their GitHub repositories dynamically. It connects via **GitHub OAuth**, allowing users to authenticate securely and automatically display their repositories with metadata such as description, language, stars, and update date. Each repository card includes **interactive features** like view, download, fork, star, bookmark, and comment.

The platform also includes a **search function** to explore other developers’ profiles, a detailed **About page** describing the project, and a **404 page** for handling invalid URLs gracefully.

This project was created by **Colm Woods** as part of a professional developer portfolio system to make sharing GitHub projects easier for developers and more accessible for recruiters. The goal is to combine automation, design, and usability into one cohesive platform that visually presents open-source work.

![screenshot](documentation/mockup.png)

source: [GitShowcase.dev amiresponsive](https://ui.dev/amiresponsive?url=https://gitshowcase-dev-a0b7673e36ce.herokuapp.com)

## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**
- Give developers an elegant platform to display GitHub repositories.
- Provide a search interface for discovering other developers and their work.
- Encourage community engagement through commenting and bookmarking.

**Primary User Needs**
- Developers want their GitHub projects to automatically sync and display.
- Visitors and recruiters want to search, view, and evaluate repositories.
- Users want an intuitive interface to interact through bookmarking and commenting.

**Business Goals**
- Deliver a professional portfolio showcase for developers.
- Support interactivity to increase engagement.
- Demonstrate full-stack Django development with GitHub API integration.

#### 2. Scope

**Features**
- GitHub OAuth authentication.
- Automatic repository fetching and live updates.
- Interactive repo actions (View, Download, Fork, Star, Bookmark, Comment).
- About page with project and author details.
- Search functionality for viewing other users’ profiles.
- 404 page for invalid routes.

#### 3. Structure

**Information Architecture**
- **Navigation:** Home, Search, About, Login/Logout.
- **User Flow:**
  1. User logs in via GitHub OAuth.
  2. Their repositories are fetched automatically.
  3. Repos display with interactive buttons and comments.
  4. Users can view, fork, download, or bookmark repos.
  5. Comments can be added, edited, or deleted.
  6. The star button toggles between **Star** and **Starred**, providing clear visual feedback.
  7. Visitors can search for other developers.
  8. The About page gives info about GitShowcase.dev.
  9. Invalid pages show a styled 404 error page.

#### 4. Skeleton

Wireframes were created to ensure a responsive, clean, and intuitive interface for mobile, tablet, and desktop.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/wireframes/mobile-home.png) | ![screenshot](documentation/wireframes/tablet-home.png) | ![screenshot](documentation/wireframes/desktop-home.png) |
| Profile | ![screenshot](documentation/wireframes/mobile-profile.png) | ![screenshot](documentation/wireframes/tablet-profile.png) | ![screenshot](documentation/wireframes/desktop-profile.png) |
| Search | ![screenshot](documentation/wireframes/mobile-search.png) | ![screenshot](documentation/wireframes/tablet-search.png) | ![screenshot](documentation/wireframes/desktop-search.png) |
| About | ![screenshot](documentation/wireframes/mobile-about.png) | ![screenshot](documentation/wireframes/tablet-about.png) | ![screenshot](documentation/wireframes/desktop-about.png) |
| 404 | ![screenshot](documentation/wireframes/mobile-404.png) | ![screenshot](documentation/wireframes/tablet-404.png) | ![screenshot](documentation/wireframes/desktop-404.png) |

#### 5. Surface

**Colour Scheme**

I used [coolors.co](https://coolors.co/080708-3772ff-df2935-fdca40-e6e8e6) to generate my color palette.

- `#080708` — Background.
- `#3772FF` — Primary accent.
- `#DF2935` — Errors / warnings.
- `#FDCA40` — Highlights.
- `#E6E8E6` — Text.

**Typography**
- [Montserrat](https://fonts.google.com/specimen/Montserrat) — Headers.
- [Lato](https://fonts.google.com/specimen/Lato) — Body text.
- [Font Awesome](https://fontawesome.com) — Icons.

## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a developer | I want to log in using GitHub OAuth | so that I can connect my account securely. |
| As a developer | I want my repositories displayed automatically | so that I don’t have to update my portfolio manually. |
| As a developer | I want to bookmark repositories | so that I can revisit projects that interest me. |
| As a user | I want to download repositories | so that I can explore code locally. |
| As a user | I want to fork repositories | so that I can contribute to open-source work. |
| As a user | I want to leave comments | so that I can give feedback on others’ work. |
| As a user | I want to edit or delete my own comments | to maintain control over my feedback. |
| As a visitor | I want to view developer profiles | to explore their repositories. |
| As a visitor | I want to read the About page | to understand the purpose of GitShowcase.dev. |
| As a visitor | I want to see a custom 404 page | when I visit an invalid URL. |
| As a user | I want clear visual feedback when starring or unstarring a repository | so that I know my action was successful. |

## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| GitHub OAuth Login | Authenticates users through GitHub’s secure OAuth system. | ![screenshot](documentation/features/oauth.png) |
| Repository Display | Dynamically fetches and shows user repositories with language, stars, and update date. | ![screenshot](documentation/features/repos.png) |
| Interactive Buttons | Each repo card includes **View**, **Download**, **Fork**, **Starred**, **Bookmark**, and **Comment** buttons. The **Star** button toggles in real time, changing between `Star` and `Starred` to indicate the user’s action clearly. | ![screenshot](documentation/features/repo-card.png) |
| Comment System | Users can comment, edit, or delete feedback on any repository. | ![screenshot](documentation/features/comments.png) |
| Search Function | Allows users to find and view other developers’ profiles. | ![screenshot](documentation/features/search.png) |
| About Page | Provides project details, purpose, and credits. | ![screenshot](documentation/features/about.png) |
| 404 Page | Displays a friendly error message for invalid URLs. | ![screenshot](documentation/features/404.png) |
| Responsive Design | Optimized across mobile, tablet, and desktop. | ![screenshot](documentation/features/responsive.png) |
| Heroku Deployment | Fully deployed via Heroku. | ![screenshot](documentation/features/heroku.png) |

### Future Features

- User profile customization (bio, avatar, pinned repos).
- Dark/light mode toggle.
- Sorting repositories by stars, forks, or language.
- Email notifications for new comments.
- Recruiter account type for saved profiles.
- Analytics dashboard for user interactions.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [Git](https://git-scm.com) | Version control. |
| [GitHub](https://github.com) | Code hosting. |
| [VSCode](https://code.visualstudio.com) | Development environment. |
| [HTML](https://en.wikipedia.org/wiki/HTML) | Structure. |
| [CSS](https://en.wikipedia.org/wiki/CSS) | Styling. |
| [JavaScript](https://www.javascript.com) | Interactivity. |
| [Bootstrap](https://getbootstrap.com) | Responsive design. |
| [Python](https://www.python.org) | Backend logic. |
| [Django](https://www.djangoproject.com) | Web framework. |
| [PostgreSQL](https://www.postgresql.org) | Database. |
| [Heroku](https://www.heroku.com) | Deployment. |
| [Font Awesome](https://fontawesome.com) | Icons. |
| [ChatGPT](https://chat.openai.com) | Documentation and debugging support. |

## Testing

See [TESTING.md](TESTING.md) for testing details.

## Deployment

Deployed on [Heroku](https://gitshowcase-dev-a0b7673e36ce.herokuapp.com).

### Environment Variables
| Key | Description |
| --- | --- |
| `DATABASE_URL` | PostgreSQL connection string |
| `SECRET_KEY` | Django secret key |
| `GITHUB_CLIENT_ID` | GitHub OAuth client ID |
| `GITHUB_CLIENT_SECRET` | GitHub OAuth secret key |

### Local Setup
```bash
git clone https://www.github.com/colmwoods/GitShowcase.dev.git
cd GitShowcase.dev
pip3 install -r requirements.txt
python3 manage.py runserver
```
Visit `http://localhost:8000` in your browser.

## Credits

### Content
- [GitHub API](https://docs.github.com/en/rest) — Repository data.
- [Bootstrap](https://getbootstrap.com) — Components and layout.
- [Font Awesome](https://fontawesome.com) — Icons.
- [Markdown Builder](https://markdown.2bn.dev) — README base template.

### Media
- [favicon.io](https://favicon.io) — Favicon generator.
- [Unsplash](https://unsplash.com) — Placeholder images.

### Acknowledgements
- [Tim Nelson](https://github.com/TravelTimN) — Code Institute mentor support.
- Code Institute Tutor and Slack teams.
- My partner for continuous encouragement and support.