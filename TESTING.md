# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

This document outlines all testing carried out on **GitShowcase.dev**, including code validation, responsiveness checks, browser compatibility testing, Lighthouse audits, defensive programming tests, and user story validation. All tests were performed on the deployed Heroku version to ensure accurate results aligned with real user interactions.

Throughout development, testing played a central role in verifying that each feature behaved as expected — from GitHub OAuth authentication, to repository listing, bookmarking, commenting, searching users, and interacting with the GitHub API.

Where relevant, screenshots are provided to demonstrate successful testing outcomes, and any issues that arose during development have been documented in the Bugs section.

---

## Code Validation

The following sections detail validation of all **HTML**, **CSS**, **JavaScript**, and **Python** files included in the project.  
Only files written or modified by me have been validated — external libraries such as Bootstrap and Django Allauth are excluded, as they are maintained by third parties.

Each validator was used according to its recommended method:

- **HTML** — validated using W3C Validator (live URL or compiled HTML via View Page Source).  
- **CSS** — validated using W3C Jigsaw Validator (live URL).  
- **JavaScript** — validated using JSHint with ES6 enabled.  
- **Python** — validated using the PEP8 CI Linter.

This ensures the codebase adheres to correct syntax, readability standards, and best practices.

### HTML Validation

I have used the recommended **[HTML W3C Validator](https://validator.w3.org)** to validate all HTML files across the GitShowcase.dev project. Since this is a Django application that includes template tags such as `{% url %}`, `{% for %}`, and `{{ variables }}`, these files cannot be validated directly when pasted into the validator.

To ensure accurate validation:

- Public pages were validated using the **Validate by URL** method on the deployed Heroku site.
- Templates requiring authentication (such as bookmarks or comment-related views) were opened on the deployed site while logged in, and the compiled HTML was obtained through the browser’s **View Page Source**. This HTML was then validated using the **Validate by Direct Input** option.
- Templates not reachable by URL (such as `base.html` or include components like `repo_card.html`) were validated by manually reviewing their rendered HTML output within the browser tools and validating the copied HTML.

This ensured every template was validated in its final rendered form, free of Django/Jinja syntax.

### HTML Validation Results

| Directory | File | URL | Screenshot | Notes |
|----------|------|-----|-----------|-------|
| templates | about.html | https://gitshowcase-dev-a0b7673e36ce.herokuapp.com/about | ![screenshot](documentation/validation/html-about.jpg) | Static About page describing the platform and its purpose |
| templates | bookmarks.html | https://gitshowcase-dev-a0b7673e36ce.herokuapp.com/bookmarks | ![screenshot](documentation/validation/html-bookmarks.jpg) | Displays the authenticated user’s bookmarked repositories |
| templates | home.html | https://gitshowcase-dev-a0b7673e36ce.herokuapp.com/ | ![screenshot](documentation/validation/html-home.jpg) | Main homepage showing repositories retrieved from the GitHub API |
| templates | search.html | https://gitshowcase-dev-a0b7673e36ce.herokuapp.com/search | ![screenshot](documentation/validation/html-search.jpg) | GitHub user search page allowing exploration of other profiles |
| templates | 404.html | Not accessible directly | ![screenshot](documentation/validation/html-404.jpg) | Custom 404 page; validated via “View Page Source” |
| templates | base.html | No live link (layout template) | ![screenshot](documentation/validation/html-base.jpg) | Master base template providing layout, navigation, and footer for all pages, Tested by removing django blocks and pasting into validator |
| templates/includes | repo_card.html | No live link (include file) | ![screenshot](documentation/validation/html-repo_card.jpg) | Reusable card component for displaying repository metadata, Tested by removing django blocks and pasting into validator |
| templates/account | login.html | https://gitshowcase-dev-a0b7673e36ce.herokuapp.com/accounts/login | ![screenshot](documentation/validation/html-login.jpg) | GitHub OAuth login page |
| templates/form | contact.html | https://gitshowcase-dev-a0b7673e36ce.herokuapp.com/contact | ![screenshot](documentation/validation/html-contact.jpg) | Contact form that stores messages in the database |
| templates/form | success.html | https://gitshowcase-dev-a0b7673e36ce.herokuapp.com/success | ![screenshot](documentation/validation/html-success.jpg) | Confirmation page displayed after a successful contact form submission |


## CSS Validation

I have used the recommended **[W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/)** to validate the custom CSS used in GitShowcase.dev. The project uses a single custom stylesheet (`style.css`) alongside external libraries such as Bootstrap. Only my own CSS was validated; external framework stylesheets are not required to be checked.

The deployed CSS file was validated using the **Validate by URL** method to ensure the production version matched the validated output.

### CSS Validation Results

| Directory | File | URL | Screenshot | Notes |
|----------|------|-----|-----------|-------|
| static/css | style.css | https://gitshowcase-dev-a0b7673e36ce.herokuapp.com/static/css/style.css | ![screenshot](documentation/validation/css-style.jpg) | Main custom stylesheet controlling layout, typography, colour scheme, and components across the site |


## JavaScript Validation

I have used the recommended **[JSHint](https://jshint.com)** tool to validate all JavaScript files in the project. The validator was configured to support modern JavaScript (ES6+). Any warnings related to external globals (such as objects provided by the browser, Django templates, or API responses) were reviewed and considered acceptable where they related to external dependencies rather than issues in my own code.

Both scripts focus on enhancing user interaction for starring repositories and working with comments on the front end.

### JavaScript Validation Results

| Directory | File | URL | Screenshot | Notes |
|----------|------|-----|-----------|-------|
| static/js | comment.js | Included via base template; no direct URL | ![screenshot](documentation/validation/js-comment.jpg) | Handles client-side behaviour for comment interactions, such as toggling forms or improving UX around comment actions |
| static/js | star.js | Included via base template; no direct URL | ![screenshot](documentation/validation/js-star.jpg) | Manages the star/unstar UI behaviour and communicates with the backend logic tied to GitHub star actions |


## Python Validation

I have used the recommended **[PEP8 CI Python Linter](https://pep8ci.herokuapp.com)** to validate all Python files that I created or modified for GitShowcase.dev. This includes core Django project files, views, models, forms, and configuration modules.

Auto-generated Django files located in `migrations/` and `__pycache__/` were intentionally excluded from validation.  
Where Django’s default configuration resulted in very long lines (for example, some password validator settings in `settings.py`), the `# noqa` comment was added sparingly and only when line-breaking would negatively impact readability or functionality.

### Python Validation Results

| Directory | File | URL | Screenshot | Notes |
|----------|------|-----|-----------|-------|
| gitshowcase/templatetags | extra_tags.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/GitShowcase.dev/main/gitshowcase/extra_tags.py) | ![screenshot](documentation/validation/py-extra-tags.jpg) | Custom Django template filter used to safely access dictionary values in templates |
| gitshowcase | admin.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/GitShowcase.dev/main/gitshowcase/admin.py) | ![screenshot](documentation/validation/py-admin.jpg) | Registers models with the Django admin interface |
| gitshowcase | asgi.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/GitShowcase.dev/main/gitshowcase/asgi.py) | ![screenshot](documentation/validation/py-asgi.jpg) | Standard ASGI configuration for async deployment |
| gitshowcase | forms.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/GitShowcase.dev/main/gitshowcase/forms.py) | ![screenshot](documentation/validation/py-forms.jpg) | Contains the contact form and any related form logic |
| gitshowcase | models.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/GitShowcase.dev/main/gitshowcase/models.py) | ![screenshot](documentation/validation/py-models.jpg) | Defines core models such as Repository, Bookmark, Comment, and Contact |
| gitshowcase | settings.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/GitShowcase.dev/main/gitshowcase/settings.py) | ![screenshot](documentation/validation/py-settings.jpg) | Project configuration, including installed apps, middleware, database, and third-party integrations |
| gitshowcase | urls.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/GitShowcase.dev/main/gitshowcase/urls.py) | ![screenshot](documentation/validation/py-urls.jpg) | URL routing for the main pages (home, bookmarks, search, about, contact, etc.) |
| gitshowcase | views.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/GitShowcase.dev/main/gitshowcase/views.py) | ![screenshot](documentation/validation/py-views.jpg) | Implements application logic for fetching GitHub data, handling bookmarks, comments, search, and page rendering |
| gitshowcase | wsgi.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/GitShowcase.dev/main/gitshowcase/wsgi.py) | ![screenshot](documentation/validation/py-wsgi.jpg) | Standard WSGI configuration used by the production server |
| root | manage.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/colmwoods/GitShowcase.dev/main/manage.py) | ![screenshot](documentation/validation/py-manage.jpg) | Django management script used to run commands such as migrations, tests, and starting the development server |

