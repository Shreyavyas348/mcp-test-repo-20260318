import subprocess

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return "", str(e)


def create_repo(repo_name):
    cmd = f"gh repo create {repo_name} --public --source=. --remote=origin --push"
    out, err = run_command(cmd)

    if err:
        return {"status": "error", "message": err}
    return {"status": "success", "message": out}


def add_file(repo_name, filename, content):
    try:
        with open(filename, "w") as f:
            f.write(content)

        run_command("git add .")
        run_command(f'git commit -m "Add {filename}"')
        run_command("git push")

        return {"status": "success", "message": f"{filename} added"}
    except Exception as e:
        return {"status": "error", "message": str(e)}