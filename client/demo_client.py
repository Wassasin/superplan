import requests
import datetime
import json


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
        # self.refresh_rate = 5  # Refresh rate in seconds
        self.previous_state = ClientState(None, None)

    def run(self):

        current_time = datetime.timedelta(hours=4)
        while True:
            print("It is currently {}.".format(current_time))
            state = self.get_new_state(current_time)

            if state == self.previous_state:
                pass
            else:
                print("New things!")
                print(state.prompts)
                print(state.schedule)
                self.previous_state = state

            # TODO TdR 19/11/16: do something with user input.

            x = raw_input("Press ENTER to continue 30 minutes.")
            current_time += datetime.timedelta(minutes=30)

    def get_new_state(self, current_time=None):
        vals = self.get_schedule(current_time)
        print(vals)
        vals = json.loads(vals)
        print(vals)
        schedule, prompts = vals["events"], vals["prompts"]
        state = ClientState(prompts, schedule)
        return state

    def do_query(self, fun_name, params=None):
        url = self.server_url + fun_name

        if params is None:
            params = {}
        return requests.get(url, params).text

    def get_schedule(self, timedelta_obj=None):

        # TODO TdR 19/11/16: add get request argument.
        if timedelta_obj is not None:
            time_obj = (datetime.datetime.min + timedelta_obj).time()
            return self.do_query('schedule', {'time': str(time_obj)})
        return self.do_query('schedule')


def smoke_test():
    c = Client()
    print(c.do_query(''))
    print(c.get_schedule())
    return True


if __name__ == "__main__":
    # if not smoke_test():
    #     sys.exit(1)
    c = Client()
    c.run()
