# ------------------------------------------------------------
class Queue:

	def __init__(self):
		self.events = []

	def push(self, data):
		self.events.append(data)
		return data

	def pop(self):
		return self.events.pop(0)

	def is_null(self):
		return len(self.events) == 0

# ------------------------------------------------------------
class EventStatus:
    def __init__(self, status_type):
        self.event_type = 'S'
        self.status_type = status_type
        self.retry_count = 0


# ------------------------------------------------------------
class EventRequest:
    def __init__(self):
        self.event_type = 'R'
        self.retry_count = 0


# ------------------------------------------------------------
def eval_events(event_queue):
    status = None
    while not event_queue.is_null():
        popped_event = event_queue.pop()
        if popped_event.event_type == 'S':
            status = popped_event.status_type
            status_event_update(event_queue,popped_event)
        elif popped_event.event_type == 'R':
            request_event_update(event_queue, popped_event, status)


# ------------------------------------------------------------
def status_event_update(event_queue, popped_event):

    print('EventStatus: {0}, {1}, {2}'.format(\
        popped_event.event_type, popped_event.status_type,\
            popped_event.retry_count))

    if (popped_event.status_type == 'C' or \
        popped_event.status_type == 'T') and\
        (popped_event.retry_count < 2):

        popped_event.retry_count += 1
        event_queue.push(popped_event)


# --------------------------------------------------------------
def request_event_update(event_queue, popped_event, status):

    if status == 'C' or status == 'T':
        print('EventRequest: {0}, {1}'.format(\
            popped_event.event_type, popped_event.retry_count))
    else:
        popped_event.retry_count += 1
        event_queue.push(popped_event)


# ---------------------------------------------------------------
if __name__ == '__main__':

    queue = Queue()

    queue.push(EventStatus('P'))
    queue.push(EventRequest())
    queue.push(EventStatus('M'))
    queue.push(EventStatus('P'))
    queue.push(EventStatus('T'))
    queue.push(EventStatus('P'))
    queue.push(EventStatus('C'))
    queue.push(EventStatus('M'))

    eval_events(queue)

    # while(1):
    #     choice = int(input("Enter number: 1.Input Event\n 2.Exit"))
    #     if choice == 1:
    #         event_type_num = int(input("Enter number: 1.Event Status\n 2.Event Request"))
            
    #     else:
    #         break