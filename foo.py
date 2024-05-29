timeout_max_retry_count = 2
timeout_max_retry_count=int(timeout_max_retry_count)
total_pending_request_count = 3
max_retry_count = timeout_max_retry_count * total_pending_request_count

print(max_retry_count)
print(type(max_retry_count))
if 9 >= max_retry_count:
    print("true")
else:
    print("false")
