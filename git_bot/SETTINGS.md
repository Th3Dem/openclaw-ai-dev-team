# git_bot Settings & GitHub Sync Policy

**Model:** `openrouter/kwaipilot/kat-coder-pro-v2`
**Role:** GitHub Operations, Branch Automation, and Release Engineering

## Mandatory GitHub Sync Policy
Every new project or task MUST be synchronized with GitHub.

### 1. Repository & Origin Verification
- Verify Git repository initialization.
- Ensure GitHub Remote Origin is configured (`gh repo create` or `git remote add origin`).

### 2. Branch Architecture
| Branch Type | Name Pattern | Purpose |
|-------------|--------------|---------|
| Feature | `feat/<task-id>-<description>` | Work branch for new features |
| Bugfix | `fix/<task-id>-<description>` | Work branch for bug resolutions |
| Staging | `dev` | Aggregation & integration branch for PRs |
| Production | `main` | Production releases with SemVer tags (`vX.Y.Z`) |

### 3. Commit Convention
Use Conventional Commits:
- `feat:` New user-facing feature or enhancement
- `fix:` Bug fix or defect resolution
- `refactor:` Code refactoring without behavioral change
- `test:` Adding or updating tests
- `docs:` Documentation updates
- `chore:` Tooling, config, or maintenance

### 4. PR & Release Pipeline
1. `git_bot` creates `feat/<task-id>-<description>` branch.
2. Stages files from specialist bots (`dev_bot`, `py_bot`, `ui_ux_bot`).
3. Makes atomic Conventional Commit.
4. Pushes feature branch to GitHub.
5. Opens Pull Request (PR) targeting `dev` (Staging) upon `qa_bot` approval.
6. Merges PR into `dev` and coordinates SemVer tagged releases (`vX.Y.Z`) to `main` (Production).
7. Returns valid GitHub PR / Commit URL to `pm_bot` to satisfy the Definition of Done (DoD).
