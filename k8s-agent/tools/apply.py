import subprocess

def kubectl_apply(path):

    result = subprocess.run(
        ["kubectl","apply","-f",path],
        capture_output=True,
        text=True
    )

    return result.stdout