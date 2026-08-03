<img width="1366" height="768" alt="WhatsApp Image 2026-08-03 at 2 56 15 AM" src="https://github.com/user-attachments/assets/4eb09154-f49a-47d1-819a-6292c33e1a72" />
# Practical 4: GitHub Integration and Branch Management using VS Code

## 📋 Prerequisites

- Visual Studio Code
- Git CLI
- GitHub Account

---

## 🛠️ Step-by-Step Procedure

### Step 1: Git Initial Configuration

Open the VS Code Terminal (`Ctrl + ~`) and configure your Git username and email.

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

### Step 2: Connect VS Code with GitHub

1. Click the **Accounts** icon in the top-right corner of VS Code.
2. Select **Sign in with GitHub**.
3. Login using your GitHub account.
4. Authorize Visual Studio Code to access your GitHub account.
5. After successful authentication, VS Code will be connected to GitHub.

---

### Step 3: Initialize Local Git Repository

1. Open your project folder in Visual Studio Code.
2. Open the **Source Control** panel (`Ctrl + Shift + G`).
3. Click **Initialize Repository**.

Or use the terminal:

```bash
git init
```

---

### Step 4: Stage and Commit Changes

1. Modify or create project files.
2. Click the **+** icon to stage files.
3. Enter a commit message.
4. Click **Commit**.

Or use the terminal:

```bash
git add .
git commit -m "Initial Commit"
```

---

### Step 5: Publish / Push Repository to GitHub

1. Click **Publish Branch** in VS Code.
2. Choose **Public** or **Private** repository.
3. Wait until the repository is uploaded successfully.

Or use the terminal:

```bash
git remote add origin https://github.com/username/repository.git
git branch -M main
git push -u origin main
```

---

### Step 6: Create and Switch to a New Branch

1. Click the branch name from the VS Code Status Bar.
2. Select **Create New Branch**.
3. Enter a branch name (Example: `feature-login`).
4. VS Code will automatically switch to the new branch.

Or use the terminal:

```bash
git checkout -b feature-login
```

or

```bash
git switch -c feature-login
```

---

## 📋 Git Commands Used

| Command | Description |
|---------|-------------|
| `git config --global user.name` | Set Git username |
| `git config --global user.email` | Set Git email |
| `git init` | Initialize repository |
| `git add .` | Stage all files |
| `git commit -m "message"` | Commit changes |
| `git remote add origin URL` | Add remote repository |
| `git branch -M main` | Rename branch to main |
| `git push -u origin main` | Push project to GitHub |
| `git checkout -b branch-name` | Create and switch branch |
| `git switch -c branch-name` | Alternative command for new branch |

---

## ✅ Result

- Git was configured successfully.
- VS Code was connected with GitHub.
- Local Git repository was initialized.
- Project files were staged and committed.
- Repository was published to GitHub.
- A new branch was created and switched successfully.

---