---

## Responsiveness

All publicly accessible pages of GitShowcase.dev were tested for responsiveness using:

- **Chrome DevTools Device Emulator**
- **Safari Responsive Design Mode**
- **Actual physical devices** (iPhone 12, Samsung Galaxy A52, iPad 10th gen)
- Screen sizes between **320px and 1920px**

The Bootstrap grid system, custom CSS, and component layout were checked to ensure consistent rendering across mobile, tablet, and desktop breakpoints.

Every page was verified for:

- Proper text scaling  
- No horizontal scrolling  
- Correct card/grid wrapping  
- Navigation collapsing correctly on mobile  
- Buttons and forms remaining accessible and sized correctly  
- Images and repository cards maintaining alignment

### Aesthetic Multi-Device Mockup

To visually demonstrate how GitShowcase.dev appears across multiple devices, I generated a responsive mockup using **ami.responsivedesign.is**.

![screenshot](documentation/mockup.jpg)

*Note: This mockup is for presentation only. All formal responsiveness testing was carried out using physical devices and developer tools, as shown in the table below.*

I've tested my deployed project to check for responsiveness issues.
To ensure consistent behaviour across key device categories, three standard screen sizes were used as primary responsiveness checkpoints:

- **Mobile:** 375 × 812 px (iPhone 12 baseline)
- **Tablet:** 768 × 1024 px (iPad portrait)
- **Laptop/Desktop:** 1440 × 900 px (MacBook Air/Pro baseline)

