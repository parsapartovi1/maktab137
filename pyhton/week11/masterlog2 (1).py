#!/usr/bin/env python3
import argparse
import re
import time
from collections import Counter

parser = argparse.ArgumentParser(description="Log Analysis Toolkit")
subparsers = parser.add_subparsers(dest="command")

scan_parser = subparsers.add_parser("scan", help="Scan a log")
scan_parser.add_argument("--file", required=True)
scan_parser.add_argument("--ip", action="store_true")
scan_parser.add_argument("--url", action="store_true")
scan_parser.add_argument("--errors", action="store_true")
scan_parser.add_argument("--count", action="store_true")
scan_parser.add_argument("--export", help="Save results to file")


stats_parser = subparsers.add_parser("stats", help="Generate statistics")
stats_parser.add_argument("--file", required=True)


clean_parser = subparsers.add_parser("clean", help="Clean logs")
clean_parser.add_argument("--file", required=True)
clean_parser.add_argument("--remove-ip", action="store_true")
clean_parser.add_argument("--mask-email", action="store_true")
clean_parser.add_argument("--remove-timestamp", action="store_true")
clean_parser.add_argument("--extract-api", action="store_true")
clean_parser.add_argument("--export", help="Save cleaned logs")

monitor_parser = subparsers.add_parser("monitor", help="Live log tailing")
monitor_parser.add_argument("--file", required=True)
monitor_parser.add_argument("--contains", required=True)

args = parser.parse_arg()

ip_pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}"
timestamp_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
http_request_pattern = r"(GET|POST|PUT|DELETE) /[^\s]*"
url_pattern = r"https?://[^\s]+"
error_pattern = r"\b[45]\d{2}\b"


if args.command == "scan":
    with open(args.file, "r", encoding="utf-8") as f:
        data = f.read()

    if args.ip:
        results = re.findall(ip_pattern, data)
    elif args.url:
        results = re.findall(url_pattern, data)
    elif args.errors:
        results = re.findall(error_pattern, data)
    else:
        results = []

    if args.count:
        print(f"Count: {len(results)}")
    else:
        for r in results:
            print(r)

    if args.export:
        with open(args.export, "w", encoding="utf-8") as out:
            for r in results:
                out.write(r + "\n")
        print(f"Results exported to {args.export}")


elif args.command == "stats":
    with open(args.file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    ips, urls, sizes = [], [], []
    errors = 0

    for line in lines:
        ip_match = re.search(ip_pattern, line)
        if ip_match: ips.append(ip_match.group())

        url_match = re.search(url_pattern, line)
        if url_match: urls.append(url_match.group())

        error_match = re.search(error_pattern, line)
        if error_match: errors += 1

        size_match = re.search(r"\b\d+$", line)
        if size_match: sizes.append(int(size_match.group()))

    unique_ips = len(set(ips))
    most_endpoint = Counter(urls).most_common(1)[0][0] if urls else None
    total_requests = len(lines)
    error_rate = (errors / total_requests * 100) if total_requests else 0
    avg_size = sum(sizes) / len(sizes) if sizes else 0

    print(f"Unique IP count: {unique_ips}")
    print(f"Most requested endpoint: {most_endpoint}")
    print(f"Error rate: {error_rate:.2f}%")
    print(f"Average response size: {avg_size:.2f}")




elif args.command == "clean":
    with open(args.file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cleaned = []
    for line in lines:
        if args.remove_ip:
            line = re.sub(ip_pattern, "[REMOVED_IP]", line)
        if args.mask_email:
            line = re.sub(email_pattern, "[EMAIL_MASKED]", line)
        if args.remove_timestamp:
            line = re.sub(timestamp_pattern, "[REMOVED_TIMESTAMP]", line)
        if args.extract_api:
            if not re.search(r"/api/", line):
                continue
        cleaned.append(line)

    if args.export:
        with open(args.export, "w", encoding="utf-8") as out:
            out.writelines(cleaned)
        print(f"Cleaned logs exported to {args.export}")
    else:
        for line in cleaned:
            print(line.strip())


elif args.command == "monitor":
    with open(args.file, "r", encoding="utf-8") as f:
        f.seek(0, 2)  
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue
            if re.search(args.contains, line):
                print(line.strip())
import re

url_pattern = r"https?://[^\s]+"
error_pattern = r"[45]\d{2}"

line = "2025-11-27 20:02:00 GET https://example.com/api/data 404 192.168.1.10 user@test.com"

print(re.findall(url_pattern, line))   
print(re.findall(error_pattern, line)) 
