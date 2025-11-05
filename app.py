import requests
import sys
import os
from datetime import datetime

def main():
    """
    A simple test script that demonstrates various features
    you can use in GitHub Actions.
    """

    print("=" * 50)
    print("🚀 GitHub Actions Test Script")
    print("=" * 50)

    # 1. Basic information
    print("\n📋 Basic Information:")
    print(f"  • Python version: {sys.version.split()[0]}")
    print(f"  • Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  • Running on: {os.uname().sysname}")

    # 2. Check environment variables (GitHub Actions provides many)
    print("\n🔧 GitHub Actions Environment:")
    github_vars = {
        'GITHUB_ACTOR': 'User who triggered the workflow',
        'GITHUB_REPOSITORY': 'Repository name',
        'GITHUB_REF': 'Branch or tag ref',
        'GITHUB_WORKFLOW': 'Workflow name',
    }
    for var, description in github_vars.items():
        value = os.getenv(var, 'Not set')
        print(f"  • {var}: {value}")

    # 3. Test external library (requests)
    print("\n🌐 Testing External Library (requests):")
    print(f"  • Requests version: {requests.__version__}")

    try:
        response = requests.get('https://api.github.com/zen', timeout=5)
        if response.status_code == 200:
            print(f"  • GitHub API test: ✓ Success")
            print(f"  • Zen message: '{response.text}'")
        else:
            print(f"  • GitHub API test: ✗ Failed ({response.status_code})")
    except Exception as e:
        print(f"  • GitHub API test: ✗ Error: {e}")

    # 4. Simple calculation test
    print("\n🧮 Simple Calculation Test:")
    result = sum(range(1, 101))
    expected = 5050
    if result == expected:
        print(f"  • Sum of 1-100: {result} ✓ Correct!")
    else:
        print(f"  • Sum of 1-100: {result} ✗ Expected {expected}")
        sys.exit(1)  # Exit with error code

    # 5. File operations test
    print("\n📁 File Operations Test:")
    test_file = 'test_output.txt'
    with open(test_file, 'w') as f:
        f.write(f"Test run completed at {datetime.now()}\n")
    print(f"  • Created file: {test_file} ✓")

    with open(test_file, 'r') as f:
        content = f.read()
    print(f"  • Read file content: {content.strip()} ✓")

    print("\n" + "=" * 50)
    print("✅ All tests passed successfully!")
    print("=" * 50)

    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