> **Authentication Notice:**  
> Several pages included in this responsiveness testing — such as Bookmarks, Search Users, and any GitHub-integrated features — require the user to be logged in.  
> Because of this, these pages are not accessible to the public without authentication.  
> All screenshots and tests were carried out while logged in to ensure that both public and private areas of the platform behave consistently across all screen sizes.

| Page | Mobile | Tablet | Desktop | Notes |
|------|--------|--------|---------|--------|
| Home | ![screenshot](documentation/responsiveness/mobile-home.jpg) | ![screenshot](documentation/responsiveness/tablet-home.jpg) | ![screenshot](documentation/responsiveness/desktop-home.jpg) | Repository cards stack correctly on mobile and expand into grid layout on larger screens |
| About | ![screenshot](documentation/responsiveness/mobile-about.jpg) | ![screenshot](documentation/responsiveness/tablet-about.jpg) | ![screenshot](documentation/responsiveness/desktop-about.jpg) | Text and spacing scale evenly across all screen sizes |
| Bookmarks | ![screenshot](documentation/responsiveness/mobile-bookmarks.jpg) | ![screenshot](documentation/responsiveness/tablet-bookmarks.jpg) | ![screenshot](documentation/responsiveness/desktop-bookmarks.jpg) | Bookmark cards reflow correctly and stay aligned |
| Search Users | ![screenshot](documentation/responsiveness/mobile-search.jpg) | ![screenshot](documentation/responsiveness/tablet-search.jpg) | ![screenshot](documentation/responsiveness/desktop-search.jpg) | Search bar and user result listings remain centred and responsive |
| Contact | ![screenshot](documentation/responsiveness/mobile-contact.jpg) | ![screenshot](documentation/responsiveness/tablet-contact.jpg) | ![screenshot](documentation/responsiveness/desktop-contact.jpg) | Form inputs adjust properly with the screen size |
| Contact Success | ![screenshot](documentation/responsiveness/mobile-success.jpg) | ![screenshot](documentation/responsiveness/tablet-success.jpg) | ![screenshot](documentation/responsiveness/desktop-success.jpg) | Confirmation message stays centred and readable on all devices |
| Login | ![screenshot](documentation/responsiveness/mobile-login.jpg) | ![screenshot](documentation/responsiveness/tablet-login.jpg) | ![screenshot](documentation/responsiveness/desktop-login.jpg) | GitHub login button displays centrally and remains touch-friendly |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.jpg) | ![screenshot](documentation/responsiveness/tablet-404.jpg) | ![screenshot](documentation/responsiveness/desktop-404.jpg) | Error message and navigation button remain fully responsive |

---

## Browser Compatibility

The deployed version of GitShowcase.dev was tested across multiple browsers to ensure consistent rendering, layout behaviour, interaction, and performance. Each page was reviewed on the latest stable releases of **Google Chrome**, **Mozilla Firefox**, **Apple Safari**, **Opera**, and **Microsoft Edge**.

Screenshots were taken on all five browsers to demonstrate compatibility and confirm that GitHub OAuth login, repository cards, bookmarks, comments, forms, and search functionality behave consistently.

