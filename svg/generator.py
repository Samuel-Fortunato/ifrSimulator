import sys
import os
import subprocess

def execute_script(script_name, output_file):
    if not os.path.exists(script_name):
        print(f"Error: Script '{script_name}' not found.")
        return

    try:
        env = os.environ.copy()
        env["OUTPUT_FILE"] = output_file
        result = subprocess.run([sys.executable, script_name], capture_output=True, text=True, env=env)
        if result.returncode == 0:
            print(f"Successfully executed '{script_name}'.")
        else:
            print(f"Error executing '{script_name}': {result.stderr}")
    except Exception as e:
        print(f"Failed to execute '{script_name}': {e}")

if __name__ == "__main__":
    if "-o" in sys.argv:
        output_index = sys.argv.index("-o")
        if output_index + 1 < len(sys.argv):
            output_file = sys.argv[output_index + 1]
            del sys.argv[output_index:output_index + 2]
        else:
            print("Error: Missing output directory after '-o' flag.")
            sys.exit(1)
    else:
        output_file = os.getcwd()

    if len(sys.argv) < 2:
        print("Usage: python generator.py [-o output_file] <sub-script1.py> [sub-script2.py ...]")
        sys.exit(1)

    # Execute each provided sub-script
    for script in sys.argv[1:]:
        execute_script(script, output_file)
