# Git Guidelines

## 1. Your Team's Branching Strategy
- Use main branch for stable production-ready code.
- Create feature branches from main for new features or fixes:  
  feature/short-description
- Merge feature branches back into main only after code review.

## 2. Commit Message Conventions
- Use clear, concise messages.
- Format: "message"   

## 3. Code Review Process
- Open a pull request for every feature branch.
- At least one teammate must review the code before merging.

## 4. Release Workflow
- Create a release branch
- Test release branch before merging back into main

# I asked for these
## 5. Common Git Commands Reference
- Clone a repo: `git clone <repo_url>`  
- Check status: `git status`  
- Stage changes: `git add <file>`  
- Commit changes: `git commit -m "message"`  
- Push changes: `git push origin <branch>`  
- Pull latest changes: `git pull origin <branch>`  
- Create branch: `git checkout -b <branch>`  
- Merge branch: `git merge <branch>`  
- Resolve conflicts: edit files → `git add <file>` → `git commit`