| Page | Chrome | Firefox | Safari | Opera | Edge | Notes |
|------|--------|---------|--------|--------|--------|--------|
| Home | ![screenshot](documentation/browsers/chrome-home.jpg) | ![screenshot](documentation/browsers/firefox-home.jpg) | ![screenshot](documentation/browsers/safari-home.jpg) | ![screenshot](documentation/browsers/opera-home.jpg) | ![screenshot](documentation/browsers/edge-home.jpg) | Repository cards and layout behave consistently across browsers |
| About | ![screenshot](documentation/browsers/chrome-about.jpg) | ![screenshot](documentation/browsers/firefox-about.jpg) | ![screenshot](documentation/browsers/safari-about.jpg) | ![screenshot](documentation/browsers/opera-about.jpg) | ![screenshot](documentation/browsers/edge-about.jpg) | Static about page displays correctly on all platforms |
| Bookmarks | ![screenshot](documentation/browsers/chrome-bookmarks.jpg) | ![screenshot](documentation/browsers/firefox-bookmarks.jpg) | ![screenshot](documentation/browsers/safari-bookmarks.jpg) | ![screenshot](documentation/browsers/opera-bookmarks.jpg) | ![screenshot](documentation/browsers/edge-bookmarks.jpg) | Bookmark functionality and card layout work consistently |
| Search Users | ![screenshot](documentation/browsers/chrome-search.jpg) | ![screenshot](documentation/browsers/firefox-search.jpg) | ![screenshot](documentation/browsers/safari-search.jpg) | ![screenshot](documentation/browsers/opera-search.jpg) | ![screenshot](documentation/browsers/edge-search.jpg) | Search bar and user listings behave the same across browsers |
| Contact | ![screenshot](documentation/browsers/chrome-contact.jpg) | ![screenshot](documentation/browsers/firefox-contact.jpg) | ![screenshot](documentation/browsers/safari-contact.jpg) | ![screenshot](documentation/browsers/opera-contact.jpg) | ![screenshot](documentation/browsers/edge-contact.jpg) | Form fields render consistently and submit correctly |
| Contact Success | ![screenshot](documentation/browsers/chrome-success.jpg) | ![screenshot](documentation/browsers/firefox-success.jpg) | ![screenshot](documentation/browsers/safari-success.jpg) | ![screenshot](documentation/browsers/opera-success.jpg) | ![screenshot](documentation/browsers/edge-success.jpg) | Confirmation message displays correctly on all browsers |
| Login | ![screenshot](documentation/browsers/chrome-login.jpg) | ![screenshot](documentation/browsers/firefox-login.jpg) | ![screenshot](documentation/browsers/safari-login.jpg) | ![screenshot](documentation/browsers/opera-login.jpg) | ![screenshot](documentation/browsers/edge-login.jpg) | GitHub OAuth login button displays properly across all browsers |
| 404 | ![screenshot](documentation/browsers/chrome-404.jpg) | ![screenshot](documentation/browsers/firefox-404.jpg) | ![screenshot](documentation/browsers/safari-404.jpg) | ![screenshot](documentation/browsers/opera-404.jpg) | ![screenshot](documentation/browsers/edge-404.jpg) | Custom error page remains fully compatible |


All tested browsers displayed the site properly with identical behaviour across all interactive elements.

---

## Lighthouse Audit

The deployed GitShowcase.dev application was tested using **Google Lighthouse** within Chrome DevTools. Each page was tested for both **mobile** and **desktop** to evaluate accessibility, performance, SEO, and best-practice compliance.

Mobile scores tend to be lower due to GitHub API requests, external fonts, and the use of third-party assets, which is expected and typical for API-driven applications. Desktop results generally show higher scores.

I am running these lighthouse tests in incognito mode as chrome extentions and more can have an impact on final

| Page | Mobile | Desktop |
|------|--------|---------|
| Home | ![screenshot](documentation/lighthouse/mobile-home.jpg) | ![screenshot](documentation/lighthouse/desktop-home.jpg) |
| About | ![screenshot](documentation/lighthouse/mobile-about.jpg) | ![screenshot](documentation/lighthouse/desktop-about.jpg) |
| Bookmarks | ![screenshot](documentation/lighthouse/mobile-bookmarks.jpg) | ![screenshot](documentation/lighthouse/desktop-bookmarks.jpg) |
| Search Users | ![screenshot](documentation/lighthouse/mobile-search.jpg) | ![screenshot](documentation/lighthouse/desktop-search.jpg) |
| Contact | ![screenshot](documentation/lighthouse/mobile-contact.jpg) | ![screenshot](documentation/lighthouse/desktop-contact.jpg) |
| Contact Success | ![screenshot](documentation/lighthouse/mobile-success.jpg) | ![screenshot](documentation/lighthouse/desktop-success.jpg) |
| Login | ![screenshot](documentation/lighthouse/mobile-login.jpg) | ![screenshot](documentation/lighthouse/desktop-login.jpg) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.jpg) | ![screenshot](documentation/lighthouse/desktop-404.jpg) |

All audited pages returned results within expected ranges, with no critical accessibility or best-practice issues detected. Minor performance warnings relate primarily to external GitHub API calls and third-party content, which are outside the project's control.

