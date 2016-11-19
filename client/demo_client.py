import requests
import time


class ClientState:

    def __init__(self, prompts, schedule):
        self.prompts = prompts
        self.schedule = schedule

    def __eq__(self, state):
        return str(self.prompts) == str(state.prompts) and \
               self.schedule == state.schedule

    def __ne__(self, state):
        return not self.__eq__(state)


class Client:

    def __init__(self):
        self.server_url = 'http://127.0.0.1:5000/'
        self.refresh_rate = 5  # Refresh rate in seconds
        self.previous_state = ClientState(None, None)

    def run(self):

        while True:
            state = self.get_new_state()

            if state == self.previous_state:
                continue

            print("New things!")
            print(state.prompts)
            print(state.schedule)
            self.previous_state = state

            # TODO TdR 19/11/16: do something with user input.

            time.sleep(self.refresh_rate)


    def get_new_state(self):
        time = None
        prompts = self.get_prompts(time)
        schedule = self.get_schedule()
        state = ClientState(prompts, schedule)
        return state

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
