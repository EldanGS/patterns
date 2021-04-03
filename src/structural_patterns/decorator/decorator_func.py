def benchmark(func_to_decorate):
    import time

    def wrapper():
        start = time.time()
        func_to_decorate()
        end = time.time()

        print(f"Time: {end - start}")

    return wrapper


@benchmark
def fetch_web_page():
    import requests

    webpage = requests.get("https://google.com")
    print(webpage)


# fetch_web_page = benchmark(fetch_web_page)
# fetch_web_page()


def set_arguments(func_to_decorate):
    import functools

    @functools.wraps(func_to_decorate)
    def wrapper(arg1, arg2):
        print("Set arguments here", arg1, arg2)
        func_to_decorate(arg1, arg2)

    return wrapper


@set_arguments
def print_full_name(first, second):
    print("My name is:", first, second)


print_full_name("Alexander", "Mustache")

print(print_full_name)
