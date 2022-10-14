import os
with open(os.path.dirname(__file__) + "/../apache_logs_big","r") as f:
    lines = f.readlines()
    requests = list()
    for line in lines:
        requests.append(line.split(" "))

    # request_counts = {}

    # for req in requests:
    #     status_code = req[8]
    #     if status_code not in request_counts:
    #         request_counts[status_code] = 0
    #     request_counts[status_code] += 1

    # sorted_keys = sorted(list(request_counts.keys()))

    # for key in sorted_keys:
    #     print(request_counts[key], key)
    # print(request_counts)
  