---

## Defensive Programming

Defensive programming was a critical part of building GitShowcase.dev due to the amount of user interaction, external API calls, and authenticated features. The platform integrates GitHub OAuth, stores user-generated comments, manages personalised bookmarks, and handles user searches, form submissions, and repository interactions. Because of this, strict validation, permission checks, and safe error handling were essential throughout development.

The main goals of defensive programming in this project were:

- **Prevent unauthorised access** to features that require GitHub authentication  
- **Ensure users can only modify their own data**, including bookmarks and comments  
- **Validate all form inputs** to protect from invalid or malicious submissions  
- **Handle URL manipulation safely**, preventing users from accessing or changing content through crafted URLs  
- **Protect against API misuse**, ensuring actions like starring/un-starring can only occur when authenticated  
- **Provide clear feedback and safe fallbacks**, avoiding crashes or unhandled exceptions  
- **Maintain data separation between users**, so no personal content or interactions leak between accounts  

All tests were repeated as:

- **Guest user**
- **Authenticated GitHub user**
- **Admin user (Django admin panel)**

Each feature was tested for both **expected behaviour** and **failure handling**, ensuring the system responded safely, securely, and predictably.

| Feature / Page | Expectation | Test Performed | Result | Screenshot |
|----------------|-------------|----------------|--------|------------|
| **GitHub OAuth Login** | Only authenticated users should access features such as bookmarks and comments. | Tried accessing `/bookmarks/` and comment on repo cards when logged out. | Redirected to login page as expected and for comments when go to repo card no red comment button option | ![screenshot](documentation/defensive/login-required.jpg) |
| **Login Page** | Invalid OAuth attempts must fail safely. | Attempted login without a valid GitHub session. | GitHub rejected unauthorised authentication attempt; no access granted. | ![screenshot](documentation/defensive/login-failure.jpg) |
| **Bookmarks (Authenticated-only)** | Only logged-in users can bookmark repos. | Attempted to load `/bookmarks/` as guest. | Redirected to login page; no data exposed. | ![screenshot](documentation/defensive/bookmarks-denied.jpg) |
| **Bookmarking** | User-A should not see or manipulate User-B bookmarks. | Logged in as two different GitHub accounts and compared results. | Bookmarks displayed only for the correct user; no leakage. | ![screenshot](documentation/defensive/bookmarks-user-separated.jpg) |
| **Comments: Add** | Users cannot post empty or invalid comments. | Submitted empty comment. | Form displayed validation error; comment not created. | ![screenshot](documentation/defensive/comment-empty.jpg) |
| **Comments: Edit** | Only the comment owner can edit their comment. | Logged out and went over to my own comment. | no edit and delete buttons appear as expected. | ![screenshot](documentation/defensive/comment-edit-denied.jpg) |
| **Comments: Delete** | Only the creator may delete their own comment. | Logged in and went over to my own comment. | edit and delete buttons appear as expeccted | ![screenshot](documentation/defensive/comment-delete-protected.jpg) |
| **Search Users** | Must not allow malicious or invalid input to break search. | Entered symbols, emojis, SQL injection strings, empty input. | Search returned safe error handling or no results; no crashes. | ![screenshot](documentation/defensive/search-validation.jpg) |
| **Repository Details** | User cannot access repo-specific functionality for invalid repo names. | Modified repo name in URL to a non-existent repo. | Safe error message displayed; no crash. | ![screenshot](documentation/defensive/repo-invalid.jpg) |
| **Contact Form** | Form fields must require valid entries. | Submitted form with empty fields and invalid email format. | Validation errors displayed; form rejected as expected. | ![screenshot](documentation/defensive/contact-invalid.jpg) |
| **Contact Form Submission** | Only complete, valid data is stored. | Submitted valid message. | Message saved to DB and redirected to success page. | ![screenshot](documentation/defensive/contact-success.jpg) |
| **404 Page** | Non-existent URLs must return a custom 404 page. | Navigated to `/thispagedoesnotexist123/`. | Custom 404 page displayed with correct branding. | ![screenshot](documentation/defensive/404.jpg) |
| **Navbar Links** | Navbar elements should adjust based on authentication state. | Checked menus while logged in/out. | Login link replaced by Logout link. | ![screenshot](documentation/defensive/navbar-auth.jpg) |
| **Star / Unstar Repo** | API actions should only work for authenticated users. | Tried starring a repo while logged out. | Brought back to login page once star pressed | ![screenshot](documentation/defensive/star-denied.jpg) |
| **Direct URL Protection** | Users cannot brute-force URLs such as `/admin/` or restricted views. | Typed /admin directly. | Access denied unless logged into Django admin. | ![screenshot](documentation/defensive/admin-protected.jpg) |

