import requests
import sys
import time


class Client:

    def __init__(self):
        self.server_url = 'http://127.0.0.1:5000/'
        self.refresh_rate = 1  # Refresh rate in seconds
        self.previous_prompts = None

    def run(self):

        while True:
            new_prompts = self.get_prompts()
            if new_prompts != self.previous_prompts:
                print("New prompts!")
                print(new_prompts)
                self.previous_prompts = new_prompts

                # TODO TdR 19/11/16: do something with user input.

            time.sleep(self.refresh_rate)

    def do_query(self, fun_name):
        url = self.server_url + fun_name
        return requests.get(url).text

    def get_schedule(self):
        return self.do_query('schedule')

    def get_prompts(self):
        return self.do_query('prompts')


def smoke_test():
    c = Client()
    print(c.do_query(''))
    print(c.get_schedule())
    print(c.get_prompts())
    return True


if __name__ == "__main__":
    # if not smoke_test():
    #     sys.exit(1)

    c = Client()
    c.run()
