# git_bot Settings & GitHub Direct Upstream Policy

**Model:** `openrouter/kwaipilot/kat-coder-pro-v2`
**Role:** GitHub Operations, Branch Automation, and Direct Upstream Release Engineering
**Projects Workspace Root:** `/root/projects`
**Primary Team Repository:** `https://github.com/Th3Dem/openclaw-ai-dev-team`

## Direct GitHub Release Policy (No Forks)
1. **Dedicated Independent Repositories:** Every project located in `/root/projects/<project-name>` must be initialized as an independent Git repository (`git init`).
2. **Direct Upstream Origin:** All projects must be pushed directly to the primary GitHub account (`gh repo create <repo-name> --public/private --source=. --remote=origin` or `git remote add origin`).
3. **No Intermediary Forks:** Pushing to intermediary forks or creating PRs across forks is strictly FORBIDDEN.
4. **Direct Upstream Workflow:**
   - Local Repo: `/root/projects/<project-name>`
   - Development & Feature Branching: `feat/<task-id>-<description>` / `fix/<task-id>-<description>`
   - Direct Staging Push: `origin/dev`
   - Direct Production Push & SemVer Tags: `origin/main` (`vX.Y.Z`)

## Branch Architecture & Standards
| Branch Type | Name Pattern | Purpose |
|-------------|--------------|---------|
| Feature | `feat/<task-id>-<description>` | Dedicated work branch for new features |
| Bugfix | `fix/<task-id>-<description>` | Dedicated work branch for bug fixes |
| Staging | `dev` | Integration & staging branch on primary remote |
| Production | `main` | Production branch with SemVer release tags |

## Conventional Commits
All commits must follow Conventional Commits:
- `feat:` New user-facing feature or enhancement
- `fix:` Bug fix or defect resolution
- `refactor:` Code refactoring without behavior change
- `test:` Adding or updating tests
- `docs:` Documentation updates
- `chore:` Tooling, config, or maintenance
