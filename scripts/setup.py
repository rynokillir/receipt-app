import os
import subprocess

def install_deps():
    subprocess.run(["pip", "install", "-r", "F:\\Receipt_App\\managers\\requirements.txt"])
    subprocess.run(["npm", "install"], cwd="F:\\Receipt_App\\app\\receipt_app"])
    subprocess.run(["F:\\Receipt_App\\flutter\\bin\\flutter.bat", "pub", "get"], cwd="F:\\Receipt_App\\app\\receipt_app"])

def setup_vercel(token):
    with open("F:\\Receipt_App\\services\\vercel_token.txt", "w") as f:
        f.write(f"VERCEL_TOKEN={token}")
    os.environ["VERCEL_TOKEN"] = token
    subprocess.run(["vercel", "deploy"], cwd="F:\\Receipt_App\\app\\receipt_app"])

if __name__ == "__main__":
    install_deps()
    vercel_token = input("Enter your Vercel API token: ")
    setup_vercel(vercel_token)