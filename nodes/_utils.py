from datetime import datetime


def wrap_agent(name, func, log_list):
    """
    Wrap a LangGraph agent node to track its execution timeline and updated state.
    Appends log to log_list after execution.
    """

    def wrapped(state):
        start = datetime.now()
        new_state = func(state)
        duration = (datetime.now() - start).total_seconds()

        log_list.append(
            {
                "agent": name,
                "time": start.strftime("%H:%M:%S"),
                "duration": duration,
                "state": new_state.copy(),  # Shallow copy of updated state
            }
        )

        return new_state

    return wrapped
