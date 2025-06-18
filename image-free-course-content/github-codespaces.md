## IDE: GitHub Codespaces

[GitHub Codespaces](https://github.com/features/codespaces) is a cloud-hosted development environment built right into GitHub that gets you coding faster with pre-configured containers, adjustable compute power, and seamless integration with workflows like Actions and Copilot.

**Why Codespaces helps**

- **Reproducible onboarding**: Say goodbye to “works on my machine” woes—everyone uses the same setup for assignments or demos.
- **Anywhere access**: Jump back into your project from a laptop, tablet, or phone without having to reinstall anything.
- **Rapid experimentation &amp; debugging**: Spin up short-lived environments on any branch, commit, or PR to isolate bugs or test features, or keep longer-lived codespaces for big projects.

[[Image description: Here's alt text describing the image:

A screenshot showing a tutorial on GitHub Codespaces. The background is a dark teal, with a stylized, light beige cloud shape in the center containing code. At the bottom, a bright blue banner displays the handwritten text "Introduction to GitHub Codespaces". The main area displays multiple code windows with lines of text, filenames, and system messages indicative of a development environment.  The right side shows a file explorer-like panel listing folders and files.  The overall color palette is predominantly dark teal with accents of light beige and bright blue.  The GitHub logo is subtly visible in the upper-right. The text within the code windows is too small to be legible in the provided alt text.]](https://www.youtube.com/watch?v=-tQ2nxjqP6o)

### Quick Setup

1. [**From the GitHub UI**](https://github.com/codespaces)

   - Go to your repo and click **Code → Codespaces → New codespace**.
   - Pick the branch and machine specs (2–32 cores, 8–64 GB RAM), then click **Create codespace**.

2. [**In Visual Studio Code**](https://code.visualstudio.com/docs/remote/codespaces)

   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac), choose **Codespaces: Create New Codespace**, and follow the prompts.

3. [**Via GitHub CLI**](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-github-codespaces-with-github-cli)

   ```bash
   gh auth login
   gh codespace create --repo OWNER/REPO
   gh codespace list    # List all codespaces
   gh codespace code    # opens in your local VS Code
   gh codespace ssh     # SSH into the codepsace
   ```

### Features To Explore

- **Dev Containers**: Set up your environment the same way every time using a `devcontainer.json` or your own Dockerfile. [Introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers)
- **Prebuilds**: Build bigger or more complex repos in advance so codespaces start up in a flash. [About prebuilds](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/about-github-codespaces-prebuilds)
- **Port Forwarding**: Let Codespaces spot and forward the ports your web apps use automatically. [Forward ports in Codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace)
- **Secrets &amp; Variables**: Keep your environment variables safe in the Codespaces settings for your repo. [Manage Codespaces secrets](https://docs.github.com/en/enterprise-cloud@latest/codespaces/managing-codespaces-for-your-organization/managing-development-environment-secrets-for-your-repository-or-organization)
- **Dotfiles Integration**: Bring in your dotfiles repo to customize shell settings, aliases, and tools in every codespace. [Personalizing your codespaces](https://docs.github.com/en/codespaces/setting-your-user-preferences/personalizing-github-codespaces-for-your-account)
- **Machine Types &amp; Cost Control**: Pick from VMs with 2 to 32 cores and track your usage in the billing dashboard. [Managing Codespaces costs](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces)
- **VS Code &amp; CLI Integration**: Flip between browser VS Code and your desktop editor, and script everything with the CLI. [VS Code Remote: Codespaces](https://code.visualstudio.com/docs/remote/codespaces)
- **GitHub Actions**: Power up prebuilds and your CI/CD right inside codespaces using Actions workflows. [Prebuilding your codespaces](https://docs.github.com/en/codespaces/prebuilding-your-codespaces)
- **Copilot in Codespaces**: Let Copilot help you write code with in-editor AI suggestions. [Copilot in Codespaces](https://docs.github.com/en/codespaces/reference/using-github-copilot-in-github-codespaces)
