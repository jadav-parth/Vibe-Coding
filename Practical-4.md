# Practical 4: GitHub Integration and Branch Management using VS Code

## 📌 Objective

To configure Git and GitHub in Visual Studio Code, initialize a Git repository, stage and commit changes, push code to GitHub, and create and manage branches.

---

## 🛠️ Prerequisites

- Visual Studio Code
- Git CLI
- GitHub Account
- Internet Connection

---

## 📂 Project Setup

1. Install Git.
2. Install Visual Studio Code.
3. Open the project folder in VS Code.
4. Open the integrated terminal (`Ctrl + ~`).

---

## 🚀 Steps Performed

### 1. Configure Git

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

### 2. Initialize Git Repository

```bash
git init
```

---

### 3. Add Project Files

```bash
git add .
```

---

### 4. Commit Changes

```bash
git commit -m "Initial Commit"
```

---

### 5. Connect to GitHub Repository

```bash
git remote add origin https://github.com/username/repository.git
```

---

### 6. Push Code to GitHub

```bash
git branch -M main
git push -u origin main
```

---

### 7. Create and Switch to a New Branch

```bash
git checkout -b feature-login
```

or

```bash
git switch -c feature-login
```

---

## 📋 Commands Used

| Command | Description |
|----------|-------------|
| `git init` | Initialize a local Git repository |
| `git add .` | Stage all files |
| `git commit -m "message"` | Commit staged changes |
| `git remote add origin URL` | Connect local repository to GitHub |
| `git branch -M main` | Rename branch to main |
| `git push -u origin main` | Push code to GitHub |
| `git checkout -b branch-name` | Create and switch to a new branch |
| `git switch -c branch-name` | Alternative command to create a new branch |

---

## ✅ Result

- Git was configured successfully.
- Local repository was initialized.
- Project files were staged and committed.
- Repository was published to GitHub.
- A new branch was created and switched successfully.

---

## 👨‍💻 Author

**Name:** Your Name  
**Course:** Diploma in Computer Engineering  
**Practical:** GitHub Integration and Branch Management using VS Code
