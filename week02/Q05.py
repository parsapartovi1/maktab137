import json

def sum_logs():
    info = []
    warning = []
    error = []

    try:
        with open('maktab137.hw.log', 'r') as file:
            for line in file:
                clean = line.split()
                try:
                    level = clean[5].lower()
                    if level == 'notice' or level == '[notice]':
                        info.append('info')
                    elif level == 'warning' or level == '[warning]':
                        warning.append('warning')
                    elif level == 'error' or level == '[error]':
                        error.append('error')
                except IndexError:
                    warning.append('warning')  # fallback for malformed lines
    except FileNotFoundError:
        print("Log file not found.")
        return

    data = {
        "INFO": str(info.count('info')),
        "WARNING": str(warning.count('warning')),
        "ERROR": str(error.count('error'))
    }

    with open('summary.json', 'w') as out_file:
        json.dump(data, out_file, indent=2)