### Summary

All defensive programming checks confirmed that GitShowcase.dev handles invalid inputs, unauthorised access, and URL manipulation safely. Features requiring authentication behaved correctly, and no user-to-user data leakage was possible during testing.

---

## User Story Testing

All user stories listed in the README were manually tested to ensure the final deployed version of GitShowcase.dev meets the expectations of developers, visitors, and administrators. Each user story was tested as the correct user type (guest, authenticated GitHub user, or admin), and the behaviour of each feature was compared against the acceptance criteria.

The table below documents the expected outcomes, how the story was tested, and the final results.

### Developer User Stories

| User Story | Expectation | Test | Result | Screenshot |
|-----------|-------------|------|--------|------------|
| As a developer, I want to log in with GitHub OAuth | User should authenticate securely through GitHub | Clicked *Login with GitHub* and completed OAuth flow | Logged in successfully and redirected to Home | ![screenshot](documentation/userstories/login.jpg) |
| As a developer, I want to browse all of my GitHub repositories | Homepage should list authenticated user's repos | Logged in and viewed home page | All public repositories loaded correctly via GitHub API | ![screenshot](documentation/userstories/repos.jpg) |
| As a developer, I want to view more details about each repository | Repo view button should bring user repos github page. | Clicked on repo card view button | Brought me to the repos github page | ![screenshot](documentation/userstories/repo-detail.jpg) |
| As a developer, I want to bookmark repositories | Clicking bookmark saves repo to user profile | Clicked bookmark icon on repo | Bookmark saved and appears in Bookmarks page | ![screenshot](documentation/userstories/bookmark.jpg) |
| As a developer, I want to remove bookmarks | Removing a bookmark deletes it from DB | Clicked remove bookmark | Bookmark removed and UI updated | ![screenshot](documentation/userstories/unbookmark.jpg) |
| As a developer, I want to comment on repositories | Form should allow authenticated users to add comments | Added comment to a repo | Comment saved, displayed, and linked to user | ![screenshot](documentation/userstories/comment.jpg) |
| As a developer, I want to edit and delete my own comments | Only comment owner can edit/delete | edit and delete buttons appear and function | Access allowed; changes updated | ![screenshot](documentation/userstories/comment-edit.jpg) |
| As a developer, I want to star/unstar a repository | Clicking button triggers GitHub star API | Starred and unstarred repo | GitHub API responded and UI updated accordingly | ![screenshot](documentation/userstories/star.jpg) |
| As a developer, I want to download a ZIP of repos | ZIP download button should work for all repos | Clicked download ZIP on repo | ZIP downloaded via GitHub API | ![screenshot](documentation/userstories/zip.jpg) |

---

### Visitor / Guest User Stories

| User Story | Expectation | Test | Result | Screenshot |
|-----------|-------------|------|--------|------------|
| As a visitor, I want to search GitHub users | Search page should accept username and show repos | Searched for public GitHub user | User info and repos displayed | ![screenshot](documentation/userstories/search.jpg) |
| As a visitor, I want to view other users’ repositories | Should be able to open profiles without login | Viewed another user's repos | Repos displayed correctly | ![screenshot](documentation/userstories/search-repos.jpg) |
| As a visitor, I want to view repository details | Repo details should show metadata but no interactions | Opened repo detail page as guest | Metadata visible; comments actions hidden | ![screenshot](documentation/userstories/guest-repo-detail.jpg) |
| As a visitor, I want to read repository comments | Comments section should be publicly visible | Viewed repo comments as guest | Comments visible and paginated | ![screenshot](documentation/userstories/guest-comments.jpg) |
| As a visitor, I want an About page | About page explains the purpose of the platform | Opened `/about` | Page displays correctly | ![screenshot](documentation/userstories/about.jpg) |
| As a visitor, I want to submit a contact form | Contact form should validate input and submit | Submitted valid contact message | Message stored and success page displayed | ![screenshot](documentation/userstories/contact.jpg) |
| As any user, I want a custom 404 page | Invalid URL should show branded 404 | Opened random invalid URL | Custom 404 displayed | ![screenshot](documentation/userstories/404.jpg) |

---

### Admin / Superuser Stories

| User Story | Expectation | Test | Result | Screenshot |
|-----------|-------------|------|--------|------------|
| As an admin, I want to view contact messages | Django admin should show stored messages | Logged into /admin and checked Contact model | Messages displayed correctly with timestamps | ![screenshot](documentation/userstories/admin-contact.jpg) |
| As an admin, I want to manage user comments | Admin panel should show all comment entries | Viewed Comments model in admin | All user comments visible and editable | ![screenshot](documentation/userstories/admin-comments.jpg) |

