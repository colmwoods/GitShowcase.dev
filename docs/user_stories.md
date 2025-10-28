# User Stories & Agile Planning

This project was planned and managed using an **Agile development methodology**, with all work organised into **Epics**, **User Stories**, and **Tasks**.  
The complete Agile workflow, including progress tracking and issue management, is available on the GitHub Project Board:  
👉 [View GitHub Project Board](https://github.com/users/colmwoods/projects/10)

---

## Agile Structure

All project functionality was planned and delivered using an **iterative Agile approach**, broken down into three top-level tiers:  
**Epics (LO1–LO7)**, **Merit**, and **Distinction** — each containing detailed **User Stories** and technical **Tasks**.

Every story across all tiers follows the standard Agile format:

> *As a [user type], I want [goal], so that [benefit].*

This ensures all deliverables — from initial features to refinement and polish — remain focused on real user needs and measurable outcomes.

---

### **1. Epics (LO1–LO7)**
Each Code Institute Learning Outcome (LO1–LO7) was treated as an **Epic**, representing a major area of functionality — such as planning, data models, authentication, testing, deployment, and object-based concepts.  
Each Epic was divided into smaller **User Stories**, each describing a specific user-focused feature written in the Agile format above.

---

### **2. Merit**
The **Merit** tier represents refinement work that goes beyond the pass-level criteria.  
Merit stories build upon the core features established in the Epics, focusing on:
- Usability improvements  
- Documentation and testing enhancements  
- Code quality and efficiency refinements  
- Data handling and maintainability upgrades  

These demonstrate iterative improvement and alignment with intermediate-level professional standards.

---

### **3. Distinction**
The **Distinction** tier includes advanced, professional-level enhancements.  
These stories are focused on:
- Accessibility and UX excellence  
- Design consistency and interface polish  
- Robust error handling and real-world reliability  
- Overall performance, responsiveness, and maintainability  

Distinction-level work demonstrates attention to detail, professional quality, and readiness for deployment in real-world environments.

---

### **4. User Stories**
Each **User Story** represents a single, testable piece of functionality from the user’s perspective.  
They define what value is being delivered and when the story is considered complete through measurable **Acceptance Criteria** checklists.  

Every story includes:
- A clear **goal and user role** written in Agile format.  
- **Acceptance Criteria** to confirm successful delivery.  
- Links to **Tasks**, commits, or issues where applicable.  

---

### **5. Tasks**
**Tasks** are the smallest actionable steps required to implement a User Story.  
They cover specific technical actions such as:
- Creating models, templates, or views  
- Writing test cases or documentation  
- Implementing CSS/UX changes or deployment scripts  

Tasks are typically tracked as checkboxes under each User Story or as smaller GitHub Issues linked to the story.

---

## Project Board Columns

| Column | Purpose |
|--------|----------|
| **Todo** | All planned Epics, Merit, and Distinction stories awaiting development. |
| **In Progress** | User stories or tasks actively being worked on. |
| **Done** | Completed Epics or stories that meet all acceptance criteria. |
| **Merit** | Medium-level refinement and enhancement phase. |
| **Distinction** | Advanced refinement and professional polish phase. |

---

## Example of Agile User Stories Across All Tiers

All stories across Epics, Merit, and Distinction follow the same Agile format:

> *As a [user type], I want [goal], so that [benefit].*

Each story includes measurable **Acceptance Criteria** to confirm when it is complete.

---

### Epic Example (LO2 – Data Model & Features)
> *As a developer, I want to automatically fetch and display my GitHub repositories, so that visitors can easily view my public projects.*

**Acceptance Criteria:**
- [ ] GitHub API integrated successfully.  
- [ ] Repository data stored and displayed dynamically on the portfolio page.  
- [ ] Repositories include name, description, and link to GitHub.  

---

### Merit Example
> *As a user, I want visual feedback when I perform an action (e.g., submit a comment or sync GitHub), so that I know it was completed successfully.*

**Acceptance Criteria:**
- [ ] Django messages framework implemented for success/error states.  
- [ ] Notification banner visible across all pages.  
- [ ] Banner uses consistent color coding (info, success, warning, danger).  

---