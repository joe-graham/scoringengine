import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../scoring_engine'))

from worker_queue import WorkerQueue
from job_queue import JobQueue


class TestWorkerQueue(object):

    def test_init(self):
        queue = WorkerQueue()
        assert isinstance(queue, JobQueue) is True
        assert queue.queue_name == "queued"
        assert queue.queue_key == "scoring_engine:queued"