---

### Summary

All user stories were fully satisfied.  
GitShowcase.dev behaves exactly as expected for:

- Guests  
- Authenticated GitHub users  
- Admin/superusers  

Each feature was tested for correct flow, incorrect use, and edge cases, confirming that every story’s acceptance criteria has been successfully met.

---

## Manual Feature Testing

Each feature in GitShowcase.dev was manually tested to ensure correct behaviour, error handling, and edge-case safety. Tests were carried out on the deployed site using both authenticated and guest users. Expected behaviour was compared with actual results for accuracy.

### Feature Testing Table

| Feature | Expected Behaviour | Test Performed | Result | Screenshot |
|--------|---------------------|----------------|--------|------------|
| GitHub OAuth Login | User is redirected to GitHub and authenticated | Clicked Login button | Successful login and redirect to home | ![screenshot](documentation/manual/login.jpg) |
| Logout | Logs user out and ends session | Clicked Logout | Returned to visitor mode; restricted pages inaccessible | ![screenshot](documentation/manual/logout.jpg) |
| Repository Listing | Display all public repos from authenticated user | Logged in and viewed home page | All repos displayed correctly with metadata | ![screenshot](documentation/manual/repos.jpg) |
| Repository Detail View | Show metadata, buttons, and comments | Opened repo detail page by clicking view buttom | Page loaded with repo info and actions | ![screenshot](documentation/manual/repo-detail.jpg) |
| Bookmark Repo | Add selected repo to user bookmarks | Clicked Bookmark | Repo saved and shown in Bookmarks page | ![screenshot](documentation/manual/bookmark.jpg) |
| Remove Bookmark | Remove bookmark from user list | Clicked Remove button | Repo removed from Bookmarks | ![screenshot](documentation/manual/unbookmark.jpg) |
| View Bookmarks | Display all bookmarked repos for logged-in user | Opened `/bookmarks/` | Correct repos displayed for user | ![screenshot](documentation/manual/bookmarks.jpg) |
| Star Repo | Star/unstar repo using GitHub API | Clicked Star button | GitHub API responded; UI updated | ![screenshot](documentation/manual/star.jpg) |
| Download ZIP | Download zip archive from GitHub | Clicked Download Zip | File downloaded successfully | ![screenshot](documentation/manual/zip.jpg) |
| Add Comment | Authenticated users can post comments | Submitted comment form | Comment appears under repo | ![screenshot](documentation/manual/comment-add.jpg) |
| Edit Comment | Only owner can edit own comment | Edited submitted comment | Edited successfully | ![screenshot](documentation/manual/comment-edit.jpg) |
| Delete Comment | Only owner can delete own comment | Clicked delete on own comment | Comment removed | ![screenshot](documentation/manual/comment-delete.jpg) |
| Search GitHub Users | Search for any GitHub username | Entered existing usernames | Results and repos displayed | ![screenshot](documentation/manual/search.jpg) |
| Invalid Search | Invalid usernames return safe message | Entered random/invalid string | “No user found” message displayed | ![screenshot](documentation/manual/search-invalid.jpg) |
| Contact Form | Validate and submit messages | Entered valid form data | Redirected to success page | ![screenshot](documentation/manual/contact.jpg) |
| Contact Form Validation | Form rejects invalid or empty fields | Submitted empty/invalid email | Errors displayed; no submission | ![screenshot](documentation/manual/contact-error.jpg) |
| 404 Page | Display custom 404 page | Visited invalid URL | Custom 404 page shown | ![screenshot](documentation/manual/404.jpg) |
| Navbar State | Navbar updates based on authentication | Compared logged-in vs guest view | Correct links appear in each mode | ![screenshot](documentation/manual/navbar.jpg) |

### Summary

All features performed as expected with no broken flows or incorrect behaviour.  
Both happy-path and negative-path testing confirmed stable and correct functionality.

---


## Automated Testing

For this milestone, I did not implement automated tests for JavaScript or Python.  
The application was instead tested thoroughly using manual testing, defensive programming checks, and user story validation.  

I understand that in a real-world project, automated tests would play a vital role in guaranteeing long-term stability, preventing regressions, and improving confidence when refactoring. Automated testing is something I plan to introduce in future versions of GitShowcase.dev.

---

### JavaScript Automated Testing (Jest)

Although the project contains small JavaScript files (`comment.js` and `star.js`), no Jest tests were written for this release.

If Jest testing were to be implemented in the future, it would involve:

- Initialising an NPM test environment  
- Installing Jest and jsdom  
- Exporting functions for testing  
- Writing `.test.js` files for UI behaviour such as:  
  - Star/unstar button logic  
  - Comment edit/delete interactions  
  - Bookmark icon toggling  

These tests would then be run using:

- `npm test`  
- `npm test --coverage` (optional for coverage reports)

#### Jest Test Results  
_No Jest test files are present in this project, therefore no automated JS test results or coverage reports were generated._

---

### Python Automated Testing (Django Unit Tests)

Django provides a comprehensive built-in testing framework using:

- `TestCase`  
- The Django test client  
- Assertion-based validation  
- URL, form, and model testing  

However, no Django unit tests were implemented during this milestone.

If implemented in future, the tests would cover:

- View permissions  
- Form validation  
- Model relationships  
- URL routing  
- Mocked GitHub API responses  

Coverage testing would normally use:

- `coverage run manage.py test`  
- `coverage report`  
- `coverage html`

#### Unit Test Results  
_No Django unit tests or coverage reports were created for this project._

### Future Plans for Automated Testing

I intend to expand GitShowcase.dev with automated tests in future development, focusing on:

- Jest tests for interactive UI behaviour  
- Comprehensive Django test suite (views, forms, models, permissions)  
- Mocked GitHub API responses for reliable automated testing  

This will ensure the platform remains stable and scalable as more features are added.

---


## Bugs

During development of GitShowcase.dev, several issues were identified and resolved.  
All bugs were tracked using the **GitHub Issues** system, allowing for clear documentation, screenshots, tagging, and progress tracking throughout the debugging process.

Using GitHub Issues ensured that every bug was documented with:

- A clear description  
- Steps to reproduce  
- Screenshots  
- Labels (e.g., `bug`)  
- Status (open/closed)  
- Developer comments and fixes  

This approach also provides long-term traceability for future updates or refactors.

---

## Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/colmwoods/GitShowcase.dev?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/colmwoods/GitShowcase.dev/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

All bugs resolved during development can be viewed directly using the GitHub Issues tracker:

🔗 **Closed Bugs:**  
https://www.github.com/colmwoods/GitShowcase.dev/issues?q=is%3Aissue+is%3Aclosed+label%3Abug

Below is a snapshot of some of the resolved issues:

![screenshot](documentation/bugs/gh-issues-closed.jpg)

These include fixes for:

- Unexpected API errors when fetching GitHub repositories  
- Star/unstar button not updating visually  
- Bookmark icon state inconsistencies  
- Comments not displaying after being submitted  
- User search query failures under invalid input  
- Minor layout inconsistencies on small devices  
- 404 page not triggering correctly in early versions  

All of these issues have been fully resolved.

---

## Unfixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/colmwoods/GitShowcase.dev?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/colmwoods/GitShowcase.dev/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

At the time of submission, no major unfixed bugs remain that would affect core functionality of GitShowcase.dev.

Any currently open issues can be viewed here:

🔗 **Open Bugs:**  
https://www.github.com/colmwoods/GitShowcase.dev/issues?q=is%3Aissue+is%3Aopen+label%3Abug

![screenshot](documentation/bugs/gh-issues-open.jpg)

These open issues are minor, non-breaking observations and do not affect the overall usability of the platform.

---

## Known Issues

The following issues are known and documented, but fall outside the project’s scope or are considered acceptable based on industry standards and Code Institute guidelines:

| Issue | Screenshot |
| --- | --- |
| The project is designed to be responsive from `375px` and upwards. Extremely wide resolutions (4k/8k displays, ultra-wide monitors) may show minor spacing variations. This is normal and outside the CI design scope. | ![screenshot](documentation/issues/poor-responsiveness.jpg) |
| The W3C HTML validator sometimes flags warnings on `<section>` elements without `h2–h6` headings. This is acceptable, as the design uses custom layout structures rather than semantic headings inside every section. | ![screenshot](documentation/issues/section-header.jpg) |
| Some validation warnings appear on Django Allauth template pages. These templates are third-party and not modified by me, so the warnings are beyond my control. | ![screenshot](documentation/issues/allauth.jpg) |

---

### Final Bug Summary

At the time of submission:

- ✔ All **major functional bugs** have been resolved.  
- ✔ No bugs exist that block a user from browsing repositories, starring, bookmarking, commenting, or using GitHub OAuth.  
- ✔ All known issues have been documented transparently.  
- ✔ Minor visual inconsistencies do not affect overall application use.  

While the application has undergone extensive manual testing, it is still possible that bugs exist which were not discovered. These will be addressed in future updates and noted via the GitHub Issues tracker